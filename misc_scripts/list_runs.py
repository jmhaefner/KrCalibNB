import os
import sys

start = int(sys.argv[1])
end = int(sys.argv[2])

found_runs = []

for run in range(start, end):
	if os.path.exists('/Volumes/NEXT_data/IC_Data/kdst/'+str(run)+'/'):
		found_runs.append(run)

for run in found_runs:
	print(run, end=' ')

print()
print('Total num = '+str(len(found_runs)))
