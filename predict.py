

import numpy as np
from keras.models import load_model
from tensorflow.keras.preprocessing import image
class dogcat:
    def __init__(self,filename):
        self.filename =filename


    def predictiondogcat(self):
        
        model = load_model('model.h5')

    
        imagename = self.filename
        test_image = image.load_img(imagename, target_size = (64, 64))
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = model.predict(test_image)

        if result[0][0] == 0:
            prediction = 'dog'
            return [{ "image" : prediction}]
        else:
            prediction = 'cat'
            return [{ "image" : prediction}]


