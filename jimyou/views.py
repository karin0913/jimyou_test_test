from django.shortcuts import render
from django.views import generic
from django.shortcuts import render, redirect
from jimyou.models import Usertest,Pro,Postmain,Goodtest,Comment,Contents
from jimyou.forms import CreateForm,UserCreateForm,ServiceForm,PostCreateForm,GoodCreateForm,CommentCreateForm,EndCreateForm
import datetime
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import  UserPassesTestMixin
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CreateForm
import datetime
from django.views import View
from jimyou.forms import LoginForm
from django.contrib.auth import login
class BaseView(generic.TemplateView):
    template_name = "base.html"

class IndexView(generic.TemplateView):
    template_name = "index.html"

class HomeView(generic.TemplateView):
    template_name = "home-page.html"

class AboutusView(generic.TemplateView):
    template_name = "about-us.html"

class AboutmeView(generic.TemplateView):
    template_name = "about-me.html"

class ContactsView(generic.TemplateView):
    template_name = "contacts.html"

def add(request):
    """
    日記の記事を追加
    """
    # 送信内容を元にフォームを作る。POSTじゃなければ空のフォームを作成。
    form = CreateForm(request.POST or None)

    # method==POSTとは送信ボタンが押されたとき。form.is_validは入力内容に問題が無い場合Trueになる。
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('../../')
    def form_valid(self,form):
        Profilet = form.save(commit=False)
        Profilet.user=self.request.user
        Profilet.save()
    # 通常時のアクセスや入力内容に誤りがあれば、再度day_form.htmlを表示
    context = {
        'form':form
    }
    return render(request, 'contacts.html', context)

