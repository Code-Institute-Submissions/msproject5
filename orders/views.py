from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, UserOrderForm
from .models import OrderLineItem
from django.conf import settings
from django.utils import timezone
from products.models import Product
import stripe


# Create your views here.


stripe.api_key = settings.STRIPE_SECRET


@login_required()
def checkout(request):
    """Stripe payment logic for checkout and order table update"""
    if request.method == "POST":
        order_form = UserOrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if payment_form.is_valid() and order_form.is_valid():
            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.product_price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                    )
                order_line_item.save()
            order.order_total = total
            order.save()
            # Stripe payment
            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="GBP",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id'],
                )

                if customer.paid:
                    messages.error(request, "You have successfully paid")
                    request.session['cart'] = {}
                    return redirect(reverse('products'))
                else:
                    messages.error(request, "Unable to take payment")
                
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")
           
        else:
            messages.error(request,
                           "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = UserOrderForm()

    return render(request, "orders.html",
                  {'order_form': order_form,
                   'payment_form': payment_form,
                   'publishable': settings.STRIPE_PUBLISHABLE})
