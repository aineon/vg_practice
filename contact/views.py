from django.shortcuts import render
from django.contrib import messages

from .models import NewsletterSubscription
from .forms import ContactForm, SubscriptionForm


def contact(request):
    template = "contact/contact.html"

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,
                             "Message Sent! We'll be in touch shortly!")

        else:
            messages.error(request, 'Message failed to send.'
                           ' Please ensure the form is valid.')

    form = ContactForm()
    news_signup_form = SubscriptionForm(request.POST or None)

    context = {
        'form': form,
        'news_signup_form': news_signup_form,
    }

    return render(request, template, context)


def newsletter_signup(request):
    news_signup_form = SubscriptionForm(request.POST or None)

    if news_signup_form.is_valid():
        instance = news_signup_form.save(commit=False)
        if (NewsletterSubscription.objects.filter(
                email=instance.email).exists()):
            messages.error(request, 'Sorry! This email address \
                           is already registered for our Newsletter.')
        else:
            instance.save()
            messages.success(request, "Congratulations! "
                             " You've been added to our mailing list!")
    
    print(news_signup_form)
    context = {
        'news_signup_form': news_signup_form,
    }

    return render(request, context)
