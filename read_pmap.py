import tables as tb

h5file = tb.open_file("test_pmap.h5", mode="r", title="Test file")

def print_s2(vec):
    print(str(vec[0])+' \t'+str(vec[1])+'\t'+str(vec[2])+'\t'+str(vec[3]))

numToShow = 0
currentEvent = h5file.root.PMAPS.S2[0][0]
currentPeak = h5file.root.PMAPS.S2[0][1]
currentTime = h5file.root.PMAPS.S2[0][2]

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

    #if currentTime == 649926:
    #    numToShow += 9

    if (currentEvent == lastEvent) and (currentPeak == lastPeak):
        if currentTime < lastTime:
            print('\nWARNING: BACKWARDS TIME STEP')
            print(str(currentTime) + ' < ' + str(lastTime))
            numToShow += 3
            badPeaks.append(currentPeak)
            badEvents.append(currentEvent)
            badTimes.append([])

    if numToShow > 0:
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
    print(badTime)

h5file.close()
