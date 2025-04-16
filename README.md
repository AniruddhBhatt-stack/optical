Text Detection with EasyOCR and OpenCV
This project uses EasyOCR to detect text from images and OpenCV to visualize the results. It reads an image (doouble.png), detects text regions, and overlays bounding boxes and recognized text on the image. The result is displayed using matplotlib.

Features
Optical Character Recognition using EasyOCR

Text annotation using OpenCV

Image display with matplotlib

Lightweight and GPU optional

Requirements
Python 3.x

EasyOCR

OpenCV

Matplotlib

NumPy

Install dependencies using:

bash
Copy
Edit
pip install easyocr opencv-python matplotlib numpy
Usage
Place your target image in the project directory and name it doouble.png or change the filename in the script.

Run the Python script:

bash
Copy
Edit
python your_script_name.py
Extracted text will be printed in the console and the annotated image will be displayed.

Example Output
Recognized text printed to the console

Image with green boxes around detected text and labels overlaid
