import fs from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const repoRoot = path.resolve(__dirname, '..');
const indexPath = path.resolve(repoRoot, '../src/definit_db/data_md/index.md');
const defsRoot = path.resolve(repoRoot, '../src/definit_db/data_md/definitions');
const outPath = path.resolve(repoRoot, './public/defs.json');

export async function parseIndex(md, defsRootPath = defsRoot) {
  // lines like: - [object](mathematics/object)
  const items = [];
  const re = /^-\s+\[([^\]]+)\]\(([^)]+)\)\s*$/;

  for (const line of md.split(/\r?\n/)) {
    const m = re.exec(line.trim());
    if (!m) continue;
    const title = m[1];
    // The link path is the definition id in the `<field>/<name>` form.
    const id = m[2].replace(/\.md$/i, '');

    const contentFilePath = path.resolve(defsRootPath, `${id}.md`);
    const content = await readIfExists(contentFilePath);

    if (!content) {
      // Definition file is missing; raise an exception to catch during dev.
      throw new Error(`Definition file not found: ${contentFilePath}`);
    }

    items.push({ id, title, content });
  }
  return items;
}

export async function readIfExists(p) {
  try {
    return await fs.readFile(p, 'utf8');
  } catch {
    return null;
  }
}

export function extractAliases(content) {
  // The serialized heading carries aliases as "# name (alias1, alias2)".
  // Names never contain parentheses; alias lists may nest them (e.g. "O(log n)").
  const firstLine = String(content ?? '')
    .split(/\r?\n/)
    .map((l) => l.trim())
    .find((l) => l.length > 0) ?? '';

  const m = /^#\s+(.+?)\s*\((.+)\)\s*$/.exec(firstLine);
  if (!m) return [];

  return m[2]
    .split(',')
    .map((a) => a.trim())
    .filter(Boolean);
}

export function normalizeHrefToId(href, knownIds) {
  const clean = String(href ?? '').trim();
  if (!clean) return null;
  if (clean.startsWith('#')) return null;

  // strip anchors/query
  const noHash = clean.split('#')[0].split('?')[0];

  // ignore external urls
  if (/^[a-z]+:\/\//i.test(noHash)) return null;

  // remove leading ./ and trailing .md
  const p = noHash.replace(/^\.\//, '').replace(/\.md$/i, '');
  if (!p.includes('/')) return null;

  // Exact match against known definition ids
  return knownIds.has(p) ? p : null;
}

export function extractDeps(md, ctx, knownIds, stats) {
  // Dependencies are definition references written inside the content:
  // [label](field/name) where the href is exactly a known definition id.
  // Self-references and non-definition links are ignored.

  const deps = new Set();

  const linkRe = /\[([^\]]+)\]\(([^)]+)\)/g;
  for (const m of md.matchAll(linkRe)) {
    const href = (m[2] ?? '').trim();

    const rel = normalizeHrefToId(href, knownIds);
    if (rel) {
      if (rel !== ctx.id) deps.add(rel);
      continue;
    }

    // Track unresolved href-based refs (useful to tune parsing).
    if (href && href.includes('/') && !href.startsWith('#') && !/^[a-z]+:\/\//i.test(href)) {
      stats.unresolvedHref++;
    }
  }

  return [...deps];
}

export function computeLevels(nodes) {
  // Kept for cycle detection + dep filtering; UI computes levels dynamically.
  const byId = new Map(nodes.map((n) => [n.id, n]));

  // keep only deps that exist in index
  for (const n of nodes) {
    n.deps = n.deps.filter((d) => d && byId.has(d) && d !== n.id);
  }

  // DFS to detect cycles; we also compute a temporary level to preserve previous validation behavior.
  const visiting = new Set();
  const visited = new Set();
  const stack = [];

  function formatNode(id) {
    const n = byId.get(id);
    if (!n) return id;
    return n.id;
  }

  function dfs(id) {
    if (visited.has(id)) return byId.get(id).level;

    if (visiting.has(id)) {
      const start = stack.indexOf(id);
      const cycleIds = start >= 0 ? stack.slice(start).concat(id) : [id, id];
      const cyclePretty = cycleIds.map(formatNode).join(' -> ');

      const hopDetails = [];
      for (let i = 0; i < cycleIds.length - 1; i++) {
        const a = cycleIds[i];
        const b = cycleIds[i + 1];
        const an = byId.get(a);
        hopDetails.push(`${formatNode(a)} depends on ${formatNode(b)} (deps: ${an?.deps?.length ?? 0})`);
      }

      console.error('\nCYCLE DETECTED');
      console.error(cyclePretty);
      console.error('\nHOPS');
      for (const line of hopDetails) console.error(`- ${line}`);
      console.error('');

      throw new Error(`Cycle detected involving ${id}`);
    }

    visiting.add(id);
    stack.push(id);

    const n = byId.get(id);
    let lvl = 0;
    for (const dep of n.deps) {
      lvl = Math.max(lvl, dfs(dep) + 1);
    }
    n.level = lvl;

    stack.pop();
    visiting.delete(id);
    visited.add(id);

    return lvl;
  }

  for (const n of nodes) dfs(n.id);
}

export async function generateData({
  indexPath: customIndexPath = indexPath,
  defsRoot: customDefsRoot = defsRoot,
  outPath: customOutPath = outPath,
} = {}) {
  const indexMd = await fs.readFile(customIndexPath, 'utf8');
  const items = await parseIndex(indexMd, customDefsRoot);

  const nodes = [];
  const stats = { unresolvedHref: 0 };

  // known definition ids for dependency resolution
  const knownIds = new Set(items.map((it) => it.id));

  for (const it of items) {
    const deps = extractDeps(it.content, it, knownIds, stats);
    const aliases = extractAliases(it.content);
    nodes.push({ ...it, aliases, deps, level: 0, content: it.content });
  }

  // Validate deps and detect cycles (also assigns temporary levels on nodes).
  computeLevels(nodes);

  const edges = [];
  for (const n of nodes) {
    for (const dep of n.deps) edges.push({ source: n.id, target: dep });
  }

  const graph = { nodes, edges };
  await fs.mkdir(path.dirname(customOutPath), { recursive: true });
  await fs.writeFile(customOutPath, JSON.stringify(graph, null, 2), 'utf8');

  return {
    graph,
    stats,
    outPath: customOutPath,
  };
}

const isMain = process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url);

if (isMain) {
  generateData()
    .then(({ graph, stats, outPath: writtenOutPath }) => {
      console.log(
        `Wrote ${writtenOutPath} (nodes=${graph.nodes.length}, edges=${graph.edges.length}, unresolvedHref=${stats.unresolvedHref})`
      );
    })
    .catch((e) => {
      console.error(e);
      process.exit(1);
    });
}
