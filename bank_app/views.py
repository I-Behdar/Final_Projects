from django.shortcuts import render
from django.views import View


class HomeView(View):
    def get(self, request):
        return render(request, "index.html")

    def post(self, request):
        return render(request, "")


class LoginView(View):
    def get(self, request):
        return render(request, "login.html")

    def post(self, request):
        return render(request, "")


class CreateAccountView(View):
    def get(self, request):
        return render(request, "create_account.html")

    def post(self, request):
        return render(request, "")
