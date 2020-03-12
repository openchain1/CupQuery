"""CollegQueryPortal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from accounts import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from Posts import views as post_views
from Comments import views as Comments_views
from accounts.forms import SignUpForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_post/', views.add_post, name='add-posts'),
    path('update profile/', views.UpdateProfileView.as_view(), name='update profile'),
    path('user info/', views.UpdateUserView.as_view(), name='update user info'),
    path('login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'template_name': 'registration/logout.html'}, name='logout'),
    path('home/', post_views.PostList.as_view(), name='home'),
    path('post-detail/<int:pk>/', login_required(post_views.PostDetail.as_view()), name='post_detail'),
    path('edit/post/<int:pk>', login_required(post_views.EditPost.as_view()), name='edit'),
    path('edit/delete/<int:pk>', login_required(post_views.DeletePost.as_view()), name='delete'),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('accounts/register/', views.MyRegistrationView.as_view(form_class=SignUpForm), name="registration_register"),
    path('accounts/', include('registration.backends.default.urls')),
    path('like/', Comments_views.like, name='like'),
    path('search_results/', post_views.postsearch, name="search"),
]

if settings.DEBUG:
        urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
