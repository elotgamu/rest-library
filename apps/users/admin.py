from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as AuthUserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


from .models import User

# Register your models here.


class MyUserChangeForm(UserChangeForm):
    """docstring for MyUserChangeForm"""
    class Meta(UserChangeForm.Meta):
        model = User


class MyUserCreationForm(UserCreationForm):

    error_message = UserCreationForm.error_messages.update({
        'duplicate_username': 'Este usuario ya existe'
    })

    class Meta(UserCreationForm.Meta):
        model = User
        fields = ('first_name', 'last_name', 'email', 'username', 'profile')

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise forms.ValidationError(
            self.error_messages['duplicate_username']
        )


@admin.register(User)
class MyUserAdmin(AuthUserAdmin):
    """docstring for MyUserAdmin"""
    form = MyUserChangeForm
    add_form = MyUserCreationForm
    fieldsets = (
                ('User Profile', {'fields': ('name', 'profile',)}),
    ) + AuthUserAdmin.fieldsets
    list_display = ('username', 'first_name', 'last_name', 'email', 'profile')
    search_fields = ['email']
