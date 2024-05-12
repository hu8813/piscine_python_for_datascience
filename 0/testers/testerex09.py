import os
import sys
os.chdir('../ex09')
sys.path.append(os.getcwd())

from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto")) 
print(count_in_list(["toto", "tata", "toto"], "tutu")) 

