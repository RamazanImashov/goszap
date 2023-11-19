from rest_framework import serializers
from .models import ChatRoom, Message


class MessageSerializer(serializers.ModelSerializer):
    sender = serializers.ReadOnlyField(source='sender.email')

    class Meta:
        model = Message
        fields = ('chatroom', 'text', 'timestamp', 'sender')

    def create(self, validated_data):
        user = self.context['request'].user
        messag = Message.objects.create(sender=user, **validated_data)
        return messag


class ChatRoomSerializer(serializers.ModelSerializer):
    admin = serializers.ReadOnlyField(source='admin.email')
    # participants = serializers.ReadOnlyField(source='participants.email')
    messages = MessageSerializer(many=True, read_only=True)

    class Meta:
        model = ChatRoom
        fields = ('id', 'admin', 'title', 'participants', 'created_at', 'messages')

    def create(self, validated_data):
        user = self.context['request'].user
        participants_data = validated_data.pop('participants', [])
        chatroom = ChatRoom.objects.create(created_by=user, admin=user, **validated_data)
        chatroom.participants.add(user)
        chatroom.participants.set(participants_data)
        return chatroom
