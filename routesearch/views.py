from django.shortcuts import render
from django.http import HttpResponse
#import requests  #requests.getのためにインポート

#import urllib.request
#import urllib.parse
#import urllib.error

def index(request):
    positions=[35.666104548381654,139.73185774868438,35.66471862664352,139.73139640873367]
    counters=[x for x in range(0, len(positions)-3, 2)]
    parms = {}
    for position in positions:
        key = 'route'
        if key not in parms:    #1
            parms[key] = []     #2
        parms[key].append(position) #3
        # results = {}
    print("parms= ", parms)
    
    nums = {}
    for counter in counters:
        key = 'counter'
        if key not in nums:
            nums[key] = []
        nums[key].append(counter)
    print('nums = ', nums)
    
    parms.update(nums) 
    print(parms)

    return render(request, 'routesearch/page.html', parms)

# def numdep(request):

