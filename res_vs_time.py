import os
import matplotlib.pyplot as plt

# Makes a plot of lifetime through the listed runs,
# with the date on the x axis. Also outputs a .txt
# containing run - date - lifetime

minRun = 6300
# minRun = 7000
maxRun = 7100
allRuns = []
allRes = []
allResErrs = []
allDates = []

allResVecs = []
allZVecs = []
allRVecs = []

neededRuns = []

def getDateFromRun(nRun, early):

    input_path  = "/Volumes/NEXT_data/IC_Data/kdst"
    output_path = "/Volumes/NEXT_data/IC_Data/dst"
    log_path    = "/Volumes/NEXT_data/IC_Data/log"
    trigger     = 'trigger1'
    file_range  = 0, 3

    if not early:
        tags = 'v0.9.9_20190111_krbg'
    else:
        tags = 'v0.9.9_20181011_krbg'

    from krcal.core.io_functions import filenames_from_paths
    input_dst_filenames, output_dst_filename, log_filename = filenames_from_paths(nRun,
                                                                                  input_path,
                                                                                  output_path,
                                                                                  log_path,
                                                                                  trigger,
                                                                                  tags,
                                                                                  file_range)

    print('TRYING TO LOAD '+input_dst_filenames[0])
    from invisible_cities.io.dst_io import load_dsts
    dst = load_dsts(input_dst_filenames, "DST", "Events")

    from krcal.core.ranges_and_bins_functions import kr_ranges_and_bins
    krTimes, krRanges, krNbins, krBins = kr_ranges_and_bins(dst,
                                                        xxrange   = (-220,  220),
                                                        yrange    = (-220,  220),
                                                        zrange    = (10,  550),
                                                        s2erange  = (3000, 13000),
                                                        s1erange  = (3, 25),
                                                        s2qrange  = (200, 800),
                                                        xnbins    = 50,
                                                        ynbins    = 50,
                                                        znbins    = 50,
                                                        s2enbins  = 50,
                                                        s1enbins  = 50,
                                                        s2qnbins  = 50,
                                                        tpsamples = 3600) # tsamples in seconds

    full_final_datetime = str(krTimes.timeStamps[-1])
    final_date = full_final_datetime[:full_final_datetime.find(' ')]
    return final_date

def splitDate(myDate):
    day = int(myDate[len(myDate)-2:])
    month = int(myDate[5:len(myDate)-3])
    year = int(myDate[:4])
    return (year, month, day)


for nRun in range(minRun, maxRun):
    textFile = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/ltMaps/plot_parameters/plot_outputs_'+str(nRun)+'.txt'
    dateFile = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/slides/run'+str(nRun)+'.tex'
    textExists = os.path.isfile(textFile)
    dateExists = os.path.isfile(dateFile)
    if textExists and dateExists:

        # Determine the resolution
        readText = open(textFile, 'r')
        res = ''
        resVec = []
        zVec = []
        rVec = []
        err = ''
        for line in readText.readlines():
            if line.find('FC:') != -1:
                res = line[5:line.find(',')-1]
                resVec = eval(line[3:len(line)-1])
            if line.find('Zi:') != -1:
                zVec = eval(line[3:len(line)-1])
            if line.find('Ri:') != -1:
                rVec = eval(line[3:len(line)-1])
            if line.find('FCE:') != -1:
                err = line[6:line.find(',')-1]
        readText.close()

        # Determine the date
        dateFailed = False
        date = ''
        try:
            readDate = open(dateFile, 'r')
            for line in readDate.readlines():
                if line.find('date & ') != -1:
                    date = line[7:len(line)-4]
                    date = splitDate(date)
            readDate.close()
        except:
            dateFailed = True

        if res != 'nan' and not dateFailed:
            allRuns.append(nRun)
            allRes.append(float(res))
            allResErrs.append(float(err))
            allResVecs.append(resVec)
            allZVecs.append(zVec)
            allRVecs.append(rVec)
            allDates.append(date)
        if res == 'nan':
            print('WARNING: NAN IN RUN '+str(nRun))
        if dateFailed:
            print('WARNING: BAD DATE IN '+str(nRun))
    else:
        pass

    if textExists and not dateExists:
        neededRuns.append(nRun)

    if dateExists and not textExists:
        print('cannot find '+textFile)
