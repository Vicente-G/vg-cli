import os
from git import git_add, git_branch, git_commit, git_download, git_upload
from github import gh_make_pr
from colima import dstart, dstop
from docker import dbuild, drun, dwatch

from tools import srun
from config import add_template
from template import gh_init
from argparse import RawTextHelpFormatter, ArgumentParser

FUNCTIONS = {
    "new": add_template,
    "init": gh_init,
    "add": git_add,
    "commit": git_commit,
    "branch": git_branch,
    "download": git_download,
    "upload": git_upload,
    "pr": gh_make_pr,
    "dstart": dstart,
    "dstop": dstop,
    "dbuild": dbuild,
    "drun": drun,
    "dwatch": dwatch
}

description = """A CLI with Vicente-G's day-to-day functions

new       \tconfigurate a new template for the init command
init      \tcreate a new private GitHub repository from a template
pr        \tcreate a new pull request with a guided interface
add       \tadd any files to this repo or all of them with a dot
branch    \tcreate and/or switch to a branch in this repo
commit    \tmake a commit with a guided interface into this repo
download  \tclone a repo with a given URL or pull from origin
upload    \tset origin to a given URL or push from this repo
dstart    \tstart the docker daemon with colima by default
dstop     \tstop the daemon, removing null images and containers
dbuild    \tbuild an image from a specified file and this repo
drun      \trun a container from the built image using N env vars
dwatch    \twatch the logs of the running container on this repo
"""

parser = ArgumentParser(
    prog="vg", 
    description=description,
    formatter_class=RawTextHelpFormatter
)
vfile = open("/usr/local/lib/vg/VERSION", "r")
parser.version = vfile.read()
vfile.close()

parser.add_argument(
    "command",
    metavar="<command>",
    choices=FUNCTIONS.keys(),
    help="choose any of the commands from above"
)
parser.add_argument("-v", "--version", action="version")
parser.add_argument("-y", action="store_true", help="skip all confirmation prompts")
args, unknown = parser.parse_known_args()

try:
    if FUNCTIONS[args.command](*unknown, skip = args.y) != 0:
        exit(1)
    url = "https://raw.githubusercontent.com/Vicente-G/vg-cli/main/VERSION"
    if srun(f"curl -fsL {url}") != 0:
        print("Version looking failed, please check your internet connection")
        exit(0)
    condition = f"$(curl -fsL {url}) != {parser.version}"
    msg = "A new version of the CLI is available, run \\\"vg upgrade\\\" to install it!"
    exit(os.system(f"if [[ {condition} ]] ; then echo \"{msg}\" ; fi"))
except KeyboardInterrupt:
    print("\nvg: error: operation cancelled by user")
    exit(1)
