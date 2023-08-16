from django.shortcuts import render, get_object_or_404
from .models import Post


def home(request):
    # Buscar todos os posts do banco de dados
    posts = Post.objects.all()

    # Passar os posts para o template
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    comments = post.comments.filter(status='approved').order_by('-published_date')
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'blog/post_detail.html', context)
