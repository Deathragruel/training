from django.shortcuts import render, redirect
from .models import BlogPost
from .forms import BlogPostForm

# Create your views here.
def home(request):
    """ The view for the home page. """
    blog_posts = BlogPost.objects.order_by('-date_added')
    context = {'blog_posts': blog_posts}
    return render(request, 'blogs/home.html', context)

def new_blog(request):
    """ View for creating new blog. """
    if request.method != 'POST':
        form = BlogPostForm()
    else:
        form = BlogPostForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    context = {'form': form}
    return render(request, 'blogs/new_blog.html', context)

def edit_blog(request, blog_id):
    """ View for editing blogs. """
    blog = BlogPost.objects.get(id=blog_id)
    if request.method != 'POST':
        form = BlogPostForm(instance=blog)
    else:
        form = BlogPostForm(instance=blog, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blogs:home')
    context = {'blog': blog, 'form': form}
    return render(request, 'blogs/edit_blog.html', context)
