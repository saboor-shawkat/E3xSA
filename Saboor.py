import subprocess
import sys

def install_tool(Tool-X):
    # Construct the GitHub repository URL
    repo_url = f"git clone https://github.com/ekadanuarta/Tool-X.git"

    # Clone the repository
    clone_cmd = f"git clone {repo_url}"
    subprocess.run(clone_cmd, shell=True)

    # Change into the repository directory
    repo_dir = f"{Tool-X}"
    os.chdir(repo_dir)

    # Install the tool using pip
    install_cmd = "pip install ."
    subprocess.run(install_cmd, shell=True)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: gitinstall <Tool-X>")
        sys.exit(1)

    Tool-X = sys.argv[1]
    install_tool(Tool-X)
