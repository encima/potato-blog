from django.db import models
from django import forms
from django.forms import ModelForm

# class PostManager(models.Manager):
#     def create_post(self, title, body, date):
#         post = self.create(title=title, body=body, pub_date=date)
#         return post

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=100, unique=True)
    pub_date = models.DateTimeField()
    body = models.TextField()
    tag = models.ForeignKey('blog.Tag')
    markdown = models.BooleanField(default=True)

    # objects = PostManager()

    def __unicode__(self):
        return '%s' % self.title

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, { 'slug': self.slug })

class Tag(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True, unique=True)

    def __unicode__(self):
        return '%s' % self.name

    @models.permalink
    def get_absolute_url(self):
        return ('view_blog_category', None, { 'slug': self.slug })

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body', 'tag', 'markdown']

