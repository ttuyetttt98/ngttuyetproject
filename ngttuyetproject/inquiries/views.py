from django.views.generic import CreateView, TemplateView
from django.urls import reverse_lazy
from .forms import InquiryForm

class InquiryView(CreateView):
    form_class = InquiryForm
    template_name = "inquiries/inquiry_form.html"
    success_url = reverse_lazy("inquiries:inquiry_success")

class InquirySuccessView(TemplateView):
    template_name = "inquiries/inquiry_success.html"
