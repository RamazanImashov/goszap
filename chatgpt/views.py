from django.shortcuts import render
from django.http import JsonResponse
from openai import OpenAI
from decouple import config
from .models import Chat
from django.utils import timezone
import asyncio

openai_api_key = config('GPT_KEY')
client = OpenAI(api_key=openai_api_key)


async def ask_openai(message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": message},
        ])

    answer = response.choices[0].message.content.strip()
    print(answer)
    return answer


async def handle_chat(request):
    chats = Chat.objects.filter(user=request.user)

    if request.method == 'POST':
        message = request.POST.get('message')
        response = await ask_openai(message)

        chat = Chat(user=request.user, message=message, response=response, created_at=timezone.now())
        chat.save()
        return JsonResponse({'message': message, 'response': response})

    return render(request, 'chatbot.html', {'chats': chats})


def chatbot(request):
    loop = asyncio.get_event_loop()
    return loop.run_until_complete(handle_chat(request))

