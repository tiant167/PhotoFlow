from .models import Picture

from rest_framework import serializers

class PictureSerialize(serializers.ModelSerializer):

    class Meta:
        model = Picture