import { mkdtemp, readFile, rm, writeFile, mkdir } from 'node:fs/promises';
import { join } from 'node:path';
import { tmpdir } from 'node:os';

import { afterEach, describe, expect, it } from 'vitest';

import { generateData } from '../../scripts/gen-data.mjs';
import type { DefGraph } from '../../src/types';

const tempDirs: string[] = [];

async function makeTempDir(): Promise<string> {
  const dir = await mkdtemp(join(tmpdir(), 'definit-db-vis-'));
  tempDirs.push(dir);
  return dir;
}

async function writeDefinition(defsRoot: string, relPath: string, content: string): Promise<void> {
  const filePath = join(defsRoot, `${relPath}.md`);
  await mkdir(join(filePath, '..'), { recursive: true });
  await writeFile(filePath, content, 'utf8');
}

afterEach(async () => {
  await Promise.all(tempDirs.splice(0).map((dir) => rm(dir, { recursive: true, force: true })));
});

describe('gen-data script', () => {
  it('generates defs.json from markdown input', async () => {
    const root = await makeTempDir();
    const defsRoot = join(root, 'definitions');
    const indexPath = join(root, 'index.md');
    const outPath = join(root, 'out', 'defs.json');

    await writeFile(
      indexPath,
      ['- [object](mathematics/fundamental/object)', '- [set](mathematics/fundamental/set)'].join('\n'),
      'utf8',
    );
    await writeDefinition(defsRoot, 'mathematics/fundamental/object', '# object\n\nAn object.\n');
    await writeDefinition(
      defsRoot,
      'mathematics/fundamental/set',
      '# set\n\nA [set](mathematics/set) is a collection of [object](mathematics/object).\n',
    );

    const { graph } = await generateData({ indexPath, defsRoot, outPath });
    const saved = JSON.parse(await readFile(outPath, 'utf8')) as DefGraph;

    expect(graph.nodes).toHaveLength(2);
    expect(saved.nodes.map((node) => node.id)).toEqual(['mathematics/object', 'mathematics/set']);
    expect(saved.edges).toEqual([{ source: 'mathematics/set', target: 'mathematics/object' }]);
  });

  it('throws on cyclic dependencies in generated data', async () => {
    const root = await makeTempDir();
    const defsRoot = join(root, 'definitions');
    const indexPath = join(root, 'index.md');
    const outPath = join(root, 'out', 'defs.json');

    await writeFile(
      indexPath,
      ['- [alpha](mathematics/fundamental/alpha)', '- [beta](mathematics/fundamental/beta)'].join('\n'),
      'utf8',
    );
    await writeDefinition(defsRoot, 'mathematics/fundamental/alpha', '# alpha\n\nSee [beta](mathematics/beta).\n');
    await writeDefinition(defsRoot, 'mathematics/fundamental/beta', '# beta\n\nSee [alpha](mathematics/alpha).\n');

    await expect(generateData({ indexPath, defsRoot, outPath })).rejects.toThrow(/Cycle detected/i);
  });
});