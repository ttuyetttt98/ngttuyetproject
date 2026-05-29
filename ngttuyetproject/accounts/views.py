from django.shortcuts import render, redirect
from django.views.generic import CreateView, TemplateView, FormView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from products.models import Book   # LẤY SÁCH TỪ APP products


# ================================
#  HOME – Trang chủ
# ================================
class HomeView(TemplateView):
    template_name = "home.html"   # dùng templates/home.html

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['books'] = Book.objects.all().order_by('-id')[:8]   # lấy 8 sách mới nhất
        return context


# ================================
#  ĐĂNG KÝ TÀI KHOẢN
# ================================
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "accounts/signup.html"
    success_url = reverse_lazy('accounts:signup_success')

    def form_valid(self, form):
        user = form.save()
        self.object = user
        return super().form_valid(form)


class SignUpSuccessView(TemplateView):
    template_name = "accounts/signup_success.html"


# ================================
#  ĐĂNG NHẬP
# ================================
class LoginView(FormView):
    template_name = "accounts/login.html"
    form_class = AuthenticationForm
    success_url = reverse_lazy('accounts:home')

    def form_valid(self, form):
        """Nếu đăng nhập thành công thì login người dùng."""
        user = form.get_user()
        login(self.request, user)
        return super().form_valid(form)

    def form_invalid(self, form):
        """Thông báo lỗi khi đăng nhập thất bại."""
        return self.render_to_response(
            self.get_context_data(form=form, error="ユーザー名またはパスワードが違います。")
        )


# ================================
#  ĐĂNG XUẤT
# ================================
class LogoutView(View):
    def get(self, request):
        logout(request)
        return render(request, "accounts/logout.html")
