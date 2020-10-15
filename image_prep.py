
import matplotlib.pyplot as plt 

def show_image_prediction(animal) :
    ROWS = 64
    COLS = 64
    CHANNELS = 3
    
    image = image.reshape((ROWS, COLS, CHANNELS))
    model.predict(animal)
    plt.figure(figsize = (4,2))
    plt.imshow(image)
    plt.title("Test {} : I think this is {}".format(image_class))
    plt.show()
