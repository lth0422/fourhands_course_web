from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Restaurant, SavedRestaurant

import pandas as pd

# 선택한 음식 카테고리에 맞는 음식점들을 데이터베이스에서 가져오는 함수 정의
def show_selected_restaurants(request):
    place_afterpick = request.session.get('place_afterpick')
    place_latitude = request.session.get('place_latitude')
    place_longitude = request.session.get('place_longitude')

    # 음식점 데이터를 직접 처리
    csv_path = 'restaurant/static/restaurant/Restaurant.csv'
    df = pd.read_csv(csv_path)

    # 음식 카테고리들 중 선택한 카테고리와 일치하는 음식점들 가져오기
    all_categories = ['한식', '일식', '중식', '양식', '카페', '아시아음식', '뷔페', '패스트푸드', '기타']
    selected_category = request.GET.get('category', all_categories[0])

    filtered_restaurants = df[df['category'] == selected_category]

    # 음식점 데이터베이스의 형식에 맞춰 정보 가져오기
    restaurant_objects = []
    for _, row in filtered_restaurants.iterrows():
        restaurant = Restaurant.objects.get_or_create(
            name=row['name'],
            category=row['category'],
            addr=row['addr'],
            latitude=row['latitude'],
            longitude=row['longitude']
        )[0]
        restaurant_objects.append({
            'id': restaurant.id,
            'name': row['name'],
            'category': row['category'],
            'addr': row['addr'],
            'latitude': row['latitude'],
            'longitude': row['longitude']
        })

    # 랜더 함수를 통해 인자들 restaurant_list.html로 보내기 (음식점의 이름, 위도, 경도, 주소, 네이버 api key, 나들이 장소의 이름, 위도 경도)
    return render(request, 'restaurant/restaurant_list.html', {
        'restaurants': restaurant_objects,
        'all_categories': all_categories,
        'selected_category': selected_category,
        'naver_map_api_key': 'hhiu54m7d5',
        'place_course': place_afterpick,
        'place_latitude': place_latitude,
        'place_longitude': place_longitude
    })

# 음식 카테고리 선택하는 함수 정의
def food_category(request):
    all_categories = ['한식', '일식', '중식', '양식', '카페', '아시아음식', '뷔페', '패스트푸드', '기타']
    selected_category = request.GET.get('category', all_categories[0])

    # 랜더 함수를 통해 인자를 food_category.html로 보내기
    return render(request, 'restaurant/food_category.html', {
        'all_categories': all_categories,
        'selected_category': selected_category,
    })

def show_selected_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    place_course = request.GET.get('place_course')
    place_latitude = request.GET.get('place_latitude')
    place_longitude = request.GET.get('place_longitude')

    return render(request, 'restaurant/restaurant_detail.html', {
        'restaurant': restaurant,
        'naver_map_api_key': 'hhiu54m7d5',
        'place_course': place_course,
        'place_latitude': place_latitude,
        'place_longitude': place_longitude
    })

# def show_selected_restaurant(request, restaurant_id):
#     restaurant = get_object_or_404(Restaurant, id=restaurant_id)
#     place_afterpick = request.session.get('place_afterpick')
#     place_latitude = request.session.get('place_latitude')
#     place_longitude = request.session.get('place_longitude')
#
#     return render(request, 'restaurant/restaurant_detail.html', {
#         'restaurant': restaurant,
#         'naver_map_api_key': 'hhiu54m7d5',
#         'place_course': place_afterpick,
#         'place_latitude': place_latitude,
#         'place_longitude': place_longitude
#     })


@login_required
def save_restaurant(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    place_course = request.session.get('place_afterpick')
    place_latitude = request.session.get('place_latitude')
    place_longitude = request.session.get('place_longitude')

    SavedRestaurant.objects.get_or_create(
        user=request.user,
        restaurant=restaurant,
        place_course=place_course,
        place_latitude=place_latitude,
        place_longitude=place_longitude
    )
    return redirect('restaurant:show_selected_restaurants')

@login_required()
def delete_saved_restaurant(request, saved_restaurant_id):
    saved_restaurant = get_object_or_404(SavedRestaurant, id=saved_restaurant_id, user=request.user)
    saved_restaurant.delete()
    return redirect('common:mypage', user_id=request.user.id)
