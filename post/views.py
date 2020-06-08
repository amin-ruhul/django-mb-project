from django.shortcuts import render

# Create your views here.
from .models import Post
def index(request):
    messages = Post.objects.all()
    contex = {
        'messages':messages
    }
    return render(request,'post/index.html',contex)