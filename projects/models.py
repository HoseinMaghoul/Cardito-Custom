from distutils.command.upload import upload
from re import T
from django.db import models
from datetime import datetime
# Create your models here.




class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    date = models.DateTimeField(default=datetime.now, blank=True)



    def __str__(self):
        return f'{self.name}-{self.description}'










class Projects(models.Model):
    category = models.ForeignKey(Category,on_delete=models.CASCADE ,related_name='categories', null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    photo_main = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    photo_1 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_2 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_3  = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_4 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_5 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_6 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_7 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_8 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_9  = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_10 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_11 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    photo_12 = models.ImageField(upload_to = 'photos/%Y/%m/%d/' , blank=True)
    is_published = models.BooleanField(default=True)
    project_date = models.DateTimeField(default=datetime.now, blank=True)




        
    
