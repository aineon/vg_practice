from django.shortcuts import render, redirect
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

    context = {
        'form': form,
    }

    return render(request, template, context)

"""
def newsletter_signup(request):

    news_sub_form = SubscriptionForm()
    news_sub_redirect = request.POST.get('news_sub_redirect')

    if request.method == 'POST':
        news_sub_form = SubscriptionForm(request.POST)
        if (NewsletterSubscription.objects.filter(
                email=request.POST.get('email')).exists()):
            messages.error(request, 'Sorry! This email address \
                          is already registered for our Newsletter.')
        else:
            if news_sub_form.is_valid():
                news_sub_form.save()
            messages.success(request, "Congratulations! "
                             " You've been added to our mailing list!")

    news_sub_form = SubscriptionForm()

    return redirect(news_sub_redirect)
"""


def newsletter_signup(request):
    news_sub_form = SubscriptionForm(request.POST or None)
    news_sub_redirect = request.POST.get('news_sub_redirect')

    if news_sub_form.is_valid():
        instance = news_sub_form.save(commit=False)
        if (NewsletterSubscription.objects.filter(
                email=instance.email).exists()):
            messages.error(request, 'Sorry! This email address \
                           is already registered for our Newsletter.')
        else:
            instance.save()
            messages.success(request, "Congratulations! "
                             " You've been added to our mailing list!")
    return redirect(news_sub_redirect)
