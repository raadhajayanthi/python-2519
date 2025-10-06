# using user defined modules

import my_modules # ModuleNotFoundError: No module named 'my_module'
import my_module_two

print(my_modules.name)
print(my_module_two.name)