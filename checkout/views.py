from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "Your bag is empty!")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IT7cbHovirDFYtchWYvEjOQd1Fnjua4q8mITV7kKl2vO9mkVSYGIPtCnJ8CElUe9VePmshuRYt2eevn01ZNyVMK00AcHXrPc3',
        'client_secret': 'test client'
    }

    return render(request, template, context)
