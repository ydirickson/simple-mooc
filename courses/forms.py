from django import forms
from django.core.mail import send_mail
from django.conf import settings

from core.mail import send_mail_template

class ContactCourseForm(forms.Form):
    name = forms.CharField(label="Nome")
    email = forms.EmailField(label="E-Mail")
    message = forms.CharField(label="Mensagem", widget=forms.Textarea)

    def send_email(self, course):
        subject = "[{}] Dúvidas sobre o curso".format(course)
        context = {
            "name": self.cleaned_data["name"],
            "email": self.cleaned_data["email"],
            "message": self.cleaned_data["message"]
        }
        send_mail_template(
            subject,"courses/contact_email.html",context,[settings.CONTACT_EMAIL]
        )