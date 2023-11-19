from django.shortcuts import render
from django.http import JsonResponse
import openai
from decouple import config
from .models import Chat
from django.utils import timezone


openai_api_key = config('GPT_KEY')
openai.api_key = openai_api_key


def ask_openai(message):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an helpful assistant."},
            {"role": "user", "content": message},
        ]
    )

    answer = response.choices[0].message.content.strip()
    print(answer)
    return answer


def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)
        user = request.user
        chat = Chat(user=user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats})
