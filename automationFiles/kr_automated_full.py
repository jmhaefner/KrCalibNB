import os, os.path
import time
import subprocess
import sys

bash_check_for_file = "sshpass -p \"djshmooshmoo2323&\" ssh jhaefner@neutrinos1.ific.uv.es \'[ -d /dsafewf/ ]\'"
print('[bash]:', bash_check_for_file)
process = subprocess.Popen(bash_check_for_file, stdout=subprocess.PIPE, shell=True).wait()
if process:
    print('no')
else:
    print('yes')
