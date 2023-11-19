from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import ChatRoom, Message
from .serializers import ChatRoomSerializer, MessageSerializer


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    # permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     chatroom = serializer.save(created_by=self.request.user, admin=self.request.user)
    #     chatroom.participants.add(self.request.user)


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    # permission_classes = [IsAuthenticated]

    # def perform_create(self, serializer):
    #     serializer.save(sender=self.request.user)


def index(request):
    return render(request, 'chat/index.html')


