from django.urls import path
from .views import MyPasswordChangeView, MyPasswordResetDoneView

app_name = 'users'

urlpatterns = [
    path('change_password/', MyPasswordChangeView.as_view(), name='change_password'),
    path('password_reset_done/', MyPasswordResetDoneView.as_view(),
         name='password_reset_done')
]
