# In wsgi.py or at the top of your main app.py file if it's the entry point
import sys
from app import (
    app as application,
)

# Add your project directory to the sys.path
# Replace 'your_username' and 'your_project_name' with actual values
path = "/home/userarpit/app"
if path not in sys.path:
    sys.path.append(path)

