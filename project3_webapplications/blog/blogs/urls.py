from django.urls import path
from . import views

app_name = 'blogs'

urlpatterns = [
        # Home page with all blogs:
        path('', views.home, name='home'),

        # Page for creating new blogs:
        path('new_blog/', views.new_blog, name='new_blog'),

        # Page for editing blogs:
        path('edit_blog/<int:blog_id>/', views.edit_blog, name='edit_blog'),
        ]
