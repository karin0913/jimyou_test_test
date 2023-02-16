# https://zenn.dev/shimakaze_soft/articles/7f3a12881614b5
from django.db import models
from accounts.models import Usertest
from django.utils import timezone


    # class Meta:
    #     verbose_name_plural = 'Pro'
    # def __str__(self):
    #     return self.gender

# https://di-acc2.com/programming/python/1694/
class Pro(models.Model):
    user = models.ForeignKey(Usertest,verbose_name='ユーザー',on_delete=models.PROTECT)
    limit = models.DateField(verbose_name='目標達成日',blank=False, null=False)
    title = models.CharField(verbose_name='目標の名前',max_length=30, blank=False, null=False)
    text = models.CharField(verbose_name='目標の説明',max_length=150, blank=False, null=False)
    check = models.BooleanField(verbose_name='完了/未完了',default=False)

class Postmain(models.Model):
    """投稿"""
    writer = models.ForeignKey(Usertest, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField(max_length=256)
    created_at = models.DateTimeField(verbose_name='作成日',auto_now_add=True)

class Goodtest(models.Model):
    """投稿に対するいいね"""
    target = models.ForeignKey(Postmain, on_delete=models.CASCADE)
    user = models.ForeignKey(Usertest, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["target", "user"],
                name="good_unique"
            ),
        ]

class Comment(models.Model):
    """コメント"""
    writer = models.ForeignKey(Usertest, on_delete=models.CASCADE)
    text = models.TextField(max_length=150,blank=False, null=False)
    target = models.ForeignKey(Postmain, on_delete=models.CASCADE,)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Contents(models.Model):
    writer = models.ForeignKey(Usertest, on_delete=models.CASCADE)
    important = models.TextField(max_length=1000)
    high = models.TextField(max_length=1000)
    insurance = models.TextField(max_length=1000)
    bank = models.TextField(max_length=1000)
    bankpassword = models.TextField(max_length=1000)
    phone = models.TextField(max_length=1000)
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["writer"],
                name="contents_unique"
            ),
        ]

