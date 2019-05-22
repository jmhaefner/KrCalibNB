import tables as tb
import time

t0 = time.time()

vocal = False
startRun = 6351
endRun = 7120
runs = [x for x in range(startRun, endRun)]
triggers = ['trigger1', 'trigger2']

output = open('investigate_kr_s2_times_output.txt', 'w')

def FourDigit(x):
    num = str(x)
    while len(num) < 4:
        num = '0' + num
    return num

def print_s2(vec):
    print(str(vec[0])+' \t'+str(vec[1])+'\t'+str(vec[2])+'\t'+str(vec[3]))

print(">>> RUN", run, "<<<")

import os, os.path

# print len([name for name in os.listdir('.') if os.path.isfile(name)])

for run in runs:
    for trigger in triggers:
        print('\n'+trigger)
        print(run)
        numBacksteps = []
        allFiles = []
        pmap_dir = "/analysis/"+str(run)+"/hdf5/prod/v0.9.9/20180921/pmaps/"+trigger+"/"
        fileMax = len([name for name in os.listdir(pmap_dir)])
        print(str(fileMax)+' files in '+pmap_dir)

        if fileMax > 0:
            for x in range(fileMax):
                backsteps = 0

                output.write('EXAMINING '+str(run)+' '+trigger+' '+FourDigit(x)+'\n')
                try:
                    h5file = tb.open_file("/analysis/"+str(run)+"/hdf5/prod/v0.9.9/20180921/pmaps/"+trigger+"/pmaps_"+FourDigit(x)+"_"+str(run)+"_"+trigger+"_v0.9.9_20180921_krbg1300.h5", mode="r", title="Test file")
                except:
                    print('could not open ',"/analysis/"+str(run)+"/hdf5/prod/v0.9.9/20180921/pmaps/"+trigger+"/pmaps_"+FourDigit(x)+"_"+str(run)+"_"+trigger+"_v0.9.9_20180921_krbg1300.h5")
                    continue

                allFiles.append(x)
                numToShow = 0
                currentEvent = h5file.root.PMAPS.S2[0][0]
                currentPeak = h5file.root.PMAPS.S2[0][1]
                currentTime = h5file.root.PMAPS.S2[0][2]
                currentCharge = h5file.root.PMAPS.S2[0][3]
                badPeaks = []
                badEvents = []
                badTimes = []

                for s2 in h5file.root.PMAPS.S2:

                    lastEvent = currentEvent
                    lastPeak = currentPeak
                    lastTime = currentTime

                    currentEvent = s2[0]
                    currentPeak = s2[1]
                    currentTime = s2[2]
                    currentCharge = s2[3]

                    #if currentTime == 649926:
                    #    numToShow += 9

                    if (currentEvent == lastEvent) and (currentPeak == lastPeak):
                        if currentTime < lastTime:
                            if vocal:
                                print('\nWARNING: BACKWARDS TIME STEP')
                                print(str(currentTime) + ' < ' + str(lastTime))
                            output.write('Event Peak Time Charge\n')
                            output.write(str(currentEvent)+' '+str(currentPeak)+' '+str(currentTime)+' '+str(currentCharge)+'\n')
                            backsteps += 1
                            numToShow += 3
                            badPeaks.append(currentPeak)
                            badEvents.append(currentEvent)
                            badTimes.append([])

                    if numToShow > 0:
                        if vocal:
                            print_s2(s2)
                            print('Current time  = '+str(currentTime))
                            print('Last time     = '+str(lastTime))
                        numToShow -= 1

                for s2 in h5file.root.PMAPS.S2:

                    currentEvent = s2[0]
                    currentPeak = s2[1]
                    currentTime = s2[2]

                    for i in range(len(badEvents)):
                        if (currentPeak == badPeaks[i]) and (currentEvent == badEvents[i]):
                            badTimes[i].append(currentTime)

                for badTime in badTimes:
                    if vocal:
                        print(badTime)

                h5file.close()
                numBacksteps.append(backsteps)

                # if backsteps > 0:
                    # print('\n!!!!! ->', end = ' ')
                    # print('('+FourDigit(x)+', '+str(backsteps)+')', end = '\t')

                if x % 1000 == 0:
                    print('\n----FILE '+str(x)+'----TIME '+str(round(time.time()-t0))+'----')
        else:
            print('NO FILES FOUND FOR RUN ' + str(run) + ' IN ' + pmap_dir)

        print()
        dt = time.time() - t0
        print('dt = ', dt)

        for nBacksteps in range(max(numBacksteps)+1):
            nFiles = 0
            for back, fileNum in zip(numBacksteps, allFiles):
                if back == nBacksteps:
                    nFiles += 1
            print(nFiles, 'files with', nBacksteps, 'backsteps')

        # for file, backstep in zip(allFiles, numBacksteps):
        #    print(file, '\t', backstep)

output.close()
