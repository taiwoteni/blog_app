from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import Post, Comment


@login_required
def add_comment(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Comment.objects.create(post=post, author=request.user, content=content)
            messages.success(request, 'Your comment has been added!')
        else:
            messages.error(request, 'Comment cannot be empty.')
    return redirect('post-detail', slug=slug)
