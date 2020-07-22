from django.shortcuts import render, redirect
from .models import Order, Product

def index(request):
    if "quantity_count" not in request.session:
        request.session["quantity_count"] = 0
    if "total_count" not in request.session: 
        request.session['total_count'] = 0 
    context = {
        "all_products": Product.objects.all()
    }
    return render(request, "store/index.html", context)

def process(request):
    quantity_from_form = int(request.POST["quantity"])
    item = Product.objects.get(id=(request.POST["product_id"]))
    price_from_form = float(item.price)
    total_charge = quantity_from_form * price_from_form
    print("Charging credit card...")
    Order.objects.create(quantity_ordered=quantity_from_form, total_price=total_charge)
    request.session["quantity_count"] = request.session['quantity_count'] + quantity_from_form
    request.session["total_count"] = request.session['total_count'] + total_charge
    return redirect("/checkout")


def checkout(request):
    total_charge = request.session['total_count']
    quantity_count = request.session['quantity_count']
    last_purchase = Order.objects.last()
    price = last_purchase.total_price
    context = {
        "total_charge": total_charge,
        "quantity_count": quantity_count,
        "price": price
    }
    return render(request, "store/checkout.html", context)