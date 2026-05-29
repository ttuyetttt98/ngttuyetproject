from django import forms
from .models import Inquiry

class InquiryForm(forms.ModelForm):
    class Meta:
        model = Inquiry
        fields = ["name", "email", "title", "message"]

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'お名前'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'メールアドレス'}),
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '件名'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'お問い合わせ内容'}),
        }
