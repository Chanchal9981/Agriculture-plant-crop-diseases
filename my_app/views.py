from django.shortcuts import render

# Create your views here.

from django.core.files.storage import FileSystemStorage
from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import os
from PIL import Image
import  numpy as np
model=load_model("potato_plant_diease.h5")
def Agriculture_crop(plant):
    img=load_img(plant,target_size=(150,150))
    img=img_to_array(img)/255
    img=np.expand_dims(img,axis=0)
    img=model.predict(img).round(3)
    print(img)
    img=np.argmax(img)
    if img == 0:
        return "Bacterial_spot"
    elif img == 1:
        return "healthy"
    elif img == 2:
        return "Early_blight"
    elif img == 3:
        return "Potato_healthy"
    elif img == 4:
        return "Late_blight"
    elif img == 5:
        return "Tomato_Target_Spot"
    elif img == 6:
        return "Tomato_mosaic_virus"
    elif img ==7:
        return "Tomato_YellowLeaf_Curl_Virus"
    elif img == 8:
        return "Tomato_Bacterial_spot"
    elif img == 9:
        return "Tomato_Leaf_Mold"
    elif img == 10:
        return "Tomato_Septoria_leaf_spot"
    else:
        return "Tomato_Spider_mites"

def home(request):
    return render(request,'Home.html')
def result(request):
    if request.method=="POST":
        image=request.FILES["image"]
        fs=FileSystemStorage()
        imgg=fs.save(image.name,image)
        imgg=fs.url(imgg)
        test_img='.'+imgg
        pred=Agriculture_crop(plant=test_img)
        return render(request,'result.html',{"pred":pred,"user_img":imgg})

    return render(request,'result.html')
