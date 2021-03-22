import os

from django.http.response import JsonResponse
from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from django.conf import settings

from accounts.models import User
from app.models import Picture, PictureHistory
from app.forms import PictureForm


class MainPageView(View):

    @method_decorator(login_required)
    def get(self, request):
        form = PictureForm()
        return render(request, 'app/main_page.html', context={'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = PictureForm(request.POST, request.FILES)

        if form.is_valid():
            picture = Picture()
            picture.login = request.user.username
            picture.picture = form.cleaned_data['picture']
            picture.save()

            email = get_object_or_404(User, username=picture.login).email
            message = f'{picture.login}; {picture.created_date}; {picture.picture.url}'
            send_mail('Uploaded image info', message, settings.EMAIL_HOST_USER, [email, ], fail_silently=False)

            return JsonResponse({'message': 'Image uploaded'})

        return JsonResponse({'message': 'Max file size is 2MB'})


class ReloadView(View):

    @method_decorator(login_required)
    def get(self, request, id):
        form = PictureForm()
        return render(request, 'app/reload_image.html', context={'form': form})

    @method_decorator(login_required)
    def post(self, request, id):
        form = PictureForm(request.POST, request.FILES)

        if form.is_valid():
            picture = Picture.objects.get(pk=id)

            PictureHistory.objects.create(old_path=picture.picture.url, picture=picture)
            os.remove(picture.picture.path)
            picture.picture = form.cleaned_data['picture']
            picture.save()

            return JsonResponse({'message': 'Image reloaded'})

        return JsonResponse({'message': 'Max file size is 2MB'})


class PictureHistoryView(View):

    @method_decorator(login_required)
    def get(self, request, id):

        picture = get_object_or_404(Picture, pk=id)
        return render(request, 'app/history.html', context={'picture': picture})
