# accounts/urls.py

from django.urls import path
from .views import (
    signup,
    login_view,
    home,
    logout_view,
    men_view,        # Import the men_view
    women_view,
    kids_view,
    personalize_view,
    sales_view,
    trending_view,
    brands_view,
    product1,
    product2,
    product3,
    product4,
    product5,
    product6,
)
app_name = 'accounts'

urlpatterns = [
    path('', home, name='home'),  # Home page
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('home/', home, name='home'),  # Home page
    path('logout/', logout_view, name='logout'),
    path('men/', men_view, name='men'),  # Ensure this line is present
    path('women/', women_view, name='women'),  # Ensure this line is present
    path('kids/', kids_view, name='kids'),  # Ensure this line is present
    path('personalize/', personalize_view, name='personalize'),  # Personalize page
    path('sales/', sales_view, name='sales'),  # Sales page
    path('trending/', trending_view, name='trending'),  # Trending page
    path('brands/', brands_view, name='brands'),
    path('product1/', product1, name='product1'),

]