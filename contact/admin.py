from django.contrib import admin
from .models import Message, NewsletterSubscription


class NewsletterAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_subscribed',)


admin.site.register(NewsletterSubscription, NewsletterAdmin)
admin.site.register(Message)
