import subprocess
import os
import tqdm
import numpy as np

times = []
time_max = 0

for i in tqdm.trange(10000):
	#out=subprocess.check_output("time ./.out", shell = True)
	os.system("/usr/bin/time --output=outtime -p sh -c './tau1.out > /dev/null'")
	file = open("outtime", "r")
	file.seek(0)
	f = file.readline()
	file.close()

	time = f[5:9]
	t = float(time)
	times.append(t)
	if t > time_max:
		time_max = t

# Display of all computed datas
Q1 = np.percentile(times, 25)
Q2 = np.percentile(times, 50)
Q3 = np.percentile(times, 75)
print(f"Min  : {times[0]:.2f} s")
print(f"Q1   : {Q1:.2f} s")
print(f"Q2   : {Q2:.2f} s")
print(f"Q3   : {Q3:.2f} s")
print(f"Max  : {times[-1]:.2f} s")
print(f"WCET : {time_max:.2f} s")
