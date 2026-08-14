# Copilot Instructions

## Definition Content Formatting

- Definition content is written as a Python multiline string in `_get_content()`.
- The visualization viewer does not render raw source spacing literally.
- Multiple spaces inside a paragraph are collapsed to a single displayed space.
- Single line breaks inside a paragraph are also collapsed to spaces.
- To create a visible new paragraph or line in the final UI, use an empty line between blocks of text.
- Keep source lines wrapped for Python style and readability, but do not rely on source wrapping for display formatting.
- Do not try to align content with extra spaces or single newlines; the viewer removes that formatting.

## Rendering Path In Visualization

- The definition body is passed from `node.content` into `renderMdToHtml()` in `visualization/src/components/DefinitionTab.tsx`.
- `renderMdToHtml()` first normalizes the markdown with `normalizeMdForViewer()` in `visualization/src/lib/graph.ts`.
- That normalization removes leading and trailing blank lines, collapses internal blank lines, and flattens each paragraph into a single line of text.
- Dependency references written as markdown links like `[label](definition_id)` are converted into clickable dependency spans in the viewer.
- Because of this pipeline, write examples in source as logically separated paragraphs and let the viewer handle the final presentation.

## Writing Examples

- Prefer clean, source-friendly prose with explicit paragraph breaks for example steps or result blocks.
- Use a blank line to separate each step or displayed result that should stay visually distinct.
- If an example should appear as one continuous paragraph in the UI, keep it as one paragraph in the source even if it is wrapped across multiple source lines.