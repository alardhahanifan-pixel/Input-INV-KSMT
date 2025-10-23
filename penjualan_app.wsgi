#!/usr/bin/python3
"""
WSGI file untuk menjalankan aplikasi dengan Apache mod_wsgi
"""

import sys
import os

# Add the project directory to the Python path
sys.path.insert(0, '/workspace')

# Set the application directory
os.chdir('/workspace')

# Import the application
from app import app as application

if __name__ == "__main__":
    application.run()