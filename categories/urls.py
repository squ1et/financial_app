from django.urls import path
from .views import CategoryListView, CategoryUpdateView, CategoryCreateView, CategoryDeleteView

urlpatterns = [
    path("", CategoryListView.as_view(), name='home'),
    path("category/<int:pk>/", CategoryUpdateView.as_view(), name='category_detail'),
    path("category/new/", CategoryCreateView.as_view(), name="category_new"),
    path("category/<int:pk>/delete/", CategoryDeleteView.as_view(), name="category_delete"),
]