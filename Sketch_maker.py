import cv2
import numpy as np
from pathlib import Path

# Path to the image file
image_path = Path('C:/Users/Lenovo/OneDrive/java-script/selfmade/sketch_maker/Iron_Man.jpeg')
output_path = image_path.with_name(f'{image_path.stem}_sketch.jpeg')

# Read the original image
image = cv2.imread(str(image_path))
if image is None:
    print(f"Error: Unable to read the image file '{image_path}'. Please check the file path and try again.")
    raise SystemExit(1)

# Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Invert the grayscale image
inverted_image = cv2.bitwise_not(gray_image)

# Blur the inverted image for dodge blend
blurred_image = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)

# Dodge blend to create pencil sketch
def dodge(front, back):
    return cv2.divide(front, 255 - back, scale=256)

sketch = dodge(gray_image, blurred_image)

# Enhance edges using Canny edge detector
edges = cv2.Canny(gray_image, threshold1=50, threshold2=150)

# Invert edges (to highlight as black lines on white background)
edges_inv = cv2.bitwise_not(edges)

# Combine edges with sketch by bitwise AND (emphasizes edges)
sketch_with_edges = cv2.bitwise_and(sketch, edges_inv)

# Sharpen the combined sketch to mimic pencil strokes
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
sharpened_sketch = cv2.filter2D(sketch_with_edges, -1, kernel)

# Animate sketch generation line by line
height, width = sharpened_sketch.shape
animated_sketch = np.ones((height, width), dtype=np.uint8) * 255  # Start with white canvas
window_name = "Hand-Drawn Pencil Sketch with Edges"
cv2.namedWindow(window_name, cv2.WINDOW_NORMAL)
cv2.resizeWindow(window_name, 800, 600)

for y in range(height):
    animated_sketch[y, :] = sharpened_sketch[y, :]
    cv2.imshow(window_name, animated_sketch)
    if cv2.waitKey(10) & 0xFF == 27:  # Press ESC to exit early
        break

if not cv2.imwrite(str(output_path), sharpened_sketch):
    raise IOError(f"Unable to save the sketch to '{output_path}'. Check the folder permissions.")

print(f"Hand-drawn style pencil sketch with visible edges saved as '{output_path}'.")

cv2.waitKey(0)
cv2.destroyAllWindows()
