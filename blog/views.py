from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def new(request):
    if request.method == "POST":
        data = request.POST["data"]
        author = User.objects.get(username='bear')
        post = Post.objects.create(author=author,
                                   title='A New Post',
                                   text=data)
        post.publish()
        response_data = {'url': '/blog/',
                         'data': data}
        return JsonResponse(response_data, safe=False)

    return render(request, 'blog/new.html')
