"""CSC108: Software Setup

Instructions (READ THIS FIRST!)
===============================

This file will only run correctly if you are using Python 3. You should run this
file by clicking the "Play" button (green triangle) toward the top of Wing 101.

Copyright and Usage Information
===============================

This file is provided solely for the personal and private use of students
taking CSC108 at the University of Toronto St. George campus. All forms of
distribution of this code, whether as given or with any changes, are
expressly prohibited.

This file is Copyright (c) 2026 by the University of Toronto CSC108 instructors.
"""
import sys
import subprocess
import importlib

requirements = ['pytest', 'python-ta']
all_set = True

name = input('Hello! What is your name? ')
print('Hi ' + name + '!')

if not (sys.version_info.major == 3 and sys.version_info.minor == 13):
    print('You are not using Python 3.13 in Wing 101. Please refer back to '
          'the instructions or ask for help in office hours or Piazza.')
    all_set = False
else:
    print('Looks like you are using Python 3.13! '
          'Next, we will check for the required packages.')


def ensure_pip() -> None:
    executables = [f'python{sys.version_info.major}.{sys.version_info.minor}',
                   sys.executable,
                   'py']
    pip_check = '-m ensurepip --upgrade'

    for executable in executables:
        print(".", end='')
        try:
            subprocess.run(executable + ' ' + pip_check,
                             shell=True,
                             stdout=subprocess.DEVNULL,
                             stderr=subprocess.DEVNULL)
        except:
            pass


def attempt_package_installation(package: str) -> None:
    """Attempt installation of <package>.
    """
    executables = [f'python{sys.version_info.major}.{sys.version_info.minor}',
                   sys.executable,
                   'py']

    attempts = [f'-m pip install {package}',
                # Turn off SSL verification (certificate errors)
                f'-m pip install {package} '
                f'config --global http.sslVerify false',
                # Set pypi as a trusted host
                f'-m pip install {package} '
                f'--trusted-host pypi.python.org'
                ]

    for i in range(len(attempts) * len(executables)):
        print(".", end='')
        try:
            # Switch between python and sys.executable
            executable = executables[i % len(executables)]
            attempt = attempts[i // len(executables)]

            # sys.executable uses check_call
            if executable != executables[1]:
                subprocess.run(executable + ' ' + attempt,
                                 shell=True,
                                 stdout=subprocess.DEVNULL,
                                 stderr=subprocess.DEVNULL)
            else:
                subprocess.check_call([executable] + attempt.split(),
                                      stderr=subprocess.DEVNULL,
                                      stdout=subprocess.DEVNULL)
        except:
            pass


try:
    import pip
except:
    print("We are now trying to ensure that we can download packages by installing "
          "'pip' for you. This requires a stable internet connection.", end='')
    ensure_pip()

for requirement in requirements:
    try:
        importlib.import_module(requirement.replace("-", "_"))
    except:
        print(f"We are now trying to install the package '{requirement}' "
              f"for you. This requires a stable internet connection.", end='')
        attempt_package_installation(requirement)
        print("\nPlease try to re-run setup.py to see if the packages "
              "were successfully installed.")
        all_set = False
    else:
        print(f"The package {requirement} is already successfully installed.")

if all_set:
    print("You're all set! Have fun in CSC108!")
else:
    print("It seems like something was not set up properly. Please try to "
          "re-run setup.py to see if the problems are resolved.")
    print("If you've already tried to re-run setup.py, please refer back to "
          "the instructions or ask for help in office hours or Piazza. ")
