from .forms import SubscriptionForm


def newsletter_subscription_form(request):
    """Make Newsletter Subscription Form available throughout the site"""
    news_sub_form = SubscriptionForm()

    context = {
        'news_sub_form': news_sub_form,
    }

    return context
