from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from arii.models import Post

def arii(request):
    posts = Post.objects.all()
    posts.reverse()
    return render(request, 'arii/index.html', {'posts': posts})

def submit(request):
    try:
        string = request.POST['comment']
        post = Post(string=string)
        post.save()
    except:
        pass
    
    return HttpResponseRedirect(reverse('arii'))
