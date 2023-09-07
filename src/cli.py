from git import git_add, git_branch, git_commit, git_download, git_upload
from config import add_template
from github import gh_make_pr
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
    "pr": gh_make_pr
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
"""

parser = ArgumentParser(
    prog="vg", 
    description=description,
    formatter_class=RawTextHelpFormatter
)
parser.version = "1.1.0"

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
    status = FUNCTIONS[args.command](*unknown, skip = args.y)
    exit(status)
except KeyboardInterrupt:
    print("\nvg: error: operation cancelled by user")
    exit(1)
