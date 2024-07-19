from django.urls import path
from .views import show_selected_restaurants, food_category, save_restaurant, show_selected_restaurant, delete_saved_restaurant

app_name = 'restaurant'
urlpatterns = [
    path('delete_saved_restaurant/<int:saved_restaurant_id>/', delete_saved_restaurant, name='delete_saved_restaurant'),
    path('save_restaurant/<int:restaurant_id>/', save_restaurant, name='save_restaurant'),
    path('show_selected_restaurant/<int:restaurant_id>/', show_selected_restaurant, name='show_selected_restaurant'),
    # 다른 URL 패턴들...
    path('food_category/', food_category, name='food_category'),   # url 뒤에 food_category가 붙으면 food_category 함수 참조하여 fodd_category.html로 가기
    path('show_selected_restaurants/', show_selected_restaurants, name='show_selected_restaurants'),    # url 뒤에 show_selected_restaurants가 붙으면 show_selected_restaurants 함수 참조하여 restaurant.html로 가기
]

