# objective : This projects is POC for Object Detections by using openCV on mobileNet SSD model

# before starting :
## 1. set up environment with venv

# macOS/ Linux
# Create a virtual environment named "venv"
python3 -m venv venv
# Activate the virtual environment
source venv/bin/activate

# window
# Create a virtual environment named "venv"
python -m venv venv
# Activate the virtual environment
venv\Scripts\activate

## 2. Install requirements.txt file
# install library
pip3 install requirements.txt

## 3. Check Camera that available
    python3 check_camera_no.py
 # set camera available number on 
    cap = cv2.VideoCapture(>setting_number_here!!<)

## after prepare venv for projects
# 4. run object_dectection.py file
python3 object_detection.py