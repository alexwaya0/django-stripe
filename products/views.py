from django.shortcuts import render, redirect  # new
from django.conf import settings  # new
from django.urls import reverse  # new

import stripe  # new


def home(request):  # new
    stripe.api_key = settings.STRIPE_SECRET_KEY
    if request.method == "POST":
        checkout_session = stripe.checkout.Session.create(
            line_items=[
                {
                    "price": "price_1Qvfx9FiF6wRnuOduaw8v4cy",  # enter yours here!!!
                    "quantity": 1,
                }
            ],
            mode="subscription",
            success_url=request.build_absolute_uri(reverse("success")),
            cancel_url=request.build_absolute_uri(reverse("cancel")),
        )
        return redirect(checkout_session.url, code=303)
    return render(request, "products/home.html")


def success(request):
    return render(request, "products/success.html")


def cancel(request):
    return render(request, "products/cancel.html")