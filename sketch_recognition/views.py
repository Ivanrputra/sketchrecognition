from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Canvas

import base64
from django.core.files.base import ContentFile
import re,random
# Create your views here.

from tensorflow.python.keras.models import Model
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import math
import tensorflow as tf
from PIL import Image
import urllib
import io 
import cv2
from io import StringIO,BytesIO
import os
from PIL import Image
from tensorflow.python.keras.models import load_model

from django.contrib.staticfiles.templatetags.staticfiles import static
# from django.contrib.staticfiles.storage import staticfiles_storage
from django.conf import settings
# from django.conf.urls.static import static


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

@csrf_exempt
def recognition(request):
    if request.is_ajax():
        # evidence= get_object_or_404(Evidence, pk=7)
        # image_data = base64.b64decode(re.search(r'base64,(.*)', request.POST['image']).group(1))
        # namefile = str(random.randint(1,21)*5)+'.jpg'
        # image = ContentFile(image_data, namefile)
        # canvas = Canvas.objects.create(user = "1")
        # canvas.image = image
        # canvas.save()

        path_model = os.path.join(settings.STATIC_ROOT, 'model.keras')
        model3 = load_model(path_model)


        # img = re.search(r'base64,(.*)', request.POST['image']).group(1)
        # tempimg = BytesIO(base64.b64decode(img))
        # im = Image.open(tempimg).convert('L')
        # # image = np.asarray(im,dtype=float)
        # image = np.asarray(im,dtype=np.uint8)
        
                
        # X_data = []
        # X_data.append (image) 
        # train_images = np.array(X_data)
        # x_train = train_images.reshape(-1,1024)
        # x_train = x_train[0:1] / 255.0

        
        # Ya = model3.predict(x=x_train)
        # Y = np.argmax(Ya,axis=1)

        img = re.search(r'base64,(.*)', request.POST['image']).group(1)
        tempimg = BytesIO(base64.b64decode(img))
        
        arr = np.asarray(bytearray(tempimg.read()), dtype=np.uint8)
        img = cv2.imdecode(arr, -1)
        image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        X_data = []
        X_data.append (image) 
        train_images = np.array(X_data)
        x_train = train_images.reshape(-1,1024)
        x_train = x_train[0:1] / 255.0

        Ya = model3.predict(x=x_train)
        Y = np.argmax(Ya,axis=1)
        
        
        a = ""
        if Y[0] == 0: a = "CIRCLE"
        if Y[0] == 1: a = "MUG"
        if Y[0] == 2: a = "EYEGLASSES"
        if Y[0] == 3: a = "HUMAN"
        if Y[0] == 4: a = "STAR"
        message = a
    else:
        message = "Not Ajax"
    return HttpResponse(message)

