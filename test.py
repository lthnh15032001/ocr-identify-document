from core.read_id_card import bytes_to_information_id_card
import cv2


image = cv2.imread('2.jpg')
success, encoded_image = cv2.imencode('.jpg', image)
print(encoded_image.toBytes())
