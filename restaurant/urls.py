from django.urls import path
from .views import show_selected_restaurants, food_category

app_name = 'restaurant'
urlpatterns = [

    path('food_category/', food_category, name='food_category'),   # url 뒤에 food_category가 붙으면 food_category 함수 참조하여 fodd_category.html로 가기
    path('show_selected_restaurants/', show_selected_restaurants, name='show_selected_restaurants'),    # url 뒤에 show_selected_restaurants가 붙으면 show_selected_restaurants 함수 참조하여 restaurant.html로 가기
]

