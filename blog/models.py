from django.db import models
# from PIL import Image
from django.contrib.auth.models import User
from django.utils.timezone import now
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50,unique=True)

    class Meta:
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ManyToManyField(Category,related_name='post_set')
    img = models.ImageField(upload_to='post_img/',default='default.jpg')
  

    # def save(self,*args, **kwargs):
    #     if self.img:
    #         img = Image.open(self.img.path)
    #         if img.height > 300 or img.width>300:
    #             img_size=(300,300)
    #             img.thumbnail(img_size)
    #             img.save(self.img.path)
    #         super().save(*args, **kwargs)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    text = models.TextField()
    parent = models.ForeignKey('self',on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.user.username + ":"+ self.text[0:10]

