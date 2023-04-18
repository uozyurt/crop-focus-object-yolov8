def choose_bbox(boxes:list,
                image_size:tuple,
                center_coordinates:tuple = (0.5,0.5),
                input_xyxy:bool = False,
                input_normalized:bool = True,
                return_xyxy:bool = True,
                AREA_RATIO_THRESHOLD:float = 0.8):
    '''
    In case of multiple object detections with same class, this function returns the most desired bbox coordinates.
    
    Input format: Nested list, containing lists with 4 numbers which represents coordinates of bboxes.
    
    image_size: (w,h) a tuple containing width and height
    
    center_coordinates: (x,y) a tuple containing x and y coordinates for a center which will be used to choose bboxes.

    If input_xyxy: The function assumes the input format is [x1,y1,x2,y2], else, the input is assumed to be in [x,y,w,h] format.
    
    If input_normalized: The function assumes the coordinates is normalized in (0,1) range.
    
    If return_xyxy: The function return the [x1,y1,x2,y2] coordinates of the chosen bbox, else, the output will be [x,y,w,h] format.
    
    AREA_RATIO_THRESHOLD: The ratio in range(0,1) to be used when deciding if a bbox comprises another bbox.
    
    Returns (-1,-1,-1,-1) if boxes is empty list.
    '''
    #Check if list is empty
    if(len(boxes) == 0):
        return (-1,-1,-1,-1)
    
    #Chech if list has just 1 bbox
    if(len(boxes) == 1):
        #Select the bbox, determine its coordinates and convert to xyxy format.
        final_box = boxes[0]
        if(input_xyxy):
            if(input_normalized):
                final_x1, final_y1, final_x2, final_y2 = final_box[0] * image_w, final_box[1] * image_h, final_box[2] * image_w, final_box[3] * image_h
            else:
                final_x1, final_y1, final_x2, final_y2 = final_box[0], final_box[1], final_box[2], final_box[3]
        else:
            if(input_normalized):
                final_x, final_y, final_w, final_h = final_box[0] * image_w, final_box[1] * image_h, final_box[2] * image_w, final_box[3] * image_h
            else:
                final_x, final_y, final_w, final_h = final_box[0], final_box[1], final_box[2], final_box[3]
            final_x1, final_y1, final_x2, final_y2 = final_x - final_w/2, final_y - final_h/2, final_x + final_w/2, final_y + final_h/2
            
        #return the coordinates of chosen bbox for desired output format.
        if(return_xyxy):
            return int(final_x1), int(final_y1), int(final_x2), int(final_y2)
        else: #assumes that the output should be normalized if this option has chosen.
            final_x = (final_x1 + final_x2)/(2*image_w)
            final_y = (final_y1 + final_y2)/(2*image_h)
            final_w = (final_x2 - final_x1)/(image_w)
            final_h = (final_y2 - final_y1)/(image_h)
            return final_x, final_y, final_w, final_h
    
    
    
    
    #Determine the main images width and height.
    image_w, image_h = image_size
    
    #Sorts the boxes according to their center's distance to predetermined main image center.
    if(input_xyxy):
        if(input_normalized):
            sorted_boxes = sorted(boxes, key= lambda x : (((center_coordinates[0] - (x[2]+x[0])/2))**2 + ((center_coordinates[1] - (x[3]+x[1])/2)**2)))
        else:
            sorted_boxes = sorted(boxes, key= lambda x : (((center_coordinates[0] - ((x[2]+x[0])/2)/image_w)**2 + ((center_coordinates[1] - ((x[3]+x[1])/2)/image_h ))**2)))
    else:
        if(input_normalized):
            sorted_boxes = sorted(boxes, key= lambda x : ((center_coordinates[0] - x[0])**2 + (center_coordinates[1] - x[1])**2))
        else:
            sorted_boxes = sorted(boxes, key= lambda x : ((center_coordinates[0] - x[0]/image_w)**2 + (center_coordinates[1]- x[1]/image_h)**2))

    #Select the first bbox, determine its coordinates and convert to xyxy format.
    final_box = sorted_boxes[0]
    if(input_xyxy):
        if(input_normalized):
            final_x1, final_y1, final_x2, final_y2 = final_box[0] * image_w, final_box[1] * image_h, final_box[2] * image_w, final_box[3] * image_h
        else:
            final_x1, final_y1, final_x2, final_y2 = final_box[0], final_box[1], final_box[2], final_box[3]
    else:
        if(input_normalized):
            final_x, final_y, final_w, final_h = final_box[0] * image_w, final_box[1] * image_h, final_box[2] * image_w, final_box[3] * image_h
        else:
            final_x, final_y, final_w, final_h = final_box[0], final_box[1], final_box[2], final_box[3]
        final_x1, final_y1, final_x2, final_y2 = final_x - final_w/2, final_y - final_h/2, final_x + final_w/2, final_y + final_h/2

    #calculate the area of chosen bbox
    final_area = (final_x2 - final_x1) * (final_y2 - final_y1)
    
    if(len(sorted_boxes)>1): #if multiple bboxes exist.
        for current_box in sorted_boxes[1:]: #iterate boxes other than the first chosen one.
            #calculate the coordinates of current bbox.
            if(input_xyxy):
                if(input_normalized):
                    current_x1, current_y1, current_x2, current_y2 = current_box[0] * image_w, current_box[1] * image_h, current_box[2] * image_w, current_box[3] * image_h
                else:
                    current_x1, current_y1, current_x2, current_y2 = current_box[0], current_box[1], current_box[2], current_box[3]
            else:
                if(input_normalized):
                    current_x, current_y, current_w, current_h = current_box[0] * image_w, current_box[1] * image_h, current_box[2] * image_w, current_box[3] * image_h
                else:
                    current_x, current_y, current_w, current_h = current_box[0], current_box[1], current_box[2], current_box[3]
                current_x1, current_y1, current_x2, current_y2 = current_x - current_w/2, current_y - current_h/2, current_x + current_w/2, current_y + current_h/2
            
            #test if any intersection area exists.
            if(final_x2 <= current_x1 or final_x1 >= current_x2 or final_y2 <= current_y1 or final_y1 >= current_y2):
                continue
            
            #calculate the intersection coordinates.
            intersection_x1, intersection_y1, intersection_x2, intersection_y2 = max(current_x1, final_x1), max(current_y1, final_y1), min(current_x2, final_x2), min(current_y2, final_y2)
            
            #calculate the intersection area.
            intersection_area = (intersection_x2 - intersection_x1) * (intersection_y2 - intersection_y1)
            
            #check if the ratio of intersection area over chosen bbox area is greater than current bbox.
            if((intersection_area / final_area) >= AREA_RATIO_THRESHOLD):
                #if it is, then the current bbox comprises the previously chosen bbox. Then, choose the desired bbox as the current one.
                final_x1, final_y1, final_x2, final_y2 = current_x1, current_y1, current_x2, current_y2
                #recalculate the final bbox are for new bbox
                final_area = (final_x2 - final_x1) * (final_y2 - final_y1)
    
    #return the coordinates of chosen bbox for desired output format.
    if(return_xyxy):
        return int(final_x1), int(final_y1), int(final_x2), int(final_y2)
    else: #assumes that the output should be normalized if this option has chosen.
        final_x = (final_x1 + final_x2)/(2*image_w)
        final_y = (final_y1 + final_y2)/(2*image_h)
        final_w = (final_x2 - final_x1)/(image_w)
        final_h = (final_y2 - final_y1)/(image_h)
        return final_x, final_y, final_w, final_h