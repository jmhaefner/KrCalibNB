import os, os.path
import time
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
import subprocess
import sys
# adapted from http://tritemio.github.io/smbits/2016/01/02/execute-notebooks/

reduce_bin_number = False

if len(sys.argv) == 2:
    run_min = int(sys.argv[1])
    run_max = run_min + 1
elif len(sys.argv) == 3:
    if int(sys.argv[2]) == 1:
        run_min = int(sys.argv[1])
        run_max = run_min + 1
        reduce_bin_number = True
        print('SELECTING WITH REDUCED BIN NUMBER')
    else:
        run_min = int(sys.argv[1])
        run_max = int(sys.argv[2])
else:
    print('Run as \"python automated_summary.py <run_no>\" or \"python automated_summary.py <run_min> <run_max>\"')
    exit()

max_time = 1200 # max seconds for a single cell

low_stat_runs = [ 6519, 6402, 6401, 6400, 6343 ] # fail at bin size 50 but do ok at smaller
crit_low_runs = [ 6518, 6514, 6507, 6476, 6405, 6404, 6399, 6398, 6397, 6396, 6393, 6363, 6586 ] # too low to ever work
bad_runs = [ 6519, 6518, 6514, 6507, 6476, 6405, 6404, 6402, 6401, 6400, 6399, 6398, 6397, 6396, 6393, 6363, 6343 ] # fail at bin size 50

for run_number in range(run_min, run_max):

    print()
    run_directory = "/Volumes/NEXT_data/IC_Data/kdst/"+str(run_number)+"/"
    num_files_in_dir = len(os.listdir(run_directory))-1
    # force the program to reduce the bin number by lying about how many files are in the directory
    if reduce_bin_number:
        num_files_in_dir = 5000

    #if not run_number in bad_runs:
    #    print('SKIPPING', run_number)
    #    continue

    try:
        print('Looking at data in', run_directory)
        dirlist = os.listdir(run_directory)
        last_file_number = -1
        last_file = ""
        for file_name in dirlist:
            check_number = file_name
            check_number = check_number[check_number.find('_')+1:]
            check_number = check_number[:check_number.find('_')]
            try:
                if int(check_number) > last_file_number:
                    last_file_number = int(check_number)
                    last_file = check_number
            except:
                pass

        print('Max file number =', last_file)

        end_tags = dirlist[-1][-23:-3]

        # Make a duplicate of the flexible notebook
        print('Duplicating', run_number, '...')
        flex_nb_location = "/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/automationFiles/kr_selection_and_filter_TPLT.ipynb"

        flex_nb = open(flex_nb_location, "r")
        mod_contents = flex_nb.read()
        mod_contents = mod_contents.replace("<RUN_PARAMS>", "run = "+str(int(run_number)))
        mod_contents = mod_contents.replace("<RUN_NUMBER>", str(int(run_number)))
        mod_contents = mod_contents.replace("<LAST_FILE>", str(int(last_file)))
        mod_contents = mod_contents.replace("<NUM_FILES>", str(int(num_files_in_dir)))
        mod_contents = mod_contents.replace("<END_TAGS>", end_tags)
        flex_nb.close()

        # make the output folder for the summary
        try:
            summary_directory = "/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/img/r"+str(run_number)+"/"
            bash_mkdir = "mkdir " + summary_directory
            print('[bash]:', bash_mkdir)
            process = subprocess.Popen(bash_mkdir, stdout=subprocess.PIPE, shell=True).wait()
        except:
            print('New folder not made; already exists')

        out_nb_prefix = "/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/krSelectionAndFilter/kr_selection_and_filter_"
        out_nb_location = out_nb_prefix+str(run_number)+".ipynb"
        out_nb = open(out_nb_location, "w")
        out_nb.write(mod_contents)
        out_nb.close()

        print('New notebook:',out_nb_location)

        t0 = time.time()
        write_notebook = out_nb_location
        print('Calculating notebook  ', out_nb_location)
        print('Outputting to         ', write_notebook)
        nb = nbformat.read(open(out_nb_location), as_version=4)
        ep = ExecutePreprocessor(timeout=max_time, kernel_name='python3')
        ep.preprocess(nb, {'metadata': {'.': './'}})
        nbformat.write(nb, open(write_notebook, mode='wt'))
        dt = time.time() - t0
        print('Running time:', round(dt/60.0,1), 'm')

    except (KeyboardInterrupt, SystemExit):
        raise

    except Exception as e:
        print(e)
        print('run', str(run_number), 'could not be analyzed')
