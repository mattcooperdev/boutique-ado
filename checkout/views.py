from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the moment.")
        return redirect(reverse('prodcuts'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LMYdaEkwgvj714Mcav5eoIM4ojIIGmaghg8wG4jokmdrt4oxyeVLYZ66BqAAPGeNlibxypE3CQYVfIBgZtTSLhe00Vz8GjYjs',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
