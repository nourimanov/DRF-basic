from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Posts(BaseModel):
    title = models.CharField(max_length=255)
    description = models.TextField()
    author = models.ForeignKey('auth.User', models.CASCADE)


class Comment(BaseModel):
    post = models.ForeignKey('app.Posts', models.CASCADE)
    text = models.CharField(max_length=255)
    file = models.FileField(upload_to='comment/file/')
    author = models.ForeignKey('auth.User', models.CASCADE)
