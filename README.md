# 🎨 Computational Pencil Sketch & Edge Detector

An automated Computer Vision pipeline built with Python, OpenCV, and NumPy that transforms standard digital photographs into high-fidelity, hand-drawn pencil sketches. The system combines classical image processing operations with advanced edge extraction to retain intricate structural details.

# 🚀 Key Features

* Dynamic Grayscale & Color Inversion: Prepares image luminance maps for structural profiling.
* Gaussian Blurring: Isolates ambient frequencies to simulate graphite shading variations.
* Mathematical Dodging & Blending: Utilizes pixel-wise division to dynamically merge contrast maps and draw out pencil strokes.
* Canny Edge Integration: Overlays structural wireframes to ensure outlines remain crisp and distinct.
* Live Procedural Rendering: Generates the artistic rendering progressively on screen.

# VISUAL TRANSFORMATION PIPELINE

 * **Source Image Loading:** Imports the raw BGR color channel image from the local path.
 * **Grayscale Conversion:** Strips the color data to isolate the foundational luminance and contrast maps.
 * **Inversion & Gaussian Blur:** Inverts the image values and applies a smoothing filter to isolate ambient shading frequencies.
 * **Mathematical Dodging:** Performs pixel-wise division between the grayscale and blurred layers to simulate light graphite       strokes.
 * **Canny Edge Blending:** Overlays a structural wireframe map to sharpen fine lines, producing the final high-fidelity pencil    sketch.

## 🛠️ Technical Stack & Dependencies

 * Core Language: Python 3.x
 * Computer Vision framework: OpenCV (opencv-python)
 * Numerical Processing: NumPy

# 💻 Installation & Setup

 1.Clone the repository:
   * git clone https://github.com
   * cd image-to-sketch-opencv
     
2.Set up a virtual environment (Recommended):
  * bashpython -m venv venv
  * source venv/bin/activate 

3.Install dependencies:
  * bashpip install -r requirements.txt

# 🏃‍♂️ How to Run
  
  1. Place your target image inside the project directory
     
  2. Update the image_path variable in the script or execute via terminal:
      * python sketch_maker.py
   
  3.The program will display the image rendering process step-by-step and automatically export a high resolution jpeg or jpg or       png image in your folder.

# 📜 License
 * Distributed under the MIT License. See LICENSE for more information.</CreativeWritingPad>
 













  










