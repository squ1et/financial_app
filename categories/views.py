from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Category

class CategoryListView(ListView):
    model = Category
    template_name = "home.html"

class CategoryCreateView(CreateView):
    model = Category
    template_name = "category_new.html"
    fields = ["title", "body"]
    success_url = reverse_lazy("home")

class CategoryUpdateView(UpdateView):
    model = Category
    template_name = "category_detail.html"
    fields = ["title", "body"]
    success_url = reverse_lazy("home")

class CategoryDeleteView(DeleteView):
    model = Category
    template_name = "category_delete.html"
    success_url = reverse_lazy("home")
