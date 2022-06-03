from django.urls import path

from products.views import ProductView,SearchView

app_name = 'products'

urlpatterns = [
    # path('', ProductDetailView.as_view(),name='detail')
    path('', ProductView.as_view(),name='list'),

]