from django.shortcuts import render
from django.http import HttpResponse

import asyncio
import glob
import io
import json
import MySQLdb
import os
import requests
import sys
import time
import uuid
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType

# Create your views here.

def scan(request):

    subscription_key = '146e40172163433cb62be9bedc90c95e'
    assert subscription_key

    face_api_url = 'https://18ticket-face.cognitiveservices.azure.com/face/v1.0/detect'

    image_url = 'https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg'
    
    if request.POST.get('url'):
        image_url = request.POST.get('url')

    headers = {
        #'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key}

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    #with open(r"imagePATH\image.jpg", 'rb') as f:
       #img = f.read()

    response = requests.post(
        face_api_url,
        params = params,
        headers = headers,
        json = {"url": image_url}
        #data=img
    )

    faceparam_buf = response.json()
    faceparam = faceparam_buf[0]

    id = (faceparam['faceRectangle']['top'] * faceparam['faceRectangle']['left'] * faceparam['faceRectangle']['width'] * faceparam['faceRectangle']['height']) % 1788 + 1
    id = (int(id))

    cnt = MySQLdb.connect(
        host = 'mysql-server-60149727.mysql.database.azure.com',
        port = 3306,
        db = 'citycode',
        user = 'fy20user@mysql-server-60149727',
        password = 'fy20P@ssw0rd',
        charset = 'utf8'
    )

    db = cnt.cursor()
    sql = "SELECT todoufuken FROM citycode WHERE id=" + str(id) + ';';
    db.execute(sql)
    todoufuken_tup = db.fetchall()[0]
    todoufuken = todoufuken_tup[0]

    sql = "SELECT sikuchoson FROM citycode WHERE id=" + str(id) + ';';
    db.execute(sql)
    sikuchoson_tup = db.fetchall()[0]
    sikuchoson = sikuchoson_tup[0]

    place = todoufuken + sikuchoson

    sql = "SELECT code FROM citycode WHERE id=" + str(id) + ';';
    db.execute(sql)
    code_tup = db.fetchall()[0]
    code = code_tup[0]
    pcode = code[:-1]

    db.close()
    cnt.close()
    return render(request, 'face_r/scan.html', {'pcode': pcode, 'place': place})


def form(request):
    return render(request, 'face_r/photoform.html')


def testface_r(request):
    return render(request, 'face_r/index.html')
