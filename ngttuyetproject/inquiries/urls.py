from django.urls import path
from .views import InquiryView, InquirySuccessView

app_name = "inquiries"

urlpatterns = [
    path("", InquiryView.as_view(), name="inquiry_form"),
    path("success/", InquirySuccessView.as_view(), name="inquiry_success"),
]
