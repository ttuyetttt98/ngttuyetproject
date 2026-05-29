from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Book

class BookListView(ListView):
    model = Book
    template_name = "products/book_list.html"
    context_object_name = "books"
    ordering = "-id"


class BookDetailView(DetailView):
    model = Book
    template_name = "products/book_detail.html"
    context_object_name = "book"


class BookCreateView(LoginRequiredMixin, CreateView):
    model = Book
    template_name = "products/book_create.html"
    fields = ["title", "author", "category", "description", "price", "image"]
    success_url = reverse_lazy("products:book_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
class BookCategoryView(ListView):
    model = Book
    template_name = "products/book_list.html"
    context_object_name = "books"

    def get_queryset(self):
        category = self.kwargs['category']
        return Book.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["selected_category"] = self.kwargs["category"]
        return context
