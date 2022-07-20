from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from bank_app.models import User


class HomeView(View):
    def get(self, request):
        return render(request, "index.html")


class CreateAccountView(View):
    def get(self, request):
        context = {}
        return render(request, "create_account.html", context)

    def post(self, request):
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        email = request.POST.get("email")
        password_1 = request.POST.get("pass1")
        password_2 = request.POST.get("pass2")

        if password_1 != password_2:
            return redirect("create_account")

        user = User.objects.create(first_name=first_name, last_name=last_name, email=email,
                                   password=password_1)

        error_messages = user.validate_user(user)

        if not error_messages:
            user.password = make_password(user.password)
            user.save()

        return render(request, "account.html")


class LoginView(View):
    def get(self, request):
        context = {}
        return render(request, "login.html", context)

    def post(self, request):
        email = request.POST.get("email")
        password = request.POST.get("pass")
        user = authenticate(request, email=email, password=password)
        print("User = ", user)
        if user is not None:
            login(request, user)
            return redirect("account")
        return HttpResponse("Something went wrong")


class AccountView(View):
    def get(self, request):
        return render(request, "account.html")

    def post(self, request):
        return render(request, "")