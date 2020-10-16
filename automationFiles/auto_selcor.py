import os, os.path
import time
from nbconvert.preprocessors import ExecutePreprocessor
import nbformat
import subprocess
import sys
# adapted from http://tritemio.github.io/smbits/2016/01/02/execute-notebooks/

run_number = int(sys.argv[1])
tag = sys.argv[2]

max_time = 4800 # max seconds for a single cell. 1200 = 20 m


print()
run_directory = "/Volumes/NEXT_data/IC_Data/kdst/"+str(run_number)+"/"
num_files_in_dir = len(os.listdir(run_directory))-1

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

    # Make a duplicate of the flexible notebook
    print('Duplicating', run_number, '...')
    flex_nb_location = "/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/automationFiles/kr_selfilcor_"+tag+"_TPLT.ipynb"

    flex_nb = open(flex_nb_location, "r")
    mod_contents = flex_nb.read()
    mod_contents = mod_contents.replace("<RUN_NUMBER>", str(int(run_number)))
    mod_contents = mod_contents.replace("<NUM_FILES>", str(int(num_files_in_dir)))
    mod_contents = mod_contents.replace("<ANALYSIS_TAG>", tag)
    flex_nb.close()

    out_nb_prefix = "/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/krSelectionAndFilter/kr_selfilcor_"
    out_nb_location = out_nb_prefix+str(run_number)+"_"+tag+".ipynb"
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