class CreateView(generic.CreateView):
    model = Pro
    template_name = 'contacts.html'
    form_class = CreateForm
    success_url = reverse_lazy('jimyou:services')
    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.user = self.request.user
        profile.save()
        messages.success(self.request, '目標を作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "目標の作成に失敗しました。")
        return super().form_invalid(form)

class HmView(generic.TemplateView):
    template_name = "hm.html"
    def get_context_data(self,**kwargs):
        hm_False = Pro.objects.filter(check=False).count()
        hm_True = Pro.objects.filter(check=True).count()
        context = {
            'hm_False':hm_False,
            'hm_True':hm_True,
        }
        return context




# class HmView(generic.TemplateView):
#     template_name = "hm.html"
#     def index(request):
#         model = Pro
#         form = ServiceForm()
#         birthday = Usertest.objects.all().values("birthday")
#         gender = Usertest.objects.all().values("gender")
#         item = Pro.objects.all()
#         context = {
#             'profile_list': item,
#             "birthday": birthday,
#             "gender": gender,
#             'form': form,
#         }
#         return render(request, 'hm.html',context)
    
class GurafuView(generic.TemplateView):
    template_name = "gurafu.html"


def home_view(request):
    context = {}
    context['form'] = CreateForm()
    return render(request, 'index.html', context)

def profile(request):
    model = Pro
    form = ServiceForm()
    item = Pro.objects.all().order_by('limit')
    """
    日記の一覧
    """
    context = {
        'profile_list': item,
        'form': form,
    }
    return render(request, 'services.html', context)


def limit(request):
    """
    日記の一覧
    """
    context = {
        'profile_list':Pro.objects.all().order_by('limit') ,
    }
    return render(request, 'services.html', context)

class loginView(generic.FormView):
    def post(self, request, *arg, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            user = Usertest.objects.get(username=username)
            login(request, user)
            return redirect('/')
        return render(request, 'index-account.html', {'form': form,})

    def get(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        return render(request, 'index-account.html', {'form': form,})

class post_in(generic.CreateView):
    form_class = PostCreateForm
    template_name = 'post_create.html'
    success_url = reverse_lazy('jimyou:services')
    def get(self, request,pk):
        profile = get_object_or_404(Pro.objects.all(), pk=pk)
        form = PostCreateForm(request.POST or None, instance=profile)
        return render(request, 'post_create.html', {'form': form,})
    def form_valid(self,form):
        formtest = form.save(commit=False)
        formtest.writer = self.request.user
        formtest.save()
        messages.success(self.request, '投稿しました。')
        return super().form_valid(form)

def good_in(request):
    model = Postmain
    item = Postmain.objects.all()
    context = {
        'post_list': item,
    }
    return render(request, 'post_list.html', context)

class post_in_input(generic.CreateView):
    model = Postmain
    template_name = 'post_input.html'
    form_class = PostCreateForm
    success_url = reverse_lazy('jimyou:post_list')
    def form_valid(self, form):
        profile = form.save(commit=False)
        profile.writer = self.request.user
        profile.save()
        messages.success(self.request, '一から投稿')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "一から投稿に失敗しました。")
        return super().form_invalid(form)

def good_detail(request,pk):
    """
    日記の詳細
    """
    good = get_object_or_404(Postmain.objects.all(),pk=pk)

    context = {
        'good_list':good,
    }
    return render(request, 'good_detail.html', context)

from django.shortcuts import redirect
from django.http import HttpResponseRedirect

# def good_test(request,pk):
#     good = get_object_or_404(Postmain, pk=pk)
#     m = Goodtest.objects.filter(target=good, user=request.user)
#     global is_user_liked_for_post
#     if request.method == "POST":
#         if m.exists():
#             is_user_liked_for_post = False
#             m.delete()
#         else:
#             is_user_liked_for_post = True
#             Goodtest.objects.create(target=good, user=request.user)
#     good_in = get_object_or_404(Postmain.objects.all(), pk=pk)
#     context = {
#         'good_list':good_in,
#         'is_user_liked_for_post':is_user_liked_for_post,
#     }
#     return render(request, 'good_good.html', context,is_user_liked_for_post)

def good_test_in(request,pk):
    form = GoodCreateForm(request.POST or None)
    good = get_object_or_404(Postmain, pk=pk)
    m = Goodtest.objects.filter(target=good, user=request.user)
    if Goodtest.objects.filter(target=good, user=request.user).exists():
        is_user_liked_for_post = False
    else:
        is_user_liked_for_post = True
    if is_user_liked_for_post==False:
        m.delete()
    else:
        Goodtest.objects.create(target=good, user=request.user)
    good_in = get_object_or_404(Postmain.objects.all(), pk=pk)
    context = {
        'good_list':good_in,
        'is_user_liked_for_post':is_user_liked_for_post,
    }
    return render(request, 'good_good.html', context)

class goodcomment(generic.CreateView):
    model = Comment
    form_class = CommentCreateForm
    template_name = 'good_comment.html'
    success_url = reverse_lazy('jimyou:post_list')
    def get_context_data(self,**kwargs):
        good = get_object_or_404(Postmain, pk=self.kwargs['pk'])
        post = get_object_or_404(Postmain.objects.all(), pk=self.kwargs['pk'])
        post_list = Comment.objects.filter(target=good)
        form = CommentCreateForm()
        context = {
            'post':post,
            'form':form,
            'post_list':post_list,
        }
        return context
    def form_valid(self,form):
        comment = form.save(commit=False)
        comment.target = Postmain.objects.get(pk=self.kwargs['pk'])
        comment.writer = self.request.user
        comment.save()
        messages.success(self.request, 'コメントを作成しました。')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "コメントの作成に失敗しました。")
        return super().form_invalid(form)
    
class ContentsView(generic.CreateView):
    template_name = "endcontents.html"
    form_class = EndCreateForm
    model = Contents
    success_url = reverse_lazy('jimyou:post_list')
    def get_context_data(self,**kwargs):
        form = EndCreateForm()
        if Contents.objects.filter(writer=self.request.user):
            item_post = False
        else:
            item_post = True
        context = {
            'form':form,
            'item_post':item_post,
        }
        return context
    def form_valid(self,form):
        end = form.save(commit=False)
        end.writer = self.request.user
        end.save()
        messages.success(self.request, 'コメントを作成しました。')
        return super().form_valid(form)
    





    # def get_context_data(request,self,**kwargs):
    #     form = EndCreateForm()
    #     if Contents.objects.filter(writer=self.request.user):
    #         item_post = True
    #     else:

    #         item_post = False
    #     if item_post == False:
    #         if request.method == 'POST' and form.is_valid():
    #             form.save()
    #     return redirect('/services')
    #     context = {
    #         'item_post' : item_post,
    #     }
    #     return context
