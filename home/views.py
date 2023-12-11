from django.shortcuts import render

# 랜더 함수를 통해 home 화면 출력
def home(request):
    return render(request,'home/home.html')
