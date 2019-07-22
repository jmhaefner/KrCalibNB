import sys
import os

def add_cmd(command, new_command):
    if len(command) == 0:
        return new_command
    else:
        return command + ' && ' + new_command

if len(sys.argv) > 2:
    command = ''
    for i in range(len(sys.argv)-1):
        run = str(sys.argv[i+1])
        command = add_cmd(command, 'cd /Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/automationFiles')
        command = add_cmd(command, 'python automated_selection.py '+run)
        command = add_cmd(command, 'python automated_correction.py '+run)
        command = add_cmd(command, 'cd /Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/')
        command = add_cmd(command, 'python automated_summary.py '+run)
        command = add_cmd(command, 'open -a TeXshop krCalib_'+run+'.tex')
else:
    run_min = 7216
    run_max = 7280

    command = ''
    for my_run in range(run_min, run_max):
        run = str(my_run)
        test_file = '/Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/ltMaps/single_map_correction_'+str(run)+'.ipynb'
        exists = os.path.isfile(test_file)
        if exists:
            command = add_cmd(command, 'cd /Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/automationFiles')
            # command = add_cmd(command, 'python automated_selection.py '+run)
            command = add_cmd(command, 'python automated_correction.py '+run)
            command = add_cmd(command, 'cd /Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/')
            command = add_cmd(command, 'python automated_summary.py '+run)
            command = add_cmd(command, 'open -a TeXshop krCalib_'+run+'.tex')



print(command)
