from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import profile, edit_profile
from .forms import LoginUserForm


urlpatterns = [
    path(
        'login/',
        LoginView.as_view(
            template_name='users/login.html',
            authentication_form=LoginUserForm
        ),
        name='login'
    ),

    path(
        'logout/',
        LogoutView.as_view(),
        name='logout'
    ),
    path(
        'profile/',
        profile,
        name='profile'
    ),
    path(
        'profile/edit/',
        edit_profile,
        name='edit_profile'
    ),
]