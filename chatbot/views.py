from django.shortcuts import render
from django.http import JsonResponse
import google.generativeai as genai
from django.conf import settings
from .models import ChatMessage

genai.configure(api_key=settings.GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-pro')

def home(request):
    if request.method == 'POST':
        message = request.POST.get('message')
        response = model.generate_content(message)
        
        # Save to database
        chat = ChatMessage.objects.create(
            message=message,
            response=response.text
        )
        
        return JsonResponse({
            'response': response.text
        })
    
    return render(request, 'chatbot.html')