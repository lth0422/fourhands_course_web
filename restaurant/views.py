from django.shortcuts import render
from  haversine import haversine, Unit
import pandas as pd

def show_selected_restaurants(request):
    place_afterpick = request.session.get('place_afterpick')
    place_latitude = request.session.get('place_latitude')
    place_longitude = request.session.get('place_longitude')

    # 음식점 데이터를 직접 처리
    csv_path = 'restaurant/static/restaurant/Restaurant.csv'
    df = pd.read_csv(csv_path)

    all_categories = ['한식', '일식', '중식', '양식', '카페', '아시아음식', '뷔페', '패스트푸드', '기타']
    selected_category = request.GET.get('category', all_categories[0])

    filtered_restaurants = df[df['category'] == selected_category]

    # 거리 조절 위한 함수.
    # for index, row in df.iterrows():
    #     if abs(haversine((row['latitude'],row['longitude']),(place_latitude,place_longitude))) < 5 :



    restaurant_objects = []
    for _, row in filtered_restaurants.iterrows():
        restaurant_objects.append({
            'name': row['name'],
            'category': row['category'],
            'addr': row['addr'],
            'latitude': row['latitude'],
            'longitude': row['longitude']
        })
    # place_afterpick = request.session.get('place_afterpick')
    # place_latitude = request.session.get('place_latitude')
    # place_longitude = request.session.get('place_longitude')

    return render(request, 'restaurant/restaurant_list.html', {
        'restaurants': restaurant_objects,
        'all_categories': all_categories,
        'selected_category': selected_category,
        'naver_map_api_key': 'hhiu54m7d5',
        'place_course': place_afterpick,
        'place_latitude': place_latitude,
        'place_longitude':  place_longitude
        # 'place_course': afterpick(request).place_afterpick,
        # 'place_latitude': afterpick(request).place_latitude,
        # 'place_longitude': afterpick(request).place_longitude,
    })

def food_category(request):
    all_categories = ['한식', '일식', '중식', '양식', '카페', '아시아음식', '뷔페', '패스트푸드', '기타']
    selected_category = request.GET.get('category', all_categories[0])

    return render(request, 'restaurant/food_category.html', {
        'all_categories': all_categories,
        'selected_category': selected_category,
    })