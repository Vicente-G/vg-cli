from tools import getch
import os

# Start colima for docker daemon
def dstart(skip = False):
    status = os.system("colima status &> /dev/null")
    if status != 0:
        os.system("colima start")
    else:
        if not skip:
            print("Colima is already running, wanna restart? (y/n) ")
        if skip or getch() == 'y':
            os.system("colima restart")
    return 0

# Stop colima and stop every container
def dstop(skip = False):
    status = os.system("colima status &> /dev/null")
    if status != 0:
        print("docker daemon was already stopped")
        return 1
    print("shutting down every container...")
    os.system("docker stop $(docker ps -q)")
    print("cleaning up...")
    os.system("docker rm $(docker ps -q)")
    os.system("docker rmi $(docker images -q -f \"dangling=true\")")
    os.system("colima stop")
    return 0
