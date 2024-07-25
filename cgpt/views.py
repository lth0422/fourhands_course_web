from django.shortcuts import render 
from django.http import JsonResponse 
from .forms import Userform
from .utils import create_thread_and_run, get_latest_message

def cgpt(request):
    form = Userform()
    return render(request, 'cgpt/cgpt.html', {'form': form})

def handle_error(message):
    return JsonResponse({'error': message})

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
        if not keywords_string or keywords_string == "[]":
            return handle_error(recommend_reason)
        return JsonResponse({
            'recommend_reason': recommend_reason,
            'keywords_string': keywords_string,
        })
    except ValueError:
        return handle_error(latest_message)
