from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render, redirect, get_object_or_404
from common.forms import UserForm
from restaurant.models import SavedRestaurant



def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)  # 사용자 인증
            login(request, user)  # 로그인
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'common/signup.html', {'form': form})

# def mypage(request, user_id):
#     context = {
#         'user_id': user_id
#     }
#     return render(request, 'common/mypage.html', context)

def mypage(request, user_id):
    user = get_object_or_404(get_user_model(), id=user_id)
    saved_restaurants = SavedRestaurant.objects.filter(user=user)
    context = {
        'user': user,
        'saved_restaurants': saved_restaurants,
    }
    return render(request, 'common/mypage.html', context)