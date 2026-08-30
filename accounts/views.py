from django.shortcuts import render
from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    authentication_form = CustomLoginForm

    redirect_authenticated_user = True


def dashboard(request):
    return render(request, 'accounts/dashboard.html')