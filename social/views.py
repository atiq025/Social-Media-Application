from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import PostForm, UserRegistrationForm
from .models import Post
from django.db.models import Q


# Registration View
def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            # set staff status to True
            user.is_staff = True
            user.save()
            login(request, user)
            return redirect("home")
            # return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, "social/register.html", {"form": form})


# Login View
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "social/login.html", {"form": form})

# Logout View
@login_required
def logout_view(request):
    logout(request)
    return redirect("login")

# Homepage (Global Feed)
def home(request):
    posts = Post.objects.all()

    search_query = request.GET.get("search", "")
    filter_media = request.GET.get("filter_media", "")
    sort_option = request.GET.get("sort", "-created_at")

    if search_query:
        posts = posts.filter(Q(content__icontains=search_query))

    if filter_media == "text":
        posts = posts.filter(image__isnull=True, content__isnull=False).exclude(content="")
    elif filter_media == "image":
        posts = posts.filter(image__isnull=False)

    posts = posts.order_by(sort_option)

    return render(request, "social/home.html", {"posts": posts})

# Profile Page
@login_required
def profile(request):
    posts = request.user.posts.all()

    search_query = request.GET.get("search", "")
    sort_option = request.GET.get("sort", "-created_at")

    if search_query:
        posts = posts.filter(Q(content__icontains=search_query))

    posts = posts.order_by(sort_option)

    return render(request, "social/profile.html", {"posts": posts})

# Create Post
@login_required
def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, "Post created successfully!")
            return redirect("profile")
    else:
        form = PostForm()
    return render(request, "social/create_post.html", {"form": form})

# Edit Post
@login_required
def edit_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Post updated successfully!")
            return redirect("profile")
    else:
        form = PostForm(instance=post)
    return render(request, "social/create_post.html", {"form": form})

# Delete Post
@login_required
def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id, user=request.user)
    if request.method == "POST":
        post.delete()
        messages.success(request, "Post deleted successfully!")
        return redirect("profile")
    return render(request, "social/delete_post.html", {"post": post})
