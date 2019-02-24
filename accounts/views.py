from django.shortcuts import render
from django.contrib.auth import get_user_model
from django.views.generic import CreateView, UpdateView, DetailView
from django.urls import reverse_lazy, reverse
from . import forms
from .models import Profile
# Create your views here.

class SignUp(CreateView):
    form_class = forms.UserCreateForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

class ProfileUpdate(UpdateView):
    model = get_user_model()
    form_class = forms.ProfileUpdateForm
    template_name = 'accounts/profile_update.html'

    def get_success_url(self):
        pk = self.kwargs['pk']
        return reverse_lazy('accounts:profile_detail', kwargs={'pk': pk})

    def get_initial(self):
        initial = super().get_initial()
        initial['gender'] = self.request.user.profile.gender
        initial['birth_date'] = self.request.user.profile.birth_date
        initial['location'] = self.request.user.profile.location
        initial['profile_pic'] = self.request.user.profile.profile_pic
        initial['bio'] = self.request.user.profile.bio
        return initial

class ProfileDetail(DetailView):
    model = get_user_model()
    template_name = 'accounts/profile_detail.html'
