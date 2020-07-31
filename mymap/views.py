from django.shortcuts import render
from django.http import HttpResponse
from .forms import  SignUpForm, LoginForm
from django.contrib.auth import login, authenticate # この行を追加
from django.shortcuts import render, redirect
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, TemplateView
from .models import   Review
import json
import requests
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.db.models import Avg
from django.contrib import messages


# index関数を読み込んだらmymap/mymap_info.htmlに飛ぶように設定
def index(request):
  return render(request, 'mymap/mymap_info.html')


#ユーザ管理機能（新規ユーザ登録）
class SignUp(CreateView):
    form_class = SignUpForm
    #新規ユーザ登録のHTMLページの定義
    template_name = 'mymap/newaccount.html'

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
        return render(request, 'mymap/newaccount.html', {'form': form})


#Djangoが標準で持っているlogin機能とlogout機能の設定
class Login(LoginView):
    form_class = LoginForm
    template_name = 'mymap/login.html'


