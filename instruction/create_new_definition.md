Inside file `src\definit_db\data_md\index.md` all currently created definitions can be found.

Inside directory `src\definit_db\data` we place all definitions in the form of python modules. Each module should be named after the definition it contains, and the definition itself should be a class with the same name as the module. Each module should contain only one definition. Each module is placed in a subdirectory named after the category of the definition. For example, if we have a definition of a "User", it should be placed in a module named `user.py` inside a subdirectory named `entities`. The class inside `user.py` should be named `User`. This structure helps to keep the definitions organized and easy to find.

When creating a new definition, you should follow these steps:

0. Check if a new definition does not exist already. All the existing definitions can be found here: `src\definit_db\data_md\index.md`.
1. Determine the category of the definition (e.g., mathematics\foundamental, computer_science\algorithms\searching, etc.).
2. Create a new subdirectory inside `src\definit_db\data` with the name of the category if it does not already exist.
3. Create a new python module inside the category subdirectory with the name of the definition (e.g., `user.py` for a "User" definition).
4. Inside the module, define a definition class with the same name as the module (e.g., `User` class inside `user.py`).
5. Figure out dependencies of the definition and import them if necessary.
6. If any dependency is not created yet, you should create it first before creating the new definition. This will ensure that all dependencies are properly defined and can be used in the new definition without any issues. If any of the dependencies of dependency does not exist - please create it as well.
7. You should replace all used definitions in the new definition with their corresponding classes. For example, if the "User" definition has a dependency on a "Profile" definition, you should import the "Profile" class and use it in the "User" class instead of just mentioning "Profile".
8. Add the new definition to the field index (for example `src\definit_db\data\field\computer_science\__init__.py` in case of a computer science definition) if it belongs to a specific field. This will help to keep track of all definitions in that field and make it easier to find them later.
9. Run all tests inside `test` directory to ensure that the new definition does not break any existing functionality and that it works as expected. This is an important step to maintain the integrity of the codebase and to catch any potential issues early on.
10. Review the create definitions. Check if all references are used and if they make sense.
11. Run ruff check and fix the issues if there are any: `uv run ruff check --fix .`.

Please now create a new definition following the above steps.
The new definition is "LRU cache".
