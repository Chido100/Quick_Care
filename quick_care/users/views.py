from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.urls import reverse_lazy
from .models import User
from .forms import UserRegisterForm

from django.contrib.auth import get_user_model
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from .tokens import account_activation_token


# Activation email
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except:
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.sucess(request, "Thank you for confirming your email. You can now login to your account.")
        return redirect('sign-in')
    else:
        messages.error(request, "Activation link is invalid.")
    return redirect('sign-in')


def activate_email(request, user, to_email):
    mail_subject = "Activate your account."
    message = render_to_string("users/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f'Dear {user}, please check your email {to_email} and click on the activation link to verify account.') 
    else:
        messages.error(request, f"There's been a problem sending email to {to_email}, please check that email address is correct.")

    

# Regsiter a User
class CreateUserView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        if form.is_valid():
           user = form.save(commit=False)
           user.is_active = False
           user.save()
           activate_email(self.request, user, form.cleaned_data.get('email'))
        return super().form_valid(form)