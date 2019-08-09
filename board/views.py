from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from .models import Post, Tag
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'location', 'category']

    def dispatch(self, *args, **kwargs):
        return super(PostCreate, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.writer = self.request.user
        obj.save()
        Post.tag_save(obj)
        obj.save()
        return redirect('/post/read/'+str(obj.id))

class PostRead(DetailView):
    model = Post

class PostDelete(DeleteView):
    model = Post
    success_url = reverse_lazy('mainpage')