from typing import Any, Dict, Set
from django.forms.models import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.views import LoginView, LogoutView
from .models import posts, Reply
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, FormView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from .form import ReplyForm


class home(ListView):
    model = posts
    template_name = 'base/home.html'
    context_object_name = 'home'



class login(LoginView):
    template_name = 'base/login.html'
    model = posts

    def get_success_url(self):
        return reverse_lazy('home')



class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):     
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)


class PostDetail(DetailView):
    template_name = 'base/post_detail.html'
    model = posts
    context_object_name = 'post'

    def get(self, *args, **kwargs):
        
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        reply_form = ReplyForm()
        context['reply_form'] = reply_form
        
        return self.render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        reply_form = ReplyForm(request.POST)
        if reply_form.is_valid():
            reply = reply_form.save(commit=False)
            reply.post1 = self.object
            reply.save()

            return redirect('post', pk=self.object.pk)
        
        context['reply_form'] = reply_form
        return self.render_to_response(context)

class CreatePost(CreateView):
    template_name = 'base/create_post.html'
    model = posts
    fields = ['title', 'description']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)


class DeletePost(DeleteView):
    template_name = 'base/delete_post.html'
    model = posts
    success_url = reverse_lazy('home')


class LogoutPage(LogoutView):
    template_name = 'base/logout.html'
    model = posts

class ReplyPost(CreateView):
    template_name = 'base/reply.html'
    model = Reply
    fields = ['body']
    success_url = reverse_lazy('post')

class UpdatePost(UpdateView):
    template_name = 'base/update.html'
    model = posts
    fields = ['title', 'description']
    success_url = reverse_lazy('home')

