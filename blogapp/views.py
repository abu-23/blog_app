from django.shortcuts import render, redirect
from django.template import context
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Blog
from django.urls import reverse_lazy, reverse
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect


# Create your views here.

def LikeView(request, pk):
    post = get_object_or_404(Blog, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))
    # return redirect('article_details', post.pk)


class HomeView(ListView):
    model = Blog
    template_name = 'home.html'


class ArticleDetailView(DetailView):
    model = Blog
    template_name = 'blog_detail.html'
    context_object_name = 'post'

    def get_context_data(self, *args, **kwargs):
        context = super(ArticleDetailView, self).get_context_data()
        stuff = get_object_or_404(Blog, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()
        context["total_likes"] = total_likes
        return context

class AddpostView(CreateView):
    model = Blog
    template_name = "add_post.html"
    fields = ('title', 'body','author')
    context_object_name = 'post'


class UpdatePostView(UpdateView):
    model = Blog
    template_name = "update_post.html"
    fields = ('title', 'body')
    context_object_name = 'post'


class DeletePostView(DeleteView):
    model = Blog
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
    context_object_name = 'post'
