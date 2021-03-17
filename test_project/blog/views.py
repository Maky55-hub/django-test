from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView)
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post

def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request, 'blog/home.html', context)

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 2 # attribute of ListView, which adds pagination to the list of the objects, here 2 means 2 objects to be shown on each page


class PostDetailView(DetailView):
    model = Post
    # when template_name not specified looks for template according to this schema: <app>/<model>_<viewtype>.html
    # in this case template name : blog/post_detail.html


# mixins should always be before GenericViews, when inheriting
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']

    # in this case template name : blog/post_form.html

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


# mixins should always be before GenericViews, when inheriting 
class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    # in this case template name : blog/post_form.html
    # that means the same template for create and update is used per default

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False


# mixins should always be before GenericViews, when inheriting
class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    # in this case template name : blog/post_confirm_delete.html

    def test_func(self):
        post = self.get_object()
        if post.author == self.request.user:
            return True
        return False

def about(request):
    return render(request, 'blog/about.html')
