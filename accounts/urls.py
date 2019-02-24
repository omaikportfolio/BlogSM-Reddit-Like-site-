from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.SignUp.as_view(), name = 'signup'),
    path('login/', auth_views.LoginView.
                as_view(template_name = 'accounts/login.html'), name = 'login'),
    path('logout/', auth_views.LogoutView.as_view(), name = 'logout'),
    path('profile/<int:pk>', views.ProfileDetail.as_view(),
                                                    name = 'profile_detail'),
    path('profile_pic/<int:pk>/update', views.ProfileUpdate.as_view(),
                                                    name = 'profile_update')
]
