import os
import sys
os.chdir('../ex02')

sys.path.append(os.getcwd())
from load_image import ft_load
print(ft_load("../testers/landscape.jpg"))
print(ft_load("../testers/landscapea.jpg"))
print(ft_load("../testers/test.png"))