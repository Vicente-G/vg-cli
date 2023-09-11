from pyautogui import write
import os
import sys
import tty
import termios

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def rlinput(prompt, prefill=''):
    print(prompt, end='', flush=True)
    write(prefill)
    return input()

def askyn(prompt, skip = False):
    if not skip:
        print(f"{prompt} (y/n) ")
    return skip or getch() == 'y'

def srun(command):
    return os.system(f"{command} &> /dev/null")

def get_cwd():
    complete = os.getcwd()
    return complete.split('/')[-1].lower()

def get_one_line(file, clean = True):
    result = ""
    with open(file, "r") as file:
        result = file.read().replace("\n", "").replace("\r", "")
    if clean:
        os.system(f"rm {file}")
    return result
