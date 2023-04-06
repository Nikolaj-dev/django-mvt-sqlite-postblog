from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, get_object_or_404, redirect

from .models import Post, PostLike, PostComment


def index(request: HttpRequest) -> HttpResponse:
    return HttpResponse("Index Page!")


def sign_up(request: HttpRequest) -> HttpResponse:
    context = {
        "form": UserCreationForm,
    }
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('posts')
    return render(request, 'sign_up.html', context=context)


def login_(request: HttpRequest) -> HttpResponse:
    context = {

    }
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(
            request,
            username=username,
            password=password,
        )
        if user is not None:
            login(request, user)
        return redirect('posts')
    return render(request, 'login.html', context=context)


def all_posts(request):
    posts = Post.objects.all()
    context = {
        "posts": posts,
    }
    return render(request, 'posts.html', context=context)


def detailed_post(request: HttpRequest, pk: int) -> HttpResponse:
    context = {
        "post": get_object_or_404(Post, pk=pk)
    }
    if request.method == "POST":
        try:
            PostComment.objects.create(
                who_commented_id=request.user.id,
                for_post_id=pk,
                comment=request.POST['comment']
            )
        except Exception as error:
            return HttpResponse(str(error))
    return render(request, 'post.html', context=context)


@login_required
def create_post(request: HttpRequest) -> HttpResponse:
    context = {

    }
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        image = request.FILES['image']
        Post.objects.create(
            title=title,
            body=body,
            author=request.user,
            image=image,
        )
        return redirect('posts')
    return render(request, 'create_post.html', context=context)


@login_required
def update_post(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    if request.user.username == post.author.username:
        context = {
            "title_value": post.title,
            "body_value": post.body,
            "img_value": post.image,
        }
        if request.method == "POST":
            if request.FILES.get('image') is None:
                post.title = request.POST['title']
                post.body = request.POST['body']
                post.save()
            else:
                post.title = request.POST['title']
                post.body = request.POST['body']
                post.image = request.FILES.get('image')
                post.save()
            return redirect('post', pk=pk)
    else:
        return HttpResponse("Method not allowed!")
    return render(request, 'update_post.html', context=context)


@login_required
def delete_post(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    if request.user.pk == post.author_id:
        post.delete()
        return redirect("posts")
    else:
        return HttpResponse("Method not allowed!")


def user_posts(request: HttpRequest, author: str) -> HttpResponse:
    posts = Post.objects.filter(author__username=author)
    context = {
        "posts": posts,
    }
    return render(request, 'user_posts.html', context=context)


def all_likes(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    likes = PostLike.objects.filter(for_post_id=post.id)
    context = {
        "likes": likes,
    }
    return render(request, 'likes_list.html', context=context)


def create_like(request: HttpRequest, pk: int) -> HttpResponse:
    post = Post.objects.get(pk=pk)
    user = request.user
    try:
        like = PostLike.objects.get(for_post=post, who_liked=user)
        if like.is_liked:
            like.is_liked = False
            like.save()
        else:
            like.is_liked = True
            like.save()
    except Exception as error:
        PostLike.objects.create(
            who_liked=user,
            for_post=post,
        )
    return redirect(request.META.get('HTTP_REFERER', None))


@login_required
def delete_comment(request: HttpRequest, pk: int) -> HttpResponse:
    comment = PostComment.objects.get(pk=pk)
    comment.delete()
    return redirect(request.META.get('HTTP_REFERER', None))


@login_required
def update_comment(request: HttpRequest, pk: int) -> HttpResponse:
    get_comment = PostComment.objects.get(pk=pk)
    if request.method == "POST":
        get_comment.comment = request.POST.get('comment')
        get_comment.save()
        return redirect('post', pk=get_comment.for_post_id)

    context = {
        "comment": get_comment,
    }
    return render(request, 'comment_update.html', context=context)

