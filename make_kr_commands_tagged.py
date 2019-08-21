import sys

def add_cmd(command, new_command):
    if len(command) == 0:
        return new_command
    else:
        return command + ' && ' + new_command

command = ''
tag = sys.argv[1]
for i in range(len(sys.argv)-2):

    run = str(sys.argv[i+2])
    command = add_cmd(command, 'cd /Volumes/NEXT_data/IC_Data/kdst/ && python move_kdsts.py '+run)
    command = add_cmd(command, 'cd /Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/automationFiles')
    command = add_cmd(command, 'python automated_selection_tagged.py '+run+' '+tag)
    command = add_cmd(command, 'python automated_correction_tagged.py '+run+' '+tag)
    command = add_cmd(command, 'cd /Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/')
    command = add_cmd(command, 'python automated_summary_tagged.py '+run+' '+tag)
    command = add_cmd(command, 'open -a TeXshop krCalib_'+run+'_'+tag+'.tex')

print(command)
