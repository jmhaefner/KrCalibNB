import os
import matplotlib.pyplot as plt

allResolutions = []
allWorstResolutions = []
allRuns = []

minRun = 7318
maxRun = 7436


filePrefix = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/ltMaps/plot_parameters/plot_outputs_'
fileSuffix = '.txt'

myTags = ['x2rgav190819', 'rg190819', 'rg_loose_190819', 'x2rg190819', 'x2rg_wide_190819', 'x2rg_interp_190819']
tagEnglish = ['X2; avg', 'Tight LT cut; avg', 'Loose LT cut; avg', 'X2; nbhd', 'X2; wide nbhd', 'X2; interpolation']

for tag in range(len(myTags)):
	allResolutionsTag = []
	allWorstResolutionsTag = []
	runsTag = []
	for run in range(minRun, maxRun):
		myFile = filePrefix + str(run) + myTags[tag] + fileSuffix
		textExists = os.path.isfile(myFile)
		if textExists:
			readText = open(myFile, 'r')
			for line in readText.readlines():
				if line.find('FC:') != -1:
					resList = eval(line[3:len(line)-1])
					res = resList[0][0]
					resBad = resList[len(resList)-1][len(resList[0])-1]
					runsTag.append(run)
			readText.close()
			allResolutionsTag.append(res)
			allWorstResolutionsTag.append(resBad)
		else:
			pass
	allResolutions.append(allResolutionsTag)
	allWorstResolutions.append(allWorstResolutionsTag)
	allRuns.append(runsTag)

for tag in range(len(myTags)):
	print(myTags[tag])
	print(allRuns[tag])
	print(allResolutions[tag])
	plt.plot(allRuns[tag],allResolutions[tag],'--o', label = tagEnglish[tag])
plt.ylabel('Resolution in best volume for Kr-83 (%)')
plt.xlabel('Run number')
plt.legend()
plt.show()

for tag in range(len(myTags)):
	plt.plot(allRuns[tag],allWorstResolutions[tag],'--o', label = tagEnglish[tag])
plt.ylabel('Resolution in worst volume for Kr-83 (%)')
plt.xlabel('Run number')
plt.legend()
plt.show()


	
