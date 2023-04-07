from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    title = models.CharField('Title', max_length=128, db_index=True)
    body = models.TextField('Text',)
    created_date = models.DateField('Date of creation', auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='posts_images/')

    def __str__(self):
        return self.title


class PostLike(models.Model):
    who_liked = models.ForeignKey(User, on_delete=models.CASCADE)
    for_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    is_liked = models.BooleanField(default=True)


class PostComment(models.Model):
    who_commented = models.ForeignKey(User, on_delete=models.CASCADE)
    for_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_img = models.ImageField(upload_to='profiles_images/')
    nickname = models.CharField(max_length=64)
