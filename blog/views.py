from blog.models import Post, Tag, PostForm
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.shortcuts import render_to_response, get_object_or_404, render
from django.http import HttpResponseRedirect
import datetime, urllib
# import markdown

# show all blog posts
def index(request):
    return render_to_response('index.html', {
        'categories': Tag.objects.all(),
        'posts': Post.objects.all()[:5]
    })

def login(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/blog/new/')
    else:
        return render(request, 'login.html', {})

def user_logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/blog/')

# validate blog post and save
@login_required(login_url='/blog/login/')
def new_post(request):
    res_dict = {'title': 'New Post', 'form': PostForm()}
    if(request.method == 'POST'):
        form = PostForm(request.POST)
        res_dict['form'] = form
        if(form.is_valid()):
            new = form.save(commit=False)
            new.slug = urllib.quote_plus(new.title)
            new.pub_date = datetime.datetime.now() 
            try:
                new.save()
            except IntegrityError as e:
                res_dict['error'] = 'Sorry, blog title already exists and must be unique'
                return render(request, 'new_post.html', res_dict)
            return HttpResponseRedirect('/blog/view/' + new.slug)
        else:
            res_dict['error'] = 'Sorry, fields cannot be blank'
    return render(request, 'new_post.html', res_dict)


@login_required(login_url='/blog/login/')
def edit_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    print post
    res_dict = {'title': 'Edit Post', 'form': PostForm(instance=post)}
    return render(request, 'new_post.html', res_dict) 

@login_required(login_url='/blog/login/')
def delete_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    return HttpResponseRedirect('/blog/')

# show post and render as markdown if necessary
def view_post(request, slug):   
    print 'view post'
    post = get_object_or_404(Post, slug=slug)
    body = post.body
    # if(post.markdown == True):
        # body = markdown.markdown(body)
    return render_to_response('view_post.html', {
        'post': post,
        'body': body
    })

#Create a new tag if the provided one does not exist
def check_or_create_tag(name):
    try:
        x = Tag.objects.get(slug=name)
    except Tag.DoesNotExist:
        x = Tag(name)
        x.slug = name.strip()
        x.save()
    print x
    return x

