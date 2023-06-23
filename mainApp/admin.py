from django.contrib import admin
from .models import *


admin.site.register((maincategory,subcategory,Brand,product,Buyer,Wishlist,Checkout,CheckoutProduct,Contact))
