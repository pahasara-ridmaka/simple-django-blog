from .views import BlogListView, BlogDetailView
from django.urls import path

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>', BlogDetailView.as_view(), name='post_detail'),

]
