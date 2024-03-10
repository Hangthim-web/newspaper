from django.urls import path

# from accounts.forms import CustomPasswordResetForm
from accounts.views import SignUpView, CheckTemplate
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("signup/",SignUpView.as_view(),name = "signup"),
    path("checkview/",CheckTemplate.as_view(),name="check"),
    # path('password_reset/', auth_views.PasswordResetView.as_view(
    #     form_class=CustomPasswordResetForm,
    #     template_name='password_reset_form.html',
    #     email_template_name='your_email_template.html'
    # ), name='password_reset'),
]
