from django import forms
from django.core.exceptions import ValidationError

from app.models import Picture


class PictureForm(forms.ModelForm):
    class Meta:
        model = Picture
        fields = ('picture', )

    def clean_picture(self):
        picture = self.cleaned_data.get('picture')
        megabyte_limit = 2.0

        if picture:
            if picture.size > megabyte_limit*1024*1024:
                raise ValidationError(f'Max file size is {megabyte_limit}MB')
            return picture
        else:
            raise ValidationError("Couldn't read uploaded image")
