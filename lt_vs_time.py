import os
import matplotlib.pyplot as plt
print('hello world')

# Makes a plot of lifetime through the listed runs,
# with the date on the x axis. Also outputs a .txt
# containing run - date - lifetime

minRun = 6341
maxRun = 6486
allRuns = []
allLts = []
allDates = []

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
    textFile = '/Volumes/NEXT_data/IC_Data/plots/text_outputs/outputs_'+str(nRun)+'.txt'
    dateFile = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/slides/run'+str(nRun)+'.tex'
    textExists = os.path.isfile(textFile)
    dateExists = os.path.isfile(dateFile)
    if textExists and dateExists:

        # Determine the lifetime
        readText = open(textFile, 'r')
        lt = ''
        for line in readText.readlines():
            if line.find('lt=') != -1:
                lt = line[3:len(line)-1]
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

        if lt != 'nan' and not dateFailed:
            allRuns.append(nRun)
            allLts.append(float(lt))
            allDates.append(date)
        if lt == 'nan':
            print('WARNING: NAN IN RUN '+str(nRun))
        if dateFailed:
            print('WARNING: BAD DATE IN '+str(nRun))
    else:
        pass

    if textExists and not dateExists:
        neededRuns.append(nRun)

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

outputTxt = open('lt_vs_time_'+str(minRun)+'_'+str(maxRun)+'.txt','w+')
outputTxt.write('Run Date Lifetime\n')
for i in range(len(allRuns)):
    outputTxt.write(str(allRuns[i])+' '+str(mplAllDates[i])+' '+str(allLts[i])+'\n')
outputTxt.close()

# plt.plot_date(mplAllDates, allLts)
# plt.show()
