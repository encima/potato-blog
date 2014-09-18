from blog.models import Post, Tag, PostForm
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect
import datetime

def index(request):
    return render_to_response('index.html', {
        'categories': Tag.objects.all(),
        'posts': Post.objects.all()[:5]
    })

def new_post(request):
    if(request.method == 'POST'):
        form = PostForm(request.POST)
        new = form.save(commit=False)
        new.pub_date = datetime.datetime.now() 
        t = Tag(1, 'test')
        t.save()
        new.tag = t
        new.save()
        print new
        return HttpResponseRedirect('/blog')
    else:
        return render(request, 'new_post.html', {'form': PostForm(), 'title': 'New Post'})

def view_post(request, slug):   
    print 'view post'
    return render_to_response('view_post.html', {
        'post': get_object_or_404(Post, slug=slug)
    })

def save_post(request, slug):
    print request

def view_tag(request, slug):
    category = get_object_or_404(Tag, slug=slug)
    return render_to_response('view_category.html', {
        'tag': tag,
        'posts': Post.objects.filter(tag=tag)[:5]
    })
