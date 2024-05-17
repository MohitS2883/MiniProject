from tensorflow.keras.models import load_model
import numpy as np
from keras.preprocessing import image
def pred(path):
    model = load_model('model.keras')
    img = image.load_img(path, target_size=(150, 150))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0
    predictions = model.predict(img_array)
    predicted_class = np.argmax(predictions)
    dic = {0:'Grassy',1:'Marshy',2:'Rocky',3:'Sandy'}
    return dic[predicted_class]