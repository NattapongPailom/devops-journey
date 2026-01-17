disk_size = 100
used_space = 85

usage_percent = (used_space / disk_size) * 100

print(f"Disk Use:{usage_percent}%")

if usage_percent  > 85:
	print("Alert: Disk space is runing low!")
else:
	print("System OK")
