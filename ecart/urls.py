from django.contrib import admin
from django.urls import path
from mainApp import views as mainApp
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",mainApp.homepage),
    path('shop/<str:mc>/<str:sc>/<str:br>/',mainApp.shoppage),
    path('filter/<str:mc>/<str:sc>/<str:br>/<str:filter>/',mainApp.filterpage),
    path('price-filter/<str:mc>/<str:sc>/<str:br>/',mainApp.priceFilterpage),
    path('search/',mainApp.searchPage),
    path('single-product/<int:id>/',mainApp.singleproductpage), 
    path('add-to-cart/<int:num>/',mainApp.addToCartPage),
    path('remove-from-cart/<str:num>/',mainApp.removeFromCartPage),
    path('update-cart/<str:num>/<str:op>/',mainApp.updateCartPage),
    path('cart/',mainApp.cartpage),
    path('checkout/',mainApp.checkoutpage),
    path('place-order/',mainApp.placeOrderPage),
     path('paymentSuccess/<str:rppid>/<str:rpoid>/<str:rpsid>/<int:checkid>/',mainApp.paymentSuccessPage),
    path('re-payment/<int:checkid>/',mainApp.payAgainPage),
    path('confirmation/',mainApp.confirmationPage),
    path('contact/',mainApp.contactPage),
    path('login/',mainApp.loginPage),
    path('logout/',mainApp.logoutPage),
    path('signup/',mainApp.signupPage),
    path('profile/',mainApp.profilePage),
    path('update-profile/',mainApp.updatePage),
    path('add-to-wishlist/<int:num>/',mainApp.addToWishlist),
    path('remove-from-wishlist/<int:num>/',mainApp.removeFromWishlist),
    path('forget-password-1/',mainApp.forgetPasswordPage1),
    path('forget-password-2/',mainApp.forgetPasswordPage2),
    path('forget-password-3/',mainApp.forgetPasswordPage3),
    
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
