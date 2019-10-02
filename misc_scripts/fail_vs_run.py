import os
import matplotlib.pyplot as plt

allFailures = []
numFailures = []
runs = []

# minRun = 6900
# maxRun = 7600

minRun = 7504
maxRun = 7506


filePrefix = '/Volumes/NEXT_data/IC_Data/plots/st190819/text_outputs/outputs_'

for run in range(minRun, maxRun):
	myFile = filePrefix + str(run) + '.txt'
	textExists = os.path.isfile(myFile)
	if textExists:
		readText = open(myFile, 'r')
		for line in readText.readlines():
			if line.find('failedfit=') != -1:
				failed = eval(line[10:len(line)-1])
				runs.append(run)
		readText.close()
		numFailures.append(len(failed))
		allFailures.append(failed)
	else:
		pass

print(runs)
print(numFailures)

plt.plot(runs, numFailures, 'o')
plt.show()

plt.plot(runs, numFailures, 'o') 
plt.ylim(0,250)
plt.show()

cutoff = 250
for run, fails in zip(runs, numFailures):
	if fails > cutoff:
		print(str(run) + ' ' + str(fails))	
