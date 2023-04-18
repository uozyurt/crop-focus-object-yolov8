import os
import cv2
from ultralytics import YOLO
from imageio import imwrite
from choose_one_bbox import choose_bbox
import time
import torch

def crop_focus_object(IMAGES_PATH: str,
                      WEIGHTS_PATH: str,
                      EXPAND_RATIO: float = 0.00,
                      save:bool = False,
                      OUTPUT_PATH:str ="",
                      conf:float=0.5):
    
    '''
    This function gets a path to source images and a pre-trained yolov8 weights, then return a list of numpy arrays which represents the cropped images.
    
    IMAGES_PATH: A string for the path of source images.
    
    WEIGHTS_PATH: A string for the path of pre-trained yolov8 weights.
    
    EXPAND_RATIO: A float number between 0 and 1 for the cropped images to be cropped with a increased size at each side. example -> 0.025 for a %2.5 increase at each side.
    
    save: If set to True, saves the cropped images in OUTPUT_PATH.
    
    OUTPUT_PATH: A string for the path of output images to be saved.
    
    conf: A float number between 0 and 1 which represents the minimum confidence threshold for a bbox to be considered.
    
    '''
    #Record the start time
    t1 = time.time()
    
    #Set cuda if available for GPU utilization
    device = 0 if torch.cuda.is_available() else "cpu"

    #Load the yolov8 model
    model = YOLO(WEIGHTS_PATH)

    #Get the prediction results
    results = model.predict(source=IMAGES_PATH, conf=conf, device=device, imgsz = 640)

    #Create a list to return
    output_images = []
    
    #Get used weights' name
    weights_name = WEIGHTS_PATH[:-3]

    #If save is True and output folder doesn't exists, create one.
    if save and (not OUTPUT_PATH):
        OUTPUT_PATH =  IMAGES_PATH.split("/")[-1] + "__" + weights_name + "__output"
        if not os.path.exists(OUTPUT_PATH):
            os.mkdir(OUTPUT_PATH)

    #Iterate each result
    for result in results:
        
        #Extract the image name
        image_name = result.path.split("\\")[-1]
        
        #Get the bbox coordinates in xyxy format
        bbox = result.boxes.xyxy
        
        #Get the current original images height and width
        h, w, c = result.orig_img.shape

        #Choose the most desired bbox in case there are multiple detections
        bbox_x1, bbox_y1, bbox_x2, bbox_y2 = choose_bbox(bbox,
                                                        image_size=(w,h),
                                                        center_coordinates=(0.5,0.5),
                                                        input_xyxy=True,
                                                        input_normalized=False,
                                                        return_xyxy=True,
                                                        AREA_RATIO_THRESHOLD=0.8
                                                        )
        
        #Check if there exists a valid detected bbox
        if((bbox_x1, bbox_y1, bbox_x2, bbox_y2) == (-1,-1,-1,-1)):
            continue
        
        #Get the width and height for image to be cropped
        cropped_image_w = bbox_x2 - bbox_x1
        cropped_image_h = bbox_y2 - bbox_y1
        
        #Calculate the cropped images coordinated regarding the EXPAND_RATIO
        left = int(max(bbox_x1-EXPAND_RATIO*cropped_image_w, 0))
        top = int(max(bbox_y1-EXPAND_RATIO*cropped_image_h, 0))
        right = int(min(bbox_x2+EXPAND_RATIO*cropped_image_w, w))
        bottom = int(min(bbox_y2+EXPAND_RATIO*cropped_image_h, h))
        
        #Obtain the cropped image
        output_image = cv2.cvtColor(result.orig_img[top:bottom, left:right], cv2.COLOR_BGR2RGB)
        

        
        #Check if save option is True
        if save: 
            
            #Get the save path
            save_name = os.path.join(OUTPUT_PATH, image_name)
            
            #Save the cropped image
            imwrite(save_name, output_image)
            
        
        #Append the output image to the return list
        output_images.append(output_image.astype)
    
    #Print a message if images saved
    if save:
        print(f"The cropped images are saved at {OUTPUT_PATH}")    
    
    #Record the end time
    t2 = time.time()
    
    #Print the passed time
    print(f"The process has been compleated in {round(t2-t1, 1)} seconds ")

    #Return the output list
    return output_images
