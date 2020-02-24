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
for i in range(len(sys.argv)-1):

    run = str(sys.argv[i+1])
    command = add_cmd(command, 'python move_kdsts.py '+run, new_section = True)

print(command)
