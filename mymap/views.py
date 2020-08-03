from django.shortcuts import render
from django.http import HttpResponse
from .forms import  SignUpForm, LoginForm
from django.contrib.auth import login, authenticate # この行を追加
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .models import  Review
import json
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Avg
from django.contrib import messages


# index関数を読み込んだらmymap/mymap_info.htmlに飛ぶように設定
def index(request):
  return render(request, 'mymap/travel-top.html')


#ユーザ管理機能（新規ユーザ登録）
class SignUp(CreateView):
    form_class = SignUpForm
    #新規ユーザ登録のHTMLページの定義
    template_name = 'mymap/signup.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('mymap:index')
            #表示するHTMLのページ
        return render(request, 'mymap/signup.html', {'form': form})


#Djangoが標準で持っているlogin機能とlogout機能の設定
class Login(LoginView):
    form_class = LoginForm
    template_name = 'mymap/login.html'

class Logout(LogoutView):
    template_name = 'mymap/logout.html'

def Overview(request):
    return render(request, 'mymap/overview.html')

def Mypage(request):
    return render(request, 'mymap/mypage.html')


