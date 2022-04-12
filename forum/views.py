
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import Post
from .forms import PostForm






# Create your views here.
def index(request):
    if request.method=='Post':
        form=Post.Form(request.POST)
        if form.isValid():
            form.save
            return HttpResponseRedirect('/')
        else:
            return HttpResponseRedirect(form.errors.as_json())

    posts=Post.objects.all()[:20]
    return render(request,'posts.html',
                    {'posts/':posts})

def delete(request,post_id):
    output='POST ID is' + str(post_id)
    return HttpResponse(output)