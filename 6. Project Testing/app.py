import sys
import os

demo_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "8. Project Demonstration")
sys.path.insert(0, demo_dir)

os.chdir(demo_dir)

from app import app as application

if __name__ == "__main__":
    application.run(debug=True)

app = application