from tools import getch
import os

def _get_cwd():
    complete = os.getcwd()
    return complete.split('/')[-1]

def _check_daemon():
    status = os.system("colima status &> /dev/null")
    if status != 0:
        print("docker daemon is not running, starting...")
        os.system("colima start")

def _get_port():
    port = 3000
    while port < 9901:
        status = os.system(f"netstat -taln | grep {port} &> /dev/null")
        if status != 0:
            return port
        port += 100
    return 0

# Build docker image
def dbuild(file = "Dockerfile", skip = False):
    _check_daemon()
    img_name = f"-t {_get_cwd()}"
    target = f"-f {os.path.join(os.getcwd(), file)}"
    if not skip:
        print(f"want to use cache? (y/n) ")
    if skip or getch() == 'y':
        os.system(f"docker build {target} {img_name} .")
    else:
        os.system(f"docker build --no-cache {target} {img_name} .")
    return 0

# Run docker container from image
def drun(env_vars_length = 0, skip = False):
    _check_daemon()
    port = _get_port()
    if not port:
        print("vg: error: no available port (3000-9900)")
        return 1
    flags = f"-d -t -p {port}:8080 -e PORT='8080' "
    image = _get_cwd()
    flags += f"--name {image}-instance"
    for _ in range(env_vars_length):
        var = input("env var: ").upper()
        var = var.replace(' ', '_').replace('-', '_')
        value = input(f"value of {var}: ")
        flags += f" -e {var}='{value}'"
    os.system(f"docker run {flags} {image} &> /dev/null")
    print(f"container on localhost:{port}/, use 'vg dwatch' to see output")
    return 0

# Watch docker container output
def dwatch(skip = False):
    _check_daemon()
    image = _get_cwd()
    print("press 'Ctrl+C' to quit...")
    os.system(f"docker logs --follow {image}-instance")
    return 0
