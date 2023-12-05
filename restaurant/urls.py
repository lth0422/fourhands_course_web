from django.urls import path
from .views import show_selected_restaurants, food_category

app_name = 'restaurant'
urlpatterns = [

    path('food_category/', food_category, name='food_category'),
    path('show_selected_restaurants/', show_selected_restaurants, name='show_selected_restaurants'),
]

