from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
from decouple import config
from .models import Chat
from django.utils import timezone
from asgiref.sync import sync_to_async
import asyncio

openai_api_key = config('GPT_KEY')
client = OpenAI(api_key=openai_api_key)


async def ask_openai(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Вы полезный ассистент."},
            {"role": "user", "content": message},
        ],
    )

    answer = response.choices[0].message.content.strip()
    print(answer)
    return answer


@sync_to_async
def save_chat(user, message, response):
    chat = Chat(user=user, message=message, response=response, created_at=timezone.now())
    chat.save()


async def handle_chat(request):
    chats = await sync_to_async(Chat.objects.filter)(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = await ask_openai(message)

        await save_chat(request.user, message, response)

        return JsonResponse({'message': message, 'response': response})

    return render(request, 'chatbot.html', {'chats': chats})


async def chatbot(request):
    return await handle_chat(request)
