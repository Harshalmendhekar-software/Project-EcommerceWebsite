from django.db import models
import datetime
import os

def get_file_path(request,filename):
    orignal_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime.orignal_filename)
    return os.path.join('uploads/',filename)

class Category(models.Model):
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    image = models.ImageField(upload_to=get_file_path,null=True,blank=True)
    description = models.TextField(max_length=500,null=False,blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    slug = models.CharField(max_length=150,null=False,blank=False)
    name = models.CharField(max_length=150,null=False,blank=False)
    product_image = models.ImageField(upload_to=get_file_path,null=True,blank=True)
    small_description = models.CharField(max_length=250,null=False,blank=False)
    quantity = models.IntegerField(null=False,blank=False)
    orignal_price = models.FloatField(null=False,blank=False)
    selling_price = models.FloatField(null=False,blank=False)

def __str(self):
    return self.slug

class Slides(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to="images")

    def _str_(self):
        return self.name

# Create your models here.
