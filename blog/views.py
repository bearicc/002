from django.shortcuts import render
from django.http import JsonResponse
from django.utils import timezone
from .models import Post
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


@login_required(login_url='/blog/admin/')
def new(request):
    if request.method == "POST":
        title = request.POST["title"]
        data = request.POST["data"]
        author = User.objects.get(username='bear')
        post = Post.objects.create(author=author,
                                   title=title,
                                   text=data)
        post.publish()
        response_data = {'url': '/blog/',
                         'data': data}
        return JsonResponse(response_data, safe=False)

    return render(request, 'blog/new.html')
