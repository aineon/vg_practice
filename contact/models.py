from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=50, null=False, blank=False)
    subject = models.CharField(max_length=254, null=False, blank=False)
    message = models.TextField(blank=False, null=False)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class NewsletterSubscription(models.Model):

    class Meta:
        verbose_name = 'Newsletter Subscription'

    email = models.EmailField(max_length=254, null=False, blank=False)
    date_subscribed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
