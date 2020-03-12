"""
In this exercise, you'll be playing around with the sys module,
which allows you to access many system specific variables and
methods, and the os module, which gives you access to lower-
level operating system functionality.
"""

import sys
import os

# See docs for the sys module: https://docs.python.org/3.7/library/sys.html

# Print out the command line arguments in sys.argv, one per line:
# YOUR CODE HERE
print("Program: ", sys.argv[0])
for arg in sys.argv:
    print(arg)

# Print out the OS platform you're using:
# YOUR CODE HERE
print("OS Platform: ", sys.platform)

# Print out the version of Python you're using:
# YOUR CODE HERE
# Python version 2.0
major = sys.version_info.major
minor = sys.version_info.minor
micro = sys.version_info.micro

print(f"Python version: version {major}.{minor}.{micro}")

# See the docs for the OS module: https://docs.python.org/3.7/library/os.html

# Print the current process ID
# YOUR CODE HERE
pid = os.getpid()
print(f"Current process ID: {pid}")

# Print the current working directory (cwd):
# YOUR CODE HERE
print("Current working directory: " + os.getcwd())

# Print out your machine's login name
# YOUR CODE HERE
print("logged in as " + os.getlogin())
