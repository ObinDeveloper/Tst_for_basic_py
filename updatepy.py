import subprocess  # Import the subprocess module to run system commands from Python.

# Function to get the installed Python version
def get_installed_python_version():
    # Runs the 'python3 --version' command to get the installed Python version.
    result = subprocess.run(["python3", "--version"], capture_output=True, text=True)
    # The result is returned as a string, we extract the version number (last part of the output).
    return result.stdout.strip().split()[-1]

# Function to check for updates via Homebrew
def check_for_updates():
    # First, run 'brew update' to update Homebrew itself.
    subprocess.run(["brew", "update"])
    # Then, run 'brew upgrade python' to upgrade Python to the latest version available.
    subprocess.run(["brew", "upgrade", "python"])

# Get and store the installed Python version.
installed_version = get_installed_python_version()

# Print the current installed version.
print(f"Installed Python version: {installed_version}")

# Print a message indicating that the update process is being started.
print("Checking for updates...")

# Call the function to update Python using Homebrew.
check_for_updates()

# After updating, get the new installed Python version.
new_version = get_installed_python_version()

# Print the updated version of Python (which could be the same if Python was already up to date).
print(f"Updated Python version: {new_version}")
