from tools import srun, askyn
import os

# Start colima for docker daemon
def dstart(skip = False):
    if srun("colima status") != 0:
        os.system("colima start")
    else:
        question = "Colima is already running, wanna restart?"
        if askyn(question, skip):
            os.system("colima restart")
    return 0

# Stop colima and stop every container
def dstop(skip = False):
    if srun("colima status") != 0:
        print("docker daemon was already stopped")
        return 1
    print("shutting down every container... ", end = "")
    srun("docker stop $(docker ps -q)")
    print("[SUCCESS]\ncleaning up... ", end = "")
    srun("docker rm $(docker ps -q)")
    srun("docker rmi $(docker images -q -f \"dangling=true\")")
    print("[SUCCESS]")
    os.system("colima stop")
    return 0
