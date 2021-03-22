from django.urls import reverse_lazy
from django.shortcuts import render
from django.views import generic
from django.views.generic.base import View

from accounts.forms import CustomUserCreationForm
from accounts.models import User
from app.models import Picture


class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserAccountView(View):

    def get(self, request, login):

        context = {
            'user': User.objects.get(username=login),
            'pictures': Picture.objects.filter(login=login)
        }

        return render(request, 'registration/user_account.html', context=context)
