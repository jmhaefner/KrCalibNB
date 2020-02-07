import sys

def add_cmd(command, new_command, new_section = False):
    if len(command) == 0:
        return new_command
    else:
        if new_section:
            return command + '; ' + new_command
        else:
            return command + ' && ' + new_command

command = 'cd /Volumes/NEXT_data/IC_Data/kdst/'
tag = sys.argv[1]
for i in range(len(sys.argv)-2):

    run = str(sys.argv[i+2])
    command = add_cmd(command, 'python move_kdsts.py '+run, new_section = True)

print(command)
