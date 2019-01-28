import nbformat
import os, os.path
import time
from nbconvert.preprocessors import ExecutePreprocessor
import subprocess
import sys
# adapted from http://tritemio.github.io/smbits/2016/01/02/execute-notebooks/

def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

# run_min = 6340
# run_max = 6526

max_time = 1200 # max seconds for a single cell

# bad_runs = [ 6519, 6518, 6514, 6507, 6476, 6405, 6404, 6402, 6401, 6400, 6399, 6398, 6397, 6396, 6393, 6363, 6343, 6586 ]

if len(sys.argv) == 2:
    min_run = int(sys.argv[1])
    max_run = min_run + 1
elif len(sys.argv) == 3:
    min_run = int(sys.argv[1])
    max_run = int(sys.argv[2])
else:
    print('Run as \"python automated_summary.py <run_no>\" or \"python automated_summary.py <run_min> <run_max>\"')
    exit()

found_runs = []
dst_directory = "/Volumes/NEXT_data/IC_Data/dst/"
dirlist = os.listdir(dst_directory)
for file_name in dirlist:
    try:
        check_number = file_name
        check_number = check_number[check_number.find('_')+1:]
        check_number = check_number[:check_number.find('_')]
        if len(check_number) == 4 and is_int(check_number):

            if int(check_number) >= min_run and int(check_number) < max_run:
                found_runs.append(check_number)
    except:
        pass

print('Total num runs =', len(found_runs))

# found_runs = [ "6337", "6338", "6339" ] # force it to just do the bad ones


for run_number in found_runs:

    print()
    run_directory = "/Volumes/NEXT_data/IC_Data/kdst/"+str(run_number)+"/"
    print('run directory =', run_directory)
    num_files_in_dir = len(os.listdir(run_directory))-1

    try:
        # Duplicate the flexible notebook
        print('Duplicating', run_number, '...')
        flex_nb_location = "/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/automationFiles/single_map_correction_TPLT.ipynb"
        flex_nb = open(flex_nb_location, "r")
        mod_contents = flex_nb.read()
        mod_contents = mod_contents.replace("<RUN_NUMBER>", str(int(run_number)))
        mod_contents = mod_contents.replace("<NUM_FILES>", str(int(num_files_in_dir)))
        flex_nb.close()

        out_nb_prefix = "/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/ltMaps/single_map_correction_"
        out_nb_location = out_nb_prefix+run_number+".ipynb"
        out_nb = open(out_nb_location, "w")
        out_nb.write(mod_contents)
        out_nb.close()

        print('New notebook:',out_nb_location)

        # Run the flexible notebook
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

    except:
        raise
        # print('Warning: run', run_number, 'could not be corrected')
