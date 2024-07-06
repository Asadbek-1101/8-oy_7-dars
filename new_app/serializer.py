from rest_framework import serializers
from .models import Header, BigHeader, Services, Oportunities, About, SocialMedia, Comments

class HeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Header
        fields = '__all__'

class BigHeaderSerializer(serializers.ModelSerializer):
    class Meta:
        model = BigHeader
        fields = '__all__'

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'

class OportunitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Oportunities
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class SocialMediaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMedia
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = '__all__'









