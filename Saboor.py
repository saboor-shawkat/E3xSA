import subprocess
import sys

def install_tool(tool_name):
    # Construct the GitHub repository URL
    repo_url = f"https://github.com/{tool_name}/{tool_name}.git"

    # Clone the repository
    clone_cmd = f"git clone {repo_url}"
    subprocess.run(clone_cmd, shell=True)

    # Change into the repository directory
    repo_dir = f"{tool_name}"
    os.chdir(repo_dir)

    # Install the tool using pip
    install_cmd = "pip install ."
    subprocess.run(install_cmd, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: gitinstall <tool_name>")
        sys.exit(1)

    tool_name = sys.argv[1]
    install_tool(tool_name)
