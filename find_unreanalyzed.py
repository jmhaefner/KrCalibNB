import os

def ltNB(run):
    ltNBprefix = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/ltMaps/single_map_correction_'
    ltNBsuffix = '.ipynb'
    return ltNBprefix + str(run) + ltNBsuffix

def pltOuts(run):
    pltsPrefix = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/ltMaps/plot_parameters/plot_outputs_'
    pltsSuffix = '.txt'
    return pltsPrefix + str(run) + pltsSuffix

def ltExists(run):
    return os.path.isfile(ltNB(run))

def pltsExists(run):
    return os.path.isfile(pltOuts(run))

potentialRuns = [x for x in range(6000,9000)]

incompleteRuns = []

for run in potentialRuns:
    if ltExists(run) and not pltsExists(run):
        incompleteRuns.append(run)

print('Number of incomplete:')
print(len(incompleteRuns))
print('')
print('All incomplete runs:')
incompleteString = ''
for run in incompleteRuns:
    incompleteString += str(run) + ' '
print(incompleteString)
