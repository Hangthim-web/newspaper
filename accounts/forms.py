from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # fields = UserCreationForm.Meta.fields + ("age",)
        fields = (
            "username",
            "age",
            "email",

        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = (
            "username",
            "email",
            "age",
        )

# class CustomPasswordResetForm(PasswordResetForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['email'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your email'})
