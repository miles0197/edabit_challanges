
import psutil

#number of cores
print("Physical corres", psutil.cpu_count(logical = False))
print("Total cores", psutil.cpu_count(logical = True))


#CPU freqeuncies
cpufreq=psutil.cpu_freq()
print(f"Max frequency:{cpufreq.max:.2f'}Mhz")
print(f"Min frequency: {cpufreq.min:.2f'} Mhz")
print(f"Current frequency: {cpufreq.current:.2f'}Mhz")

#CPU usage
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval = 1)):
	print(f"Core {i}: {percentage}%")

print(f"Total CPU usage: {psutil.cpu_percent()}%")
