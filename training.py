#importing required libraries and packages
from tensorflow.keras.preprocessing.image import ImageDataGenerator  #to apply transformations on training images
from tensorflow.keras.applications import MobileNetV2  #object detection and segmentation, fast
from tensorflow.keras.layers import AveragePooling2D  #for pooling and downsampling
from tensorflow.keras.layers import Dropout #avoiding overfiting i.e inability to perform for unseen data
from tensorflow.keras.layers import Flatten #flattwning the output from pooling layer, reshaping 
from tensorflow.keras.layers import Dense  #operation for dense layer. Get weighted layers
from tensorflow.keras.layers import Input #instantiate a keras tensorflow. For input layer
from tensorflow.keras.models import Model #grouping layers into object with training and inference features
from tensorflow.keras.optimizers import Adam #optimizer implementing Adam algo
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input #adequate image into the format required by our model
from tensorflow.keras.preprocessing.image import img_to_array #converting images into numpy arrays
from tensorflow.keras.preprocessing.image import load_img  #loads image to path with the given target_size
from tensorflow.keras.utils import to_categorical  #converts int class vectors into a binary matrix
from sklearn.preprocessing import LabelBinarizer  #Binarize using one-vs-all fashion
from sklearn.model_selection import train_test_split #splitting datset for training and testing purpose
from sklearn.metrics import classification_report  #Measure quality of predictions 
from imutils import paths #general image processing functions
import matplotlib.pyplot as plt #interactive plotting similar to matlab
import numpy as np  #numpy for ease of operations on arrays etc
import os

#setting up initial learning rate, epochs to train for, and batchsize
init_lr = 1e-4 #keep it low so that loss is measured accurately
EPOCHS = 20
BS = 32

Directory = r"C:\Users\ashle\Face-Mask-Detection\dataset"
Categories = ["with_mask", "without_mask"] #actually the folder names in which data set is splitted

#now we get the list of images from dataset ddirectory and initialise the list of data
print("INFO: loading images.....")
data=[]
labels=[]

for cat in Categories:
  path = os.path.join(Directory, cat)  
  for img in os.listdir(path): #listsdown all the images in directory
      img_path = os.path.join(path, img)
      image= load_img(img_path, target_size=(224, 224)) #from keras preprocessing
      image= img_to_array(image)
      image= preprocess_input(image)
      #now append to both lists
      data.append(image)
      labels.append(cat)
      
#now we have our image data in numerical value, but lables are still string or alphabets.
#so we need to convert it to useful form
lb= LabelBinarizer()
labels= lb.fit_transform(labels)
labels= to_categorical(labels)

data= np.array(data, dtype="float32")
labels= np.array(labels)

#splitting for training and testing purpose 20%for testing and 80%for training
(trainX, testX, trainY, testY) = train_test_split(data, labels, test_size=0.20, stratify= labels, random_state=42)

#training image generator- for data augmentaion
#next step will generate many images with one image by applying various prop like flipping, rotating, etc
aug= ImageDataGenerator(rotation_range=20, 
                        zoom_range= 0.15, 
                        width_shift_range= 0.2, 
                        height_shift_range=0.2, 
                        shear_range=0.15, 
                        horizontal_flip=True, 
                        fill_mode="nearest")

#load MobileNetV2 network
baseModel = MobileNetV2(weights="imagenet", include_top=False,
	input_tensor=Input(shape=(224, 224, 3)))

#place head fc model on top of base model and freeze them so they will not be updated during 1st training process
headModel= baseModel.output
headModel= AveragePooling2D(pool_size= (7,7))(headModel) #creating pooling layer
headModel= Flatten(name="flatten")(headModel) #flatten layer
headModel= Dense(128, activation="relu")(headModel) #add dense layer with 128 neurons, relu
headModel= Dropout(0.5)(headModel)  #avoid overfitting
headModel= Dense(2, activation= "softmax")(headModel)  #ouput model, with 2 layers with_mask and without_mask

#place  head fc model on top of base model. this is the actual model to train
model = Model(inputs= baseModel.input, outputs= headModel)
#freeze all layers of base model. 
for layer in baseModel.layers:
    layer.trainable = False
    
#complie the model
print("[Info] Compiling model")
opt= Adam(lr= init_lr, decay= init_lr/ EPOCHS)  
model.compile(loss="binary_crossentropy", optimizer=opt, metrics= ["accuracy"])

#train head of network
print("[Info] training head")
H = model.fit(
	aug.flow(trainX, trainY, batch_size=BS),
	steps_per_epoch=len(trainX) // BS,
	validation_data=(testX, testY),
	validation_steps=len(testX) // BS,
	epochs=EPOCHS)


#predicttions on testing set
print("[Info] evaluating network")
predIdxs= model.predict(testX, batch_size=BS)

#for each image in testing dataset, we fing index of label with corr largest predicted probability
predIdxs = np.argmax(predIdxs, axis=1)

#now show the formatted classifcation report
print(classification_report(testY.argmax(axis=1), predIdxs, target_names=lb.classes_))

#serialise model to disk
print("[Info] saving mask detector model...")
model.save("mask_detector.model", save_format="h5")

#plot training loss and accuracy
N= EPOCHS
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0,N), H.history["loss"], label= "train_loss")
plt.plot(np.arange(0,N), H.history["val_loss"], label= "val_loss")
plt.plot(np.arange(0,N), H.history["accuracy"], label= "train_acc")
plt.plot(np.arange(0,N), H.history["val_accuracy"], label= "val_acc")
plt.title("Training loss and accuracy")
plt.xlabel("Epoch #")
plt.ylabel("Loss/Accuracy")
plt.legend(loc ="lower left")
plt.savefig("plot.png")



