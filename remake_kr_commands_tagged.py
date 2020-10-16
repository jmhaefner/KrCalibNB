import sys
import os

select = True
correct = True
summarize = True
alt_input = False
alt_input_tag = 'st190819'

def add_cmd(command, new_command, new_section = False):
    if len(command) == 0:
        return new_command
    else:
        if new_section:
            return command + '; ' + new_command
        else:
            return command + ' && ' + new_command

if not select or not correct or not summarize:
    print('WARNING: NOT ALL FUNCTIONS WILL BE PERFORMED')
    if select:
        print('SELECTING.')
    if correct:
        print('CORRECTING.')
    if summarize:
        print('SUMMARIZING.')

command = ''
tag = sys.argv[1]
for i in range(len(sys.argv)-2):
    run = str(sys.argv[i+2])
    if correct or select:
        command = add_cmd(command, 'cd /Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/automationFiles', new_section = True)
    if select or correct:
        command = add_cmd(command, 'python auto_selcor.py '+run+' '+tag)
    if summarize:
        command = add_cmd(command, 'cd /Users/jmhaefner/Development/KryptonCalibration/KrCalibNB_JMH/KrCalibNB/doc/')
        command = add_cmd(command, 'python automated_summary_tagged.py '+run+' '+tag)
        command = add_cmd(command, 'open -a TeXshop krCalib_'+run+'_'+tag+'.tex')

print(command)
