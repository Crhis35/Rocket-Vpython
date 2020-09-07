# Rocket-Vpython
Crhistian Caraballo

## Linux Distribution setup
> Delete line 62 from requirements pywin32.
- If your virtual environment is activated, then run this command to freeze the requirements to a file that you can access later: pip freeze > requirements.txt
- If your virtual environment is activated, then deactivate it using: deactivate
- Delete your virtualenv folder.
- Install python-tk using: sudo apt-get install python-tk
- Recreate your virtualenv using: virtualenv > nameofyourenv --system-site-packages
- Next, activate your virtualenv: source <virtual environment folder>/bin/activate
- Restore all your packages that you froze earlier from the requirements.txt file: pip install -r > path to requirements.txt file
