import cv2
events = [i for i in dir(cv2) if 'EVENts' in i]
print events
