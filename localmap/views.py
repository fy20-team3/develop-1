from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import requests
import numpy as np

addresscode = 13103         #デフォルト東京都小平市

def convert_1d_to_2d(l, cols):
    return [l[i:i + cols] for i in range(0,len(l),cols)]

#l = [0,1,2,3,4,5]
#print(convert_1d_to_2d(l,3))

def viewspot(request):
    print("viewspot START")
    API_Key = 'dj00aiZpPVhOQ1FXTGhJdlNEOSZzPWNvbnN1bWVyc2VjcmV0Jng9NGI-'
    global addresscode

    """
    if request.POST['addresscode']:
        addresscode = request.POST['addresscode']
    """

    url = 'https://map.yahooapis.jp/search/local/V1/localSearch'

    query = {
        'ac': addresscode,
        'output': 'json',
        'appid': API_Key,
    }

    r = requests.get(url,params=query)
    #print("response",r.json())
    
    result = []
    for x in range(r.json()['ResultInfo']['Count']):
        print("x: ",x)
        if r.json()['Feature'][x]['Property']['Genre'][0].get('Code') != '0304009':
            result.append("名称: ")
            result.append(r.json()['Feature'][x]['Name'])
            result.append('\n')
            result.append("カテゴリー: ")
            result.append(r.json()['Feature'][x]['Category'])
            result.append('\n')
            result.append("住所: ")
            result.append(r.json()['Feature'][x]['Property']['Address'])
            result.append('\n')
            result.append("電話番号: ")
            tel = r.json()['Feature'][x]['Property'].get('Tel1','No Information')
            result.append(tel)
            result.append('\n')
            result.append("紹介: ")
            catch = r.json()['Feature'][x]['Property'].get('CatchCopy','No Information')
            result.append(catch)
            result.append('\n')
            result.append("アクセス: ")
            ac = r.json()['Feature'][x]['Property'].get('Access1','No Information')
            result.append(ac)
            
            result.append('\n\n')

    result = convert_1d_to_2d(result,18)
    #print(result[0][0])
    """
    c=0
    for x in result:
        print(c)
        print(x)
        c=c+1
    """
    #mapped_num = map(str, result) #格納される数値を文字列にする
    #result_string = ' '.join(mapped_num)
    """
    c=0
    for x in result_string:
        print(c)
        print(x)
        c=c+1
    """
    #print("addresscode",addresscode)

    
    return render(request,'location/index.html',{'address': addresscode,'result':result})

def hotelspot(request):
    print("hotelspot START")

    API_Key = 'dj00aiZpPVhOQ1FXTGhJdlNEOSZzPWNvbnN1bWVyc2VjcmV0Jng9NGI-'
    url = 'https://map.yahooapis.jp/search/local/V1/localSearch'

    global addresscode
    gyosyucode = '0304'

    #print(gyosyucode)

    query = {
        'ac': addresscode,
        'gc': gyosyucode,
        'output': 'json',
        'appid': API_Key,
    }

    rh = requests.get(url,params=query)
    #print("response",rh.json())

    resulthotel = []
    for x in range(rh.json()['ResultInfo']['Count']):
        print("x: ",x)
        print("gc : ",rh.json()['Feature'][x]['Property']['Genre'][0]['Code'])
        resulthotel.append("名称: ")
        resulthotel.append(rh.json()['Feature'][x]['Name'])
        resulthotel.append('\n')
        resulthotel.append("カテゴリー: ")
        resulthotel.append(rh.json()['Feature'][x]['Category'])
        resulthotel.append('\n')
        resulthotel.append("住所: ")
        resulthotel.append(rh.json()['Feature'][x]['Property']['Address'])
        resulthotel.append('\n')
        resulthotel.append("電話番号: ")
        tel = rh.json()['Feature'][x]['Property'].get('Tel1','No Information')
        resulthotel.append(tel)
        resulthotel.append('\n')
        resulthotel.append("紹介: ")
        catch = rh.json()['Feature'][x]['Property'].get('CatchCopy','No Information')
        resulthotel.append(catch)
        resulthotel.append('\n')
        resulthotel.append("アクセス: ")
        ac = rh.json()['Feature'][x]['Property'].get('Access1','No Information')
        resulthotel.append(ac)
        resulthotel.append('\n\n')

    mapped_num = map(str, resulthotel) #格納される数値を文字列にする
    resulth_string = ' '.join(mapped_num)
    #print("resulth_string", resulth_string)


    return render(request,'location/hotel.html',{'address': addresscode,'resulth':resulth_string})


# Create your views here.
