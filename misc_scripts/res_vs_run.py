import os
import matplotlib.pyplot as plt

allResErrors = []
allWorstResErrors = []
allResolutions = []
allWorstResolutions = []
allRuns = []

minRun = 7318
maxRun = 7436


filePrefix = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/ltMaps/plot_parameters/plot_outputs_'
fileSuffix = '.txt'

# myTags = ['x2rgav190819', 'rg190819', 'rg_loose_190819']
# tagEnglish = ['X2; avg', 'Tight LT cut; avg', 'Loose LT cut; avg']

myTags = ['x2rgav190819','x2rg190819', 'x2rg_wide_190819', 'x2rg_interp_190819']
tagEnglish = ['X2; avg', 'X2; nbhd', 'X2; wide nbhd', 'X2; interpolation']



# myTags = ['x2rgav190819', 'rg190819', 'rg_loose_190819', 'x2rg190819', 'x2rg_wide_190819', 'x2rg_interp_190819']
# tagEnglish = ['X2; avg', 'Tight LT cut; avg', 'Loose LT cut; avg', 'X2; nbhd', 'X2; wide nbhd', 'X2; interpolation']

for tag in range(len(myTags)):
	allResolutionsTag = []
	allWorstResolutionsTag = []
	allWorstResErrorsTag = []
	allResErrorsTag = []
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
				if line.find('FCE:') != -1:
					errList = eval(line[4:len(line)-1])
					err = errList[0][0]
					errBad = errList[len(errList)-1][len(errList[0])-1]
			readText.close()
			allResolutionsTag.append(res)
			allWorstResolutionsTag.append(resBad)
			allResErrorsTag.append(err)
			allWorstResErrorsTag.append(errBad)
		else:
			pass
	allResolutions.append(allResolutionsTag)
	allWorstResolutions.append(allWorstResolutionsTag)
	allResErrors.append(allResErrorsTag)
	allWorstResErrors.append(allWorstResErrorsTag)
	allRuns.append(runsTag)

for run in range(len(allRuns[0])):
	if allResolutions[0][run] < allResolutions[1][run]:
		print('Anomaly in run '+str(allRuns[0][run]))



for tag in range(len(myTags)):
	print(myTags[tag])
	print(allRuns[tag])
	print(allResolutions[tag])
	plt.errorbar(allRuns[tag],allResolutions[tag],yerr = allResErrors[tag], fmt = '--o', label = tagEnglish[tag])
plt.ylabel('Resolution in best volume for Kr-83 (%)')
plt.xlabel('Run number')
plt.legend()
plt.show()

for tag in range(len(myTags)):
	plt.errorbar(allRuns[tag],allResolutions[tag],yerr = allResErrors[tag], fmt = '--o', label = tagEnglish[tag])
plt.xlim(7427, 7436)
plt.ylim(3.75, 4.0)
plt.ylabel('Resolution in best volume for Kr-83 (%)')
plt.xlabel('Run number')
plt.legend()
plt.show()



for tag in range(len(myTags)):
	plt.errorbar(allRuns[tag],allWorstResolutions[tag],yerr = allWorstResErrors[tag], fmt='--o', label = tagEnglish[tag])
plt.ylabel('Resolution in worst volume for Kr-83 (%)')
plt.xlabel('Run number')
plt.legend()
plt.show()

for tag in range(len(myTags)):
	plt.errorbar(allRuns[tag],allWorstResolutions[tag],yerr = allWorstResErrors[tag], fmt = '--o', label = tagEnglish[tag])
plt.xlim(7427, 7436)
plt.ylim(4.25, 4.4)
plt.ylabel('Resolution in worst volume for Kr-83 (%)')
plt.xlabel('Run number')
plt.legend()
plt.show()

for run in range(len(allRuns[0])):
	if allResolutions[0][run] < allResolutions[1][run]:
		print('Anomaly in run '+str(allRuns[0][run]))

print(allWorstResErrors)	
