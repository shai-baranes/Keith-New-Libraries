from tqdm import tqdm
import time



# for i in range(1000):
# 	if i % 100 == 0:
# 		print(i) # fallback to trace the status of my progress
# 	time.sleep(0.01)


# tqdm provides you with a nice progress bar for your console
for i in tqdm(range(1000), desc="Basic Loop"): # 'desc' is optional
	time.sleep(0.01)


names = ["Shai", "Merav", "Yoni", "Oshrat"]
[print(name) for name in tqdm(names, desc="Our Family")]