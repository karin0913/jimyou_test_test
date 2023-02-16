from django.shortcuts import render, redirect
from django.views import View
from django.views import generic
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import Usertest
from jimyou.models import Pro
from django.views.generic import CreateView,TemplateView,UpdateView
from jimyou.forms import UserCreateForm, LoginForm, UserUpdateForm,CreateForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib import messages
# https://qiita.com/sw1394/items/c81aa8685e003ea9f246
import datetime
from django.utils import timezone
from datetime import datetime, timedelta
def index(request):
  template_name = "login_app/index.html" # templates以下のパスを書く
  birthday = Usertest.objects.all().values("birthday")
  test = '2002-01-01'
# 171.55 2083344+172limitdata = 81.47  
#   date_format = "%Y-%m-%d"
#   birthday = datetime.strptime(birthday, date_format)
#   birthday = birthday.year
#   <QuerySet [{'birthday': datetime.date(2002, 12, 11)}]>
#   birthday = birthday + timedelta(days=81)
#   birthday = datetime.strptime(birthday, '%Y%m%d')
#   birthday = datetime.strptime(birthday)


  ctx = {"birthday": birthday,}
  return render(request,template_name,ctx)

def main_page(request):
    return render(request, 'registration/login.html')

def new_login_page(request):
    return render(request, 'registration/create.html')

def logout_page(request):
    return render(request, 'registration/logout.html')

class LogoutView(LoginRequiredMixin, LogoutView):
    """ログアウトページ"""
    template_name = "login_app/index.html"


#アカウント作成
class Create_Account(CreateView):
    def post(self, request, *args, **kwargs):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            #フォームから'username'を読み取る
            username = form.cleaned_data.get('username')
            #フォームから'password1'を読み取る
            password = form.cleaned_data.get('password1')
            #フォームに入力された'username', 'password1'が一致する会員をDBから探し，userに代入
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('/')
        form.add_error(None, 'LOGIN_ID、またはPASSWORDが違います。')
        return render(request, 'registration/create.html', {'form': form,})
    def get(self, request, *args, **kwargs):
        checks_value = request.POST.getlist('checks[]')

    def get(self, request, *args, **kwargs):
        form = UserCreateForm(request.POST)
        return  render(request, 'registration/create.html', {'form': form,})

create_account = Create_Account.as_view()

#ログイン
class Account_login(View):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = Usertest.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'registration/login.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'registration/login.html', {'form': form,})

account_login = Account_login.as_view()

#ユーザー情報更新
class UserUpdateForm(UpdateView):
    model = Usertest
    form_class = UserUpdateForm
    template_name = 'registration/user_form.html'

from datetime import datetime


def add(request):
    """
    日記の記事を追加
    """
    # 送信内容を元にフォームを作る。POSTじゃなければ空のフォームを作成。
    form = CreateForm(request.POST or None)

    # method==POSTとは送信ボタンが押されたとき。form.is_validは入力内容に問題が無い場合Trueになる。
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('profile_index')

    # 通常時のアクセスや入力内容に誤りがあれば、再度day_form.htmlを表示
    context = {
        'form':form
    }
    return render(request, 'registration/profile_form.html', context)

from django.shortcuts import render, redirect, get_object_or_404

def indexprofile(request):
    """
    日記の一覧
    """
    context = {
        'profile_list':Pro.objects.all(),
    }
    return render(request, 'registration/profile_index.html', context)

def detail(request,pk):
    """
    日記の詳細
    """
    profile = get_object_or_404(Pro.objects.all(),pk=pk)

    context = {
        'profile_list':profile
    }
    return render(request, 'registration/profile_detail.html', context)

def update(request, pk):
    """
    日記の記事変更
    """
    profile = get_object_or_404(Pro.objects.all(), pk=pk)
    form = CreateForm(request.POST or None, instance=profile)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('/services')
    context = {
        'form':form
    }
    return render(request, 'registration/profile_update.html', context)


def delete(request, pk):
    """
    日記の記事削除
    """
    profile = get_object_or_404(Pro, pk=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('/services')
    context = {
        'profile':profile
    }
    return render(request, 'registration/profile_delete.html', context)
