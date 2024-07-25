import json
from django.shortcuts import render 
from django.http import JsonResponse 
from .forms import Userform
from .utils import create_thread_and_run, get_latest_message

VALID_KEYWORDS = [
  '거리&골목길', '건축물', '공원', '궁궐', '광화문&종로', '다리', '산', '서촌&북촌', '식물', 
  '역사 문화 공간', '자연산책로', '캠퍼스', '야경&전망', '테마파크', '한강'
]

def cgpt(request):
  form = Userform()
  return render(request, 'cgpt/cgpt.html', {'form': form})

def handle_error(message):
  return JsonResponse({'error': message})

def filter_valid_keywords(keywords_string):
  try:
    # JSON 형식의 문자열로 파싱
    keywords = json.loads(keywords_string)
    # 유효한 키워드만 필터링
    filtered_keywords = [keyword for keyword in keywords if keyword in VALID_KEYWORDS]
    return filtered_keywords
  except json.JSONDecodeError:
      return []

def recommend_keyword(request):
    if request.method != 'POST':
      return handle_error('Invalid request method')
    
    user_input = request.POST.get('user_input')
    run, thread_id = create_thread_and_run(user_input)
    
    if run.status != 'completed':
      return handle_error(f"Run Status: {run.status}, Details: {run}")
    
    latest_message = get_latest_message(thread_id)
    if not latest_message:
      return handle_error("No valid response received from assistant")
    
    try:
      recommend_reason, keywords_string = latest_message.split('@')
      # 유효한 키워드만 필터링
      filtered_keywords = filter_valid_keywords(keywords_string)
      print(filtered_keywords)
      if not filtered_keywords or len(filtered_keywords) == 0:
        return handle_error(recommend_reason)

      return JsonResponse({
          'recommend_reason': recommend_reason,
          'keywords_string': filtered_keywords,
      })
    except ValueError:
      return handle_error(latest_message)
