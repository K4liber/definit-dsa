# Review definition agent

## General Definition Guidelines

<data_md_file_path> = `src\definit_db\data_md`
<index_md_file_path> = <data_md_file_path>\index.md`

Inside file <index_md_file_path> all currently created definitions can be found.

Inside directory `src\definit_db\data\field` we place all definitions in the form of python modules. Each module should be named after the definition it contains, and the definition itself should be a class with the same name as the module. Each module should contain only one definition. Each module is placed in a subdirectory named after the category of the definition. For example, if we have a definition of a "User", it should be placed in a module named `user.py` inside a subdirectory named `entities`. The class inside `user.py` should be named `User`. This structure helps to keep the definitions organized and easy to find.

## Review definition steps

1. [COMPLETE] Check if the definition is accurate and complete.
2. [CONCISE] Check if the definition is not complex and if it is easy to understand.
3. [HIERARCHY] Make sure that each definition reference is a lower-level definition. For example, if a definition A references another definition B, then B should not reference A or any other definition that references A. This will help to avoid circular dependencies and make the definitions easier to understand. You need to understand the hierarchy of definitions and make sure that each definition only references definitions that are lower in the hierarchy. This will help to create a clear and organized structure for the definitions and make it easier for users to understand how the definitions relate to each other.
4. [EXAMPLE] Check if a definition content contains an example that illustrates the definition. If does, please place it under a new segment under the content, and split it with a `---` separator. If it does not, please create an example that illustrates the definition. Every concept mentioned in the example that exists as a lower-level definition must be added as a formal reference (import + `get_reference()` call) — do not leave referenced concepts as plain text. The example does not need to reference all definitions that the definition body has, only those actually used in the example. The same hierarchy rule from step 3 applies: only reference definitions that are lower-level than the current one. If an example would naturally mention a higher-level definition (e.g. a specific algorithm when defining a general concept), then a different example should be created that does not reference the higher-level definition.
5. [REFERENCES] Please add missing references to other definitions if there are any. To find missing references, compare every word/phrase used in the definition's content (both the main body and the example) against the full list of definitions in <index_md_file_path>: for each term in the content that matches an existing lower-level definition (per the HIERARCHY rule in step 3), add a formal reference (import + `get_reference()` call) instead of leaving it as plain text. Do this systematically — scan the whole content rather than relying only on the terms that stand out first — since it is easy to miss less obvious matches (e.g. generic words like "operation", "root", or "worst case" that happen to have their own definition). If a matching definition does not exist yet, please create it first before adding it as a reference. A concept only needs to be referenced once per definition — if a term is mentioned multiple times, add the reference on its first occurrence and leave the rest as plain text.

## Instruction execution

Please now review the definition "XXX".
