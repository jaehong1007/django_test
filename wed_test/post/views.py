from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post


def post_list(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }

    return render(request, 'post/post_list.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post,
    }
    return render(request, 'post/post_detail.html', context)


def post_create(request):
    if request.method == 'POST':
        photo = request.FILES['up_photo']
        post = Post.objects.create(photo=photo)
        return HttpResponse('succeed')
    else:
        return render(request, 'post/post_create.html')


def post_delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
    return redirect(post_list)
