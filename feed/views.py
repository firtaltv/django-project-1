from django.shortcuts import render, redirect
from .models import Post
from .forms import PostCreationForm
from django.http import HttpResponseRedirect, HttpResponseNotFound, HttpResponseForbidden
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from functools import wraps


def authors_only(function):
    @wraps(function)
    def wrap(request, pk, *args, **kwargs):
        author = request.user  # переменная для записи залогиненого пользователя
        post = Post.objects.get(pk=pk)  # переменная для опреденнёного поста над которым собираются проводить действия
        if post.author == author:  # сравнение - является автор этого поста залогиненым пользователем
            return function(request, pk, *args, **kwargs)
        else:
            # return HttpResponseRedirect(reverse_lazy('profile'))
            return HttpResponseForbidden()

    return wrap


@login_required(login_url='login')
def main(request):
    posts = Post.objects.all()  # все посты
    return render(request, 'feed/feed.html', {'posts': posts})


@login_required(login_url='login')
def create(request):
    if request.method == 'POST':
        form = PostCreationForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse_lazy('home'))
        else:
            error = "Invalid Form"
    else:
        form = PostCreationForm()

    data = {
        'form': form,
    }

    return render(request, 'feed/create_post.html', data)


@login_required(login_url='login')
def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        'post': post
    }
    print(request.user, post.author)
    template = 'feed/detail.html'
    return render(request, template, context)


@authors_only
@login_required(login_url='login')
def edit(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        if request.method == 'POST':
            form = PostCreationForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect(reverse_lazy('profile'))
            else:
                error = "Invalid Form"
        else:
            form = PostCreationForm(instance=post)

        data = {
            'form': form,
        }
        return render(request, 'feed/edit.html', data)

    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2 style='margin: 250px;'>Person not found</h2>")


@authors_only
@login_required(login_url='login')
def delete(request, pk):
    try:
        post = Post.objects.get(pk=pk)
        post.delete()
        return HttpResponseRedirect(reverse_lazy('profile'))
    except Post.DoesNotExist:
        return HttpResponseNotFound("<h2>Person not found</h2>")


@login_required(login_url='login')
def profile(request):
    posts = Post.objects.order_by('-date')
    posts_count = Post.objects.filter(author__username=request.user.username).count()
    return render(request, 'feed/profile.html', {'posts': posts,
                                                 'posts_count': posts_count})
