from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(32)):
    sleep(0.005)
print()
for elem in tqdm(range(32)):
    sleep(0.005)
print()
for elem in ft_tqdm(range(111)):
    sleep(0.005)
print()
for elem in tqdm(range(111)):
    sleep(0.005)
print()
for elem in ft_tqdm(range(1111)):
    sleep(0.005)
print()
for elem in tqdm(range(1111)):
    sleep(0.005)
print()
