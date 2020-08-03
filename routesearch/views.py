from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def index(request):
    # content = {
        # 'title':'ルート検索結果',
        # 'position':[35.68233286004894,139.76649043148458,35.685173782469064,139.76584670132092], 
    # }
    # return render(request, 'routesearch/page.html', content)


import urllib.request
import urllib.parse
import urllib.error

def index(request):
    content = {
        serviceurl = 'https://map.yahooapis.jp/course/V1/routeMap?'
        positions=[35.68233286004894,139.76649043148458,35.685173782469064,139.76584670132092]
    # encodeSearchRoute = searchRoute.encode()

# param作成
        parms = dict()
        parms['appid'] ='dj00aiZpPTZ2eTFacW9oTHVMciZzPWNvbnN1bWVyc2VjcmV0Jng9MDY-'#プライバシー保護のため一部変更してます
        for position in positions:
            key = 'route'
            if 'route' not in parms:
                parms['route']=[]
            parms['route'].append(position)
    # parms['route'] = searchRoute
# parms['results'] = 100
# parms['output'] = 'xml'   
        url = serviceurl + urllib.parse.urlencode(parms)
    }
    return render(request, 'routesearch/page.html', content)
# print('Retrieving', url)
# uh = urllib.request.urlopen(url)
# data = uh.read().decode()
# print('Retrieved', len(data), 'characters')
# print(data[:200])


# 書き込み
# file = open('result.xml', 'w', encoding='UTF-8')
# file.write(data)
# file.close()

