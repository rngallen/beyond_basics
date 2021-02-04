
from django.contrib.auth.views import PasswordChangeView, PasswordResetDoneView
from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.


class MyPasswordChangeView(PasswordChangeView):
    template_name = 'users/password_change.html'
    success_url = reverse_lazy('users:password_reset_done')


class MyPasswordResetDoneView(PasswordResetDoneView):
    template_name = 'users/password_reset_done.html'
    success_url = reverse_lazy('index')
