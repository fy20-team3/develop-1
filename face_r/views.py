from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponse

import asyncio
import io
import glob
import json
import os
import sys
import time
import uuid
import requests
from urllib.parse import urlparse
from io import BytesIO
from PIL import Image, ImageDraw
from azure.cognitiveservices.vision.face import FaceClient
from msrest.authentication import CognitiveServicesCredentials
from azure.cognitiveservices.vision.face.models import TrainingStatusType, Person, SnapshotObjectType, OperationStatusType

def index(request):
    return render(request, 'face_r/index.html')

#def photoin(request):
#    return render(request, '')
#photo strageに保存する。
#保存したurlを返す


def scan(request):

    # set to your own subscription key value
    subscription_key = '146e40172163433cb62be9bedc90c95e'
    assert subscription_key

    # replace <My Endpoint String> with the string from your endpoint URL
    face_api_url = 'https://18ticket-face.cognitiveservices.azure.com/face/v1.0/detect'

    image_url = 'https://upload.wikimedia.org/wikipedia/commons/5/56/Donald_Trump_official_portrait.jpg'


    headers = {
        #'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': subscription_key}

    params = {
        'returnFaceId': 'true',
        'returnFaceLandmarks': 'false',
        'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
    }

    #with open(r"C:\\django_iis\hello\myhello\picture\gettyimages-902654682-612x612.jpg", 'rb') as f:
       #img = f.read()

    response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
    print(json.dumps(response.json()))
    #pcode:place code no keisan
    #pcode_top = (response.faceRectangle.top * response.faceRectangle.left * response.faceRectangle.width * response.faceRectangle.height) % 47 + 1
    
    #print('pcode_top',pcode_top)

    pcode = '011002' #tokyo-to, koutou-ku
    #sql
    #acsess to mysql
    # MySQLの接続情報（各自の環境にあわせて設定のこと）
    #db_config = {
        #'host': 'localhost',
        #'db': 'sample_db',  # Database Name
        #'user': 'testuser',
        #'passwd': 'testpass',
        #'charset': 'utf8',
    #}
    #try:
    # 接続
        #conn = MySQLdb.connect(host=db_config['host'], db=db_config['db'], user=db_config['user'],
                               #passwd=db_config['passwd'], charset=db_config['charset'])
    place = '北海道札幌市'

    return render(request, 'face_r/scan.html', {'pcode': pcode, 'place': place})

def dbtest(request):
    #return HttpResponse('dbtest 始まるよ')
    # MySQL接続
    cnt = mysql.connector.connect(
        host='mysql-server-60149727.mysql.database.azure.com',
        port='3306',
        db='citycode',
        user='fy20user@mysql-server-60149727',
        password='fy20P@ssw0rd',
        charset='utf8'
    )

    # カーソル取得
    db = cnt.cursor(buffered=True)

    id = 10
    #id 
    
    # SQLクエリ実行（データ取得）
    sql = "SELECT todoufuken FROM citycode WHERE id='" + id + ';';
    db.execute(sql)
    # 表示
    todoufuken = db.fetchall()
    print(todoufuken)

    # SQLクエリ実行（データ取得）
    sql = "SELECT sikuchoson FROM citycode WHERE id='" + id + ';';
    db.execute(sql)
    # 表示
    sikuchoson = db.fetchall()
    print(sikuchoson)

    place = todoufuken + sikuchoson

    print(place)

    # カーソル終了
    db.close()
    # MySQL切断
    cnt.close()

    return httpResponce('placepowershellを確認')


def phototest(request):
    return render(request, 'face_r/photoform.html')

# Create your views here.
