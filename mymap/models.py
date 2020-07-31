from django.db import models
from django.contrib.auth.models import User 

# Create your models here.



class Review(models.Model):
    shop_id = models.CharField('店舗ID', max_length=10, blank=False)
    shop_name = models.CharField('店舗名', max_length=200, blank=False)
    image_url = models.CharField('画像１URL', max_length=300, blank=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    comment = models.TextField(verbose_name='レビューコメント', blank=False)
   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Meta:
        unique_together = ('shop_id', 'user')




