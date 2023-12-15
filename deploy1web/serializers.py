from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Bibik


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class BibikSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Bibik
        fields = ['imie', 'pseudonim', 'ocena1na10', 'opis']
