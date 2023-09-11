from tools import get_cwd, askyn, srun
import os

def _check_daemon():
    if srun("colima status") != 0:
        print("docker daemon is not running, starting...")
        os.system("colima start")

def _get_port():
    port = 3000
    while port < 9901:
        if srun(f"netstat -taln | grep {port}") != 0:
            return port
        port += 100
    return 0

# Build docker image
def dbuild(file = "Dockerfile", skip = False):
    _check_daemon()
    img_name = f"-t {get_cwd()}"
    target = f"-f {os.path.join(os.getcwd(), file)}"
    if askyn("want to use cache?", skip):
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
    image = get_cwd()
    flags += f"--name {image}-instance"
    for _ in range(env_vars_length):
        var = input("env var: ").upper()
        var = var.replace(' ', '_').replace('-', '_')
        value = input(f"value of {var}: ")
        flags += f" -e {var}='{value}'"
    srun(f"docker run {flags} {image}")
    print(f"running container on http://localhost:{port}/")
    print("use 'vg dwatch' to see container's output")
    return 0

# Watch docker container output
def dwatch(skip = False):
    _check_daemon()
    image = get_cwd()
    print("press 'Ctrl+C' to quit...")
    os.system(f"docker logs --follow {image}-instance")
    return 0