# Convert tuple dates to matplotlib dates
# import matplotlib.dates as mpldates
import datetime
mplAllDates = []
for date in allDates:
    mplDate = datetime.date(date[0], date[1], date[2])
    mplAllDates.append(mplDate)

print('Half done runs:')
for nRun in neededRuns:
    print(nRun, end = ' ')
print()

outputTxt = open('res_vs_time_'+str(minRun)+'_'+str(maxRun)+'.txt','w+')
outputTxt.write('Run Date Resolution\n')
for i in range(len(allRuns)):
    outputTxt.write(str(allRuns[i])+' '+str(mplAllDates[i])+' '+str(allRes[i])+'\n')
outputTxt.close()

print('Rs = ')
print(allRVecs[0])
print('Zs = ')
print(allZVecs[0])


import pylab
import matplotlib.dates
import matplotlib.ticker as mticker

lowerCutoff = 3.4 # resolution is never better than this
poorCutoff = 5 # resolutions worse than this are considered "bad"
histCutoff = 4.4 # histogram cutoff is tighter for fit

numBadRuns = 14 # observationally, 14 runs look consistently worse
worstRuns = [] # the list of 14 bad runs
worstRess = [] # the worst fiducial resolutions
resBad = [False for x in range(len(allResVecs))]

testWorstResVec = [allResVecs[x][0][0] for x in range(len(allResVecs))]

for runIndex in range(len(allRuns)):
    numWorse = 0
    for compare in testWorstResVec:
        if compare > testWorstResVec[runIndex]:
            numWorse += 1
    if numWorse < 14:
        worstRuns.append(allRuns[runIndex])
        worstRess.append(testWorstResVec[runIndex])
        resBad[runIndex] = True

print('Worst runs:')
print(worstRuns)

for ri in range(len(allRVecs[0])):
    for zi in range(len(allZVecs[0])):

        # plt.plot_date(mplAllDates, resVals)
        resVals = [allResVecs[run][ri][zi] for run in range(len(allResVecs))]

        # Plot regular resolutions
        fig, ax = plt.subplots()
        ax.plot(mplAllDates, resVals, 'o')
        fig.autofmt_xdate()
        numTicks = 8
        ax.xaxis.set_major_locator(mticker.MaxNLocator(numTicks+1))
        plt.ylabel('Resolution (r < '+str(allRVecs[0][ri])+', z < '+str(allZVecs[0][zi])+')')
        ax.set_ylim(lowerCutoff,poorCutoff)
        plt.xlabel('Date')
        plt.show()

        # Plot poor resolutions
        fig, ax = plt.subplots()
        ax.plot(mplAllDates, resVals, 'o')
        fig.autofmt_xdate()
        numTicks = 8
        ax.xaxis.set_major_locator(mticker.MaxNLocator(numTicks+1))
        plt.ylabel('Resolution (r < '+str(allRVecs[0][ri])+', z < '+str(allZVecs[0][zi])+')')
        ax.set_ylim(poorCutoff, 15)
        plt.xlabel('Date')
        plt.show()

        # Histogram resolutions
        resValsCut = [] # Cut out the resolutions from the worst runs
        for i in range(len(resVals)):
            if not resBad[i]:
                resValsCut.append(resVals[i])

        # Plot histogram with all runs
        n, bins, patches = plt.hist(resVals, 90)
        plt.title('Resolution distribution full (r < '+str(allRVecs[0][ri])+', z < '+str(allZVecs[0][zi])+')')
        plt.xlabel('Resolution at 41.5 keV (%)')
        plt.show()

        from scipy.stats import norm
        import matplotlib.mlab as mlab


        # Plot histogram with poor runs cut out, and fit gaussian
        n, bins, patches = plt.hist(resValsCut, 30, density = 1)
        (mu, sigma) = norm.fit(resValsCut)
        y = norm.pdf(bins, mu, sigma)
        l = plt.plot(bins, y, 'r--', linewidth=2, label='fit mu = '+str(round(mu,2))+', sigma = '+str(round(sigma,3)))
        plt.title('Resolution distribution cut (r < '+str(allRVecs[0][ri])+', z < '+str(allZVecs[0][zi])+')')
        plt.xlabel('Resolution at 41.5 keV (%)')
        plt.legend()
        plt.show()
