import cv2
import easyocr


def find_license_plate(image):
    
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    edges = cv2.Canny(blurred_image, 50, 150)

    contours, _ = cv2.findContours(
        edges,
        cv2.RETR_LIST,
        cv2.CHAIN_APPROX_SIMPLE
    )

    contours = sorted(contours, key=cv2.contourArea, reverse=True)

    for contour in contours:
        perimeter = cv2.arcLength(contour, True)
        corners = cv2.approxPolyDP(contour, 0.02 * perimeter, True)

       
        if len(corners) == 4:
            x, y, width, height = cv2.boundingRect(corners)
            plate_image = image[y:y + height, x:x + width]

            return plate_image, corners

    return None, None


image_path = "images/car.png"
image = cv2.imread(image_path)

if image is None:
    raise FileNotFoundError("Image not found. Please check the file path.")

plate_image, plate_contour = find_license_plate(image)

if plate_image is None:
    raise ValueError("License plate area not found.")

reader = easyocr.Reader(["en"], gpu=False)

ocr_result = reader.readtext(
    plate_image,
    detail=0,
    allowlist="0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
)

recognized_plate = "".join(ocr_result)

print("Recognized license plate:", recognized_plate)

result_image = image.copy()
cv2.drawContours(result_image, [plate_contour], -1, (0, 255, 0), 3)

cv2.imshow("Detected Plate Area", result_image)
cv2.imshow("Cropped Plate", plate_image)

cv2.waitKey(0)
cv2.destroyAllWindows()