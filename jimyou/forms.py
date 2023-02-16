import os

from django import forms
from django.core.mail import EmailMessage
from accounts.models import Usertest
from .models import Pro
from .models import Postmain,Goodtest,Comment,Contents
class CreateForm(forms.ModelForm):
    class Meta:
        model = Pro
        fields = ('limit', 'title', 'text','check')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ServiceForm(forms.Form):
    class Meta:
        model = Pro
        fields = ('check')

class CommentCreateForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
        widgets = {
            'text': forms.TextInput(),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class PostCreateForm(forms.ModelForm):
    class Meta:
        model = Postmain
        fields = ('title', 'text')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class GoodCreateForm(forms.ModelForm):
    class Meta:
        model = Goodtest
        fields = ('target','user')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class EndCreateForm(forms.ModelForm):
    class Meta:
        model = Contents
        fields = ('important', 'high', 'insurance','bank','bankpassword','phone')
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

#from django import forms
# https://hombre-nuevo.com/python/python0038/
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from .models import Usertest
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import validate_email

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
       super().__init__(*args, **kwargs)
       #htmlの表示を変更可能にします
       self.fields['username'].widget.attrs['class'] = 'form-control'
       self.fields['password'].widget.attrs['class'] = 'form-control'

class UserCreateForm(UserCreationForm):
    birthday = forms.CharField(required=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['birthday'].widget.attrs['class'] = 'form-control'
        self.fields['country'].widget.attrs['class'] = 'form-control'
        self.fields['gender'].widget.attrs['class'] = 'form-control'

    class Meta:
       model = Usertest
       fields = ("username", "password1", "password2","birthday","country","gender")


class UserUpdateForm(forms.ModelForm):
 
    # 入力を必須にするために、required=Trueで上書き
    birthday = forms.CharField(required=True)
    email = forms.EmailField(max_length=30, required=True)
    userver = forms.CharField(max_length=30, required=True)
 
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.user = kwargs.get('instance', None)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['birthday'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['userver'].widget.attrs['class'] = 'form-control'
 
    class Meta:
        model = User
        fields = (
            "username", "birthday", "email", "userver",
        )
 
    def clean_email(self):
        email = self.cleaned_data["email"]
 
        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("正しいメールアドレスを指定してください。")
 
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return email
        else:
            if self.user.email == email:
                return email
 
            raise ValidationError("このメールアドレスは既に使用されています。別のメールアドレスを指定してください")
 
class UserPasswordChangeForm(PasswordChangeForm):
    pass


