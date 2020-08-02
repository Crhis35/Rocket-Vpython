# Cohete-Vpython
Chistian Caraballo

## Linux Distribution setup
> delete line 62 from requirements pywin32
- if your virtual environment is activated, then run this command to freeze the requirements to a file that you can access later: pip freeze > requirements.txt
- if your virtual environment is activated, then deactivate it using: deactivate
- delete your virtualenv folder.
- install python-tk using: sudo apt-get install python-tk
- recreate your virtualenv using: virtualenv <nameofyourenv> --system-site-packages
- next, activate your virtualenv: source <virtual environment folder>/bin/activate
- restore all your packages that you froze earlier from the requirements.txt file: pip install -r <path to requirements.txt file>
