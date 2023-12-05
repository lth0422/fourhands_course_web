import pandas as pd
from django.shortcuts import render, redirect
from .models import PlaceModel

def place_category(request):
    place_categories = ['거리&골목길',
                        '건축물',
                        '공원',
                        '궁궐',
                        '광화문&종로',
                        '다리',
                        '산',
                        '서촌&북촌',
                        '식물',
                        '역사 문화 공간',
                        '자연산책로',
                        '캠퍼스',
                        '야경&전망',
                        '테마파크',
                        '한강'
                        ]

    if request.method == 'POST':
        selected_place_categories = request.POST.getlist('place_categories')
        print(selected_place_categories)
        # Save selected categories in session
        if len(selected_place_categories) > 2:
            error_message = "최대 2개의 테마를 선택할 수 있습니다. 다시 선택해주세요."
            return render(request, 'place/place_category.html', {'place_categories': place_categories, 'error_message': error_message})
        else:
            request.session['selected_place_categories'] = selected_place_categories
            return redirect('/place/references')  # Redirect to references page

    return render(request, 'place/place_category.html', {'place_categories': place_categories})

# def references(request):
#     # Retrieve selected categories from session
#     selected_categories = request.session.get('selected_categories', [])

#     return render(request, 'references.html', {'selected_categories': selected_categories})

def references(request):
    # CSV 파일 경로 설정 (예: media 폴더 안에 있는 파일)
    csv_file_path = 'place/static/place/PlaceList.csv'

    # CSV 파일을 pandas DataFrame으로 읽기
    df = pd.read_csv(csv_file_path, encoding='UTF-8')

    print(df.columns)


    # DataFrame을 순회하며 Django 모델에 데이터 저장
    for index, row in df.iterrows():
        PlaceModel.objects.create(
            name=row['출사 장소 리스트'],
            attribute1=row['거리&골목길'],
            attribute2=row['건축물'],
            attribute3=row['공원'],
            attribute4=row['광화문&종로'],
            attribute5=row['궁궐'],
            attribute6=row['다리'],
            attribute7=row['산'],
            attribute8=row['서촌&북촌'],
            attribute9=row['식물'],
            attribute10=row['역사 문화 공간'],
            attribute11=row['자연산책로'],
            attribute12=row['캠퍼스'],
            attribute13=row['야경&전망'],
            attribute14=row['테마파크'],
            attribute15=row['한강'],
            latitude=row['위도'],
            longitude=row['경도'],
            address=row['주소'],
            # ... (one-hot 벡터에 해당하는 각 속성에 대한 필드 추가)
        )

    selected_place_categories = request.session.get('selected_place_categories', [])
    print(selected_place_categories)

    # Filter DataFrame based on selected categories

    if len(selected_place_categories) == 1:
        recommended_place = df[df[selected_place_categories[0]] == 1]['출사 장소 리스트'].tolist()

        if request.method == 'POST':
            place_afterpick = request.POST.get('place_afterpick')
            print(place_afterpick)

            request.session['place_afterpick'] = place_afterpick
            return redirect('/place/afterpick')  # Redirect to references page


        return render(request, 'place/recommended_place.html', {'recommended_place': recommended_place,'naver_map_api_key': 'hhiu54m7d5'})


    if len(selected_place_categories) == 2:
        recommended_place = df[(df[selected_place_categories[0]] == 1)&(df[selected_place_categories[1]] == 1)]['출사 장소 리스트'].tolist()
        recommended_place1T = df[(df[selected_place_categories[0]] == 1)&(df[selected_place_categories[1]] != 1)]['출사 장소 리스트'].tolist()
        recommended_place2T = df[(df[selected_place_categories[0]] != 1)&(df[selected_place_categories[1]] == 1)]['출사 장소 리스트'].tolist()

        if request.method == 'POST':
            place_afterpick = request.POST.get('place_afterpick')
            # Save selected categories in session
            request.session['place_afterpick'] = place_afterpick
            return redirect('/place/afterpick')  # Redirect to references page

        return render(request, 'place/recommended_place.html', {'recommended_place': recommended_place, 'recommended_place1T': recommended_place1T, 'recommended_place2T': recommended_place2T,  'naver_map_api_key': 'hhiu54m7d5'})


def afterpick(request):
    place_afterpick = request.session.get('place_afterpick')

    # 선택한 장소의 위도 및 경도 정보 검색
    selected_place_info = PlaceModel.objects.filter(name=place_afterpick).first()

    # 위도 및 경도를 템플릿으로 전달
    return render(request, 'place/afterpick.html', {'place_afterpick': place_afterpick, 'latitude': selected_place_info.latitude, 'longitude': selected_place_info.longitude})


# Create your views here.
