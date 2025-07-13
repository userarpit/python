import os
import sys
PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
sys.path.append(PROJECT_ROOT)

print(sys.path)
import utils
print(utils.get_length("Hello"))
utils.yolo(10)
print(os.path.dirname(__file__))
print(PROJECT_ROOT)