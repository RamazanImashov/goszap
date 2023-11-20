from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
from decouple import config
from .models import Chat
from django.utils import timezone


openai_api_key = config('GPT_KEY')
client = OpenAI(api_key=openai_api_key)


def ask_openai(message):
    response = client.chat.completions.create(model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are an helpful assistant."},
        {"role": "user", "content": message},
    ])

    answer = response.choices[0].message.content.strip()
    print(answer)
    return answer


def chatbot(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})
    return render(request, 'chatbot.html', {'chats': chats})
