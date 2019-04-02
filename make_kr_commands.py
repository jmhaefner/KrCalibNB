import sys

def add_cmd(command, new_command):
    if len(command) == 0:
        return new_command
    else:
        return command + ' && ' + new_command

command = ''
for i in range(len(sys.argv)-1):

    run = str(sys.argv[i+1])
    command = add_cmd(command, 'cd /Volumes/NEXT_data/IC_Data/kdst/ && python move_kdsts.py '+run)
    command = add_cmd(command, 'cd /Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/automationFiles')
    command = add_cmd(command, 'python automated_selection.py '+run)
    command = add_cmd(command, 'python automated_correction.py '+run)
    command = add_cmd(command, 'cd /Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/')
    command = add_cmd(command, 'python automated_summary.py '+run)
    command = add_cmd(command, 'open -a TeXshop krCalib_'+run+'.tex')

print(command)
