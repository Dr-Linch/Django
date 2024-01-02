from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import CreateView, UpdateView, View
from users.forms import UserRegisterForm, UserProfileForm
from users.models import User
from django.urls import reverse_lazy, reverse
from django.core.mail import send_mail
from config.settings import EMAIL_HOST_USER
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
import random


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        new_user = form.save()
        code = ''.join(random.sample('0123456789', 4))
        new_user.verification_code = code
        send_mail(
            subject='Верификация SkyStore',
            message=f'''Перейдите по ссылке для верификации: http://127.0.0.1:8000/users/verification_code/{code}
    и введите Логин и пароль''',
            from_email=EMAIL_HOST_USER,
            recipient_list=[new_user.email]
        )
        return super().form_valid(form)


def verify_mail(request, code):
    user = User.objects.get(verification_code=code)
    user.is_active = True
    user.save()
    messages.success(request, 'Ваш аккаунт активирован!')
    return redirect(reverse('users:login'))


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


def generate_new_password(request):
    new_password = User.objects.make_random_password()
    send_mail(
        subject='Вы успешно сменили пароль',
        message=f'Ваш новый пароль: {new_password}',
        from_email=EMAIL_HOST_USER,
        recipient_list=[request.user.email]
    )
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('users:login'))


def reset_password(request):
    pass


def restore_password(request):
    if request.method == "POST":
        email = request.POST.get('email')
        user = get_object_or_404(User, email=email)
        new_password = User.objects.make_random_password()
        send_mail(
            subject='Восстановление пароля',
            message=f'Ваш новый пароль: {new_password}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email]
        )
        user.set_password(new_password)
        user.save()
        return redirect(reverse('users:login'))
    return render(request, "users/restore_password.html")
