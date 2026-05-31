## General Definition Guidelines

<index_md_file_path> = `src\definit_db\data_md\index.md`

Inside file <index_md_file_path> all currently created definitions can be found.

Inside directory `src\definit_db\data` we place all definitions in the form of python modules. Each module should be named after the definition it contains, and the definition itself should be a class with the same name as the module. Each module should contain only one definition. Each module is placed in a subdirectory named after the category of the definition. For example, if we have a definition of a "User", it should be placed in a module named `user.py` inside a subdirectory named `entities`. The class inside `user.py` should be named `User`. This structure helps to keep the definitions organized and easy to find.

## Review definition steps

1. Check if the definition is accurate and complete.
2. Check if the definition is not complex and if it is easy to understand.
3. Check if a definition content contains an example that illustrates the definition. If does, please place it under a new segment under the content, and split it with a `---` separator. If it does not, please create an example that illustrates the definition. Please use references in the example. The example should be simple and does not contain references to higher-level definitions.
4. Please add missing references to other definitions if there are any. If you find any reference that does not exist yet, please create it first before adding it as a reference to the definition.
5. Make sure that each definition reference is a lower-level definition. For example, if a definition A references another definition B, then B should not reference A or any other definition that references A. This will help to avoid circular dependencies and make the definitions easier to understand. You need to understand the hierarchy of definitions and make sure that each definition only references definitions that are lower in the hierarchy. This will help to create a clear and organized structure for the definitions and make it easier for users to understand how the definitions relate to each other.

## Instruction execution

Please now review all definitions (from the file <index_md_file_path>) following the above steps, starting from the definition `information`. After each definition review, please stop and wait for [HUMAN] feedback on your remarks.
