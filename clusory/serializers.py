from rest_framework import serializers
from django.contrib.auth.models import User

from clusory.models import Debate, Question



class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ('user', 'text', 'timestamp')


class DebateSerializer(serializers.ModelSerializer):
    user = serializers.Field(source='user')

    class Meta:
        model = Debate
        fields = ('id', 'text', 'user', 'timestamp')

    def validate_text(self, attrs, source):
        value = attrs[source]
        if len(value) < 1:
            raise serializers.ValidationError(
                "Text is too short!")
        return attrs


class UserSerializer(serializers.ModelSerializer):
    debates = DebateSerializer(many=True, source="debate_set") 

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'last_login', 'debates') 
