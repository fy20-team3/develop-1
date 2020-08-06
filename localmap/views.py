from django.shortcuts import render
from django.http import HttpResponse
import requests

#-------------------------------Global 変数------------------------------------------------------------------------------
addresscode = 13103         #デフォルト東京都港区
result = 0                  #観光地一覧格納
resulthotel = 0             #ホテル一覧格納
spotdst = 0                 #選択した観光地の数字格納
hoteldst = 0                #選択したホテルの数字格納

#-------------------------------1次元配列から2次元配列へ---------------------------------------------------------------------
def convert_1d_to_2d(l, cols):    
    return [l[i:i + cols] for i in range(0,len(l),cols)]

#-------------------------------住所コード入力------------------------------------------------------------------------------
def entrance(request):
    print("entrance START")
    return render(request,'location/enter.html')

#------------------------------観光地一覧表示-------------------------------------------------------------------------------
def viewspot(request):
    print("viewspot START")
    API_Key = 'dj00aiZpPVhOQ1FXTGhJdlNEOSZzPWNvbnN1bWVyc2VjcmV0Jng9NGI-'
    global addresscode
    global result

    
    if request.POST.get('num'):
        addresscode = request.POST.get('num')

    # if 'spot1' in request.POST:
    #     exsample = request.POST['spot1']
    # else:
    #     exsample = False
    
    # print(exsample)

    url = 'https://map.yahooapis.jp/search/local/V1/localSearch'

    query = {
        'ac': addresscode,
        'output': 'json',
        'sort' : 'rating',
        'appid': API_Key,
    }

    r = requests.get(url,params=query)
    #print("response",r.json())

    result = []
    for x in range(r.json()['ResultInfo']['Count']):
        print("x: ",x)
        
        result.append("名称: ")
        result.append(r.json()['Feature'][x]['Name'])
        
        result.append("カテゴリー: ")
        result.append(r.json()['Feature'][x]['Category'])
        
        result.append("住所: ")
        result.append(r.json()['Feature'][x]['Property']['Address'])
        
        result.append("電話番号: ")
        tel = r.json()['Feature'][x]['Property'].get('Tel1','No Information')
        result.append(tel)
        
        result.append("紹介: ")
        catch = r.json()['Feature'][x]['Property'].get('CatchCopy','No Information')
        result.append(catch)
        
        result.append("アクセス: ")
        ac = r.json()['Feature'][x]['Property'].get('Access1','No Information')
        result.append(ac)            
        
        result.append("緯度経度: ")
        result.append(r.json()['Feature'][x]['Geometry']['Coordinates'])

    result = convert_1d_to_2d(result,14)  #1次元配列から2次元配列
    
    
    for x in result:        #緯度経度分割
        # print("x:",x)
        s=x[13]
        l=s.split(',')
        x.append(l[0])
        x.append(l[1])
        # print("x:",x)
    
    
    #mapped_num = map(str, result) #格納される数値を文字列にする
    #result_string = ' '.join(mapped_num)
    
    return render(request,'location/index.html',{'address': addresscode,'result':result})

#-------------------------------ホテル一覧表示------------------------------------------------------------------------------
def hotelspot(request):
    print("hotelspot START")

    global addresscode
    global result
    global resulthotel
    global spotdst

    if 'spot1' in request.POST:
        spotdst = request.POST.getlist('spot1')
    else:
        spotdst = False

    spotdst = list(map(int,spotdst))
    print("spotdst:",spotdst)
    # print(result[spotdst[0]])

    gyosyucode = '0304'

    API_Key = 'dj00aiZpPVhOQ1FXTGhJdlNEOSZzPWNvbnN1bWVyc2VjcmV0Jng9NGI-'
    url = 'https://map.yahooapis.jp/search/local/V1/localSearch'

    query = {
        'ac': addresscode,
        'gc': gyosyucode,
        'output': 'json',
        'sort' : 'rating',
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
        
        resulthotel.append("カテゴリー: ")
        resulthotel.append(rh.json()['Feature'][x]['Category'])
        
        resulthotel.append("住所: ")
        resulthotel.append(rh.json()['Feature'][x]['Property']['Address'])
        
        resulthotel.append("電話番号: ")
        tel = rh.json()['Feature'][x]['Property'].get('Tel1','No Information')
        resulthotel.append(tel)
        
        resulthotel.append("紹介: ")
        catch = rh.json()['Feature'][x]['Property'].get('CatchCopy','No Information')
        resulthotel.append(catch)
        
        resulthotel.append("アクセス: ")
        ac = rh.json()['Feature'][x]['Property'].get('Access1','No Information')
        resulthotel.append(ac)
        
        resulthotel.append("緯度経度: ")
        resulthotel.append(rh.json()['Feature'][x]['Geometry']['Coordinates'])

    #mapped_num = map(str, resulthotel) #格納される数値を文字列にする
    #resulth_string = ' '.join(mapped_num)
    #print("resulth_string", resulth_string)

    resulthotel = convert_1d_to_2d(resulthotel,14)      #1次元配列から2次元配列

    for x in resulthotel:    #緯度経度分割
        # print("x:",x)
        s=x[13]
        l=s.split(',')
        x.append(l[0])
        x.append(l[1])
        # print("x:",x)

    return render(request,'location/hotel.html',{'address': addresscode,'resulthotel':resulthotel})

#-------------------------------旅行プラン出力------------------------------------------------------------------------------
def tripplan(request):
    print("tripplan START")
    global addresscode
    global result
    global resulthotel
    global spotdst
    global hoteldst

    if 'spot2' in request.POST:
        hoteldst = request.POST.getlist('spot2')
    else:
        hoteldst = False

    hoteldst = list(map(int,hoteldst))
   
    print("spotdst:",spotdst)
    print("hoteldst:",hoteldst)

    hoteloutput = []
    hoteloutput.append(resulthotel[hoteldst[0]])
    # for x in range(hoteldst):
    #     hoteloutput.append(resulthotel[x])

    #print(hoteloutput)

    spotoutput = []
    for x in range(len(spotdst)):
        i=spotdst[x]
        print("i=",i)
        spotoutput.append(result[i])

    #print(spotoutput)

    gcode = []
    for x in range(len(spotoutput)):
        if x==0:
            gcode.append(spotoutput[x][15])
            gcode.append(spotoutput[x][14])
            gcode.append(spotoutput[x][1])
        else:
            gcode.append(spotoutput[x][15])
            gcode.append(spotoutput[x][14])
            gcode.append(spotoutput[x][1])
            gcode.append(spotoutput[x][15])
            gcode.append(spotoutput[x][14])
            gcode.append(spotoutput[x][1])

    for x in hoteloutput:
        gcode.append(x[15])
        gcode.append(x[14])
        gcode.append(x[1])

    
    gcode = convert_1d_to_2d(gcode,6)
    print(gcode)


    # print(resulthotel[hoteldst[0]])

    # print(result[spotdst[0]])

    return render(request,'location/output.html',{'address': addresscode,'spot':spotoutput,'hotel':hoteloutput,'gcode':gcode})




# Create your views here.
