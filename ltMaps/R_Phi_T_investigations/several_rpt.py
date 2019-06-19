# all_runs = [7116, 7115, 7114, 7113, 7112, 7108, 7107, 7106, 7105]
all_runs = [1111]

print('Runs =', all_runs)

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

reduce_bin_number = False

for run_number in all_runs:
    print('')
    try:
        # Duplicate the flexible notebook
        print('Duplicating', run_number, '...')
        flex_nb_location = "/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/ltMaps/R_Phi_T_investigations/single_map_correction_7005_RPhiT.ipynb"
        flex_nb = open(flex_nb_location, "r")
        mod_contents = flex_nb.read()
        mod_contents = mod_contents.replace("7005", str(int(run_number)))
        flex_nb.close()

        out_nb_location = "/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/ltMaps/R_Phi_T_investigations/single_map_correction_"+str(run_number)+"_RPhiT.ipynb"
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
