from django.urls import path
from . import views

app_name = 'place'
urlpatterns = [
    path('place_category/', views.place_category, name='place_category'),  # 장소 카테고리 선택 화면으로 가기
    path('references/', views.references, name='references'),  # 나들이 장소 선택 화면으로 가기
    path('afterpick/', views.afterpick, name='afterpick'),  # 선택한 장소의 정보 확인하는 화면으로 가기
]