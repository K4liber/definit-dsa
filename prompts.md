# Create a new definition

Please write a simple definition of a <definition_name> 
using already existing definitions as needed with the same format of 
_get_content method as other definitions have. 
Please also add a new definitions if some are required to create a 
<definition_name> definition.

Please link all the used references in the definition _get_content method.
Each reference should be applied only once. Please use the method ".key.get_reference()".

Please update index.py and track.py with the created definition(s).

Remember to add any definition that is not created yet, but is used in the <definition_name>.

Make sure you do not create circular dependencies between definitions and between fields. 
For example, a definition from mathematics should not depend on any definition from computer_science.

Please create a definition for "Asymptotic runtime". First check all the available categories (subdirectories) under src\definit_db\data\field and if any fits, put it there. If there is no a good category, please create one. Remember to keep the definition simple and add all available references (dependencies on other definitions).