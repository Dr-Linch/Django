from django.urls import path
from blog import views
from blog.apps import BlogConfig
from blog.views import BlogCreateView, BlogListView, BlogDetailView, BlogUpdateView, BlogDeleteView, toggle_publish

app_name = BlogConfig.name

urlpatterns = [
    path('blog/create/', BlogCreateView.as_view(), name='create'),
    path('blog/list/', BlogListView.as_view(), name='list'),
    path('view/<int:pk>/', BlogDetailView.as_view(), name='view'),
    path('blog/update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
]