from django.contrib.auth.models import AbstractUser
from django.db import models

class Usertest(AbstractUser):
    """拡張ユーザーモデル"""
    # email = models.EmailField(max_length=30, required=True)
    birthday = models.DateField(verbose_name='誕生日',null=True, blank=True)
    COUNTRY_CHOICES = (
        (u'ja', u'日本'),(u'us', u'アメリカ'),(u'uk', u'イギリス'),(u'ch', u'中国'),
        # (u'a', u'北海道'),(u'b', u'青森県'),(u'c', u'岩手県'),(u'd', u'宮城県'),
        # (u'e', u'秋田県'),(u'f', u'山形県'),(u'g', u'福島県'),(u'h', u'茨城県'),
        # (u'i', u'栃木県'),(u'j', u'群馬県'),(u'k', u'埼玉県'),(u'l', u'千葉県'),
        # (u'm', u'東京都'),(u'n', u'神奈川県'),(u'o', u'新潟県'),(u'p', u'富山県'),
        # (u'q', u'石川県'),(u'r', u'福井県'),(u's', u'山梨県'),(u't', u'長野県'),
        # (u'u', u'岐阜県'),(u'w', u'静岡県'),(u'x', u'愛知県'),(u'y', u'三重県'),
        # (u'z', u'滋賀県'),(u'aa', u'京都府'),(u'bb', u'大阪府'),(u'cc', u'兵庫県'),
        # (u'dd', u'奈良県'),(u'ee', u'和歌山県'),(u'ff', u'鳥取県'),(u'gg', u'島根県'),
        # (u'hh', u'岡山県'),(u'ii', u'広島県'),(u'jj', u'山口県'),(u'kk', u'徳島県'),
        # (u'll', u'香川県'),(u'mm', u'愛媛県'),(u'nn', u'高知県'),(u'oo', u'福岡県'),
        # (u'pp', u'佐賀県'),(u'qq', u'長崎県'),(u'rr', u'熊本県'),(u'ss', u'大分県'),
        # (u'tt', u'宮崎県'),(u'uu', u'鹿児島県'),(u'ww', u'沖縄県'),

    )
    country = models.CharField(verbose_name='国籍',null=True, blank=False, max_length=50,choices=COUNTRY_CHOICES)
    GENDER_CHOICES = (
        (u'M', u'男性'),
        (u'F', u'女性'),
        (u'N', u'未回答'),
    )
    gender = models.CharField(verbose_name='性別',null=True, blank=False, max_length=50,choices=GENDER_CHOICES)
    class Meta:
        verbose_name_plural = 'Usertest'
    REQUIRED_FIELDS = ["email", "birthday", "country", "gender"]
# https://hodalog.com/how-to-extend-django-user-model/
# https://www.maytisk.com/django-login/
# (venv_jimyou_app) C:\Users\karin09\venv_jimyou_app\private_jimyou>python manage.py createsuperuser
# ユーザー名: postgres
# メールアドレス: karin0214sp@gmail.com
# Password:
# Password (again):
# このパスワードは メールアドレス と似すぎています。
# Bypass password validation and create user anyway? [y/N]: y
# Superuser created successfully.
# https://github.com/knakajima3027/User-login-sample/blob/master/accounts/forms.py