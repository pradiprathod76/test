from django import forms
from .models import Post,Category,Audio,Pic
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class DateInput(forms.DateInput):
    input_type = 'date'

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['username','email']
    def save(self,commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        if commit:
            user.save()
        return user


class CgForm(forms.ModelForm):
            class Meta:
                model = Category
                fields = ['img','name','des']

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['name','des','img','audio','cg','sub','date']
        widgets = {
            'date': DateInput(),
        }

class PicForm(forms.ModelForm):
    class Meta:
        model = Pic
        fields = ['img','user']