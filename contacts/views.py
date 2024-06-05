from django.views import View
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from .forms import ContactForm


class ContactIndexView(View):

    def get(self, request):
        form = ContactForm()
        context = {'form': form}
        return render(request, 'contact-index.html', context)

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()

            subject = form.cleaned_data.get('subject', '')
            message = form.cleaned_data.get('message', '')
            email_from = form.cleaned_data.get('email', '')
            name = form.cleaned_data.get('name', '')
            recipient_list = [settings.EMAIL_HOST_USER]

            message = f"Name: {name}\nEmail: {email_from}\n\n{message}"

            # Sending email
            send_mail(subject, message, email_from, recipient_list)

            # Debugging email
            print("Email From:", email_from)
            print("Recipient List:", recipient_list)

            return redirect('contacts:contact')

        context = {'form': form}
        return render(request, 'contact-index.html', context)


class ContactAboutView(View):

    def get(self, request):
        return render(request, 'contact-about.html')
