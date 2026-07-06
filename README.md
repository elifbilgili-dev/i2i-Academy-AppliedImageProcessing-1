# License Plate Detection and OCR

This project detects a car license plate from an image and reads the plate text using OCR.

## Technologies Used

- Python
- OpenCV
- EasyOCR

## Project Steps

1. Load the car image with OpenCV.
2. Convert the image to grayscale.
3. Apply Gaussian Blur to reduce noise.
4. Use Canny Edge Detection to find edges.
5. Detect contours and select the rectangular license plate area.
6. Crop the detected license plate.
7. Read the plate text using EasyOCR.

## Example Output

```text
Recognized license plate: 34BJK1903