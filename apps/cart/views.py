from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from .models import Cart, CartItem
from apps.products.models import Product


@login_required
def cart_detail(request):
    """
    Отображение корзины пользователя
    """
    cart, created = Cart.objects.get_or_create(user=request.user)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


@login_required
def cart_add(request, product_id):
    """
    Добавление товара в корзину
    """
    product = get_object_or_404(Product, id=product_id, available=True)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product,
        defaults={'quantity': 1}
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'message': f'Товар {product.name} добавлен в корзину',
            'cart_total_items': cart.total_items,
            'cart_total_price': str(cart.total_price)
        })

    messages.success(request, f'Товар {product.name} добавлен в корзину')
    return redirect('cart:cart_detail')


@login_required
def cart_remove(request, product_id):
    """
    Удаление товара из корзины
    """
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'message': f'Товар {product.name} удален из корзины',
            'cart_total_items': cart.total_items,
            'cart_total_price': str(cart.total_price)
        })

    messages.success(request, f'Товар {product.name} удален из корзины')
    return redirect('cart:cart_detail')


@login_required
def cart_update(request, product_id):
    """
    Обновление количества товара в корзине
    """
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, id=product_id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    
    quantity = int(request.POST.get('quantity', 1))
    if quantity > 0:
        cart_item.quantity = quantity
        cart_item.save()
    else:
        cart_item.delete()

    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return JsonResponse({
            'message': f'Количество товара {product.name} обновлено',
            'cart_total_items': cart.total_items,
            'cart_total_price': str(cart.total_price),
            'item_total_price': str(cart_item.total_price) if quantity > 0 else '0'
        })

    messages.success(request, f'Количество товара {product.name} обновлено')
    return redirect('cart:cart_detail') 