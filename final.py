import subprocess

program_list = ['app.py', 'subs.py']

for program in program_list:
    subprocess.call(['python', program])
    print("Finished:" + program)
