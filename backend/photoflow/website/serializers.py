from .models import Website

from rest_framework import serializers

class WebsiteSerialize(serializers.ModelSerializer):

    class Meta:
        model = Website