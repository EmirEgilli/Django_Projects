from django.shortcuts import render, redirect, get_object_or_404
from .forms import PostCreateForm
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from .models import Post

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_item = form.save(commit=False)
            new_item.user = request.user
            new_item.save()
            return redirect('index')  # Redirect to a success page or the index page
    else:
        form = PostCreateForm()
    return render(request, 'posts/create.html', {'form': form})

def feed(request):
    posts = Post.objects.all()
    return render(request, 'posts/feed.html', {'posts': posts})

@login_required
@require_POST
def like_post(request):
    post_id = request.POST.get('post_id')
    post = get_object_or_404(Post, id=post_id)
    if post.liked_by.filter(id=request.user.id).exists():
        post.liked_by.remove(request.user)
        liked = False
    else:
        post.liked_by.add(request.user)
        liked = True
    return JsonResponse({'liked': liked, 'likes_count': post.liked_by.count()})