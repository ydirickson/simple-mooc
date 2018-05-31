from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from core.mail import send_mail_template
from mooc.utils import generate_hash_key

from .models import PasswordReset

User = get_user_model()

class RegisterUserForm(forms.ModelForm):

    #email = forms.EmailField(label="E-mail")
    password1 = forms.CharField(label="Senha", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirmação de Senha", widget=forms.PasswordInput)

    def clean_password2(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 and password2 and password1 != password2:
            raise form.ValidationError("A confirmação da senha não está correta")
        return password2

    def save(self, commit=True):
        user = super(RegisterUserForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class Meta:
        model = User
        fields = ["email", "name"]

class PasswordResetForm(forms.Form):

    email = forms.EmailField(label="E-Mail")

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            return email
        else:
            raise forms.ValidationError("Nenhum usuário encontrado com esse e-mail")

    def save(self):
        user = User.objects.get(email=self.cleaned_data["email"])
        key = generate_hash_key(user.email)
        reset = PasswordReset(key=key, user=user)
        reset.save()

        template_name = "accounts/password_reset_mail.html"
        subject = "[SimpleMooc] Criando nova Senha"
        context = {
            "reset": reset
        }
        send_mail_template(subject, template_name, context, [user.email])


class EditAccountForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ["email", "name"]


