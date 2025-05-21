"""
URL configuration for otaku_store project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.core.urls', namespace='core')),
    path('products/', include('apps.products.urls', namespace='products')),
    path('cart/', include('apps.cart.urls', namespace='cart')),
    # path('orders/', include('apps.orders.urls', namespace='orders')),
    path('users/', include('apps.users.urls', namespace='users')),
    path('accounts/', include('allauth.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)