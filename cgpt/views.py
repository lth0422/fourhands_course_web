from django.shortcuts import render 
from django.http import JsonResponse 
from .forms import Userform


from django.shortcuts import render 
from django.http import JsonResponse 
from .forms import Userform
from .utils import create_thread_and_run, get_latest_message

def cgpt(request):
    form = Userform()
    return render(request, 'cgpt/cgpt.html', {'form': form})

def recommend_keyword(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        run, thread_id = create_thread_and_run(user_input)
        
        if run.status == 'completed':
            latest_message = get_latest_message(thread_id)
            if latest_message:
                try:
                    recommend_reason, keywords_string = latest_message.split('@')
                    return JsonResponse({
                        'recommend_reason': recommend_reason,
                        'keywords_string': keywords_string,
                    })
                except ValueError:
                    return JsonResponse({
                        'error': f"Invalid Response: {latest_message}"
                    })
            return JsonResponse({'error': "No valid response received from assistant"})
        else:
            return JsonResponse({'error': f"Run Status: {run.status}, Details: {run}"})
    else:
        return JsonResponse({'error': 'Invalid request method'})
