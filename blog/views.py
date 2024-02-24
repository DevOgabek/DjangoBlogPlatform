from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user.is_authenticated:
        post.views += 1
        post.save()
    return render(request, 'post_detail.html', {'post': post})

@login_required(login_url='signin')
def post_create(request):
    if request.method == 'POST':
        author = request.user
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        if title and content:
            post = Post.objects.create(author=author, title=title, content=content)
            messages.success(request, 'Post created successfully!')
            return redirect('post_detail', pk=post.pk)
        else:
            messages.error(request, 'Please provide both title and content.')
    return render(request, 'post_form.html')

@login_required(login_url='signin')
def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        messages.error(request, 'You are not authorized to edit this post.')
        return redirect('post_detail', pk=pk)

    if request.method == 'POST':
        title = request.POST.get('title', '')
        content = request.POST.get('content', '')
        if title and content:
            post.title = title
            post.content = content
            post.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('post_detail', pk=post.pk)
        else:
            messages.error(request, 'Please provide both title and content.')
    
    return render(request, 'post_form.html', {'post': post})

@login_required(login_url='signin')
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.user != post.author:
        messages.error(request, 'You are not authorized to delete this post.')
        return redirect('post_detail', pk=pk)

    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Post deleted successfully!')
        return redirect('post_list')

    return render(request, 'post_confirm_delete.html', {'post': post})
