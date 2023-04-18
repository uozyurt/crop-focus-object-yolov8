# crop-focus-object-yolov8
This project is useful only for pre-trained yolov8 weights. It requires a weights file ("xxx.pt") and images to crop.

"crop_focus_object_driver.py" file is an example for using the crop function. You need to declare the paths of images and weight.pt file.

"choose_one_bbox.py" has a function which decides the bounding box which is most likely to be the focus object bbox in case of multiple detections.

Requirements that have to be installed:

ultralytics,
cv2,
os,
imageio,
pytorch,
time
