import os
from crop_focus_object import crop_focus_object

BASE_FOLDER = ""
IMAGES_PATH = os.path.join(BASE_FOLDER + "test_data")
WEIGHTS_PATH = os.path.join(BASE_FOLDER + "weights1.pt")

cropped_results = crop_focus_object(IMAGES_PATH = IMAGES_PATH,
                    WEIGHTS_PATH = WEIGHTS_PATH,
                    EXPAND_RATIO = 0.01,
                    save=True,
                    conf = 0.5)
