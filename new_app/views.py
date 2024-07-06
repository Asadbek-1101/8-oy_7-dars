from django.shortcuts import render

from rest_framework.generics import RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAdminUser

from .models import Header, BigHeader, Services, Oportunities, About, SocialMedia, Comments
from.serializer import HeaderSerializer, BigHeaderSerializer, ServicesSerializer, OportunitiesSerializer, AboutSerializer, SocialMediaSerializer, CommentsSerializer


class HeaderView(RetrieveAPIView):
    queryset = Header.objects.all()
    serializer_class = HeaderSerializer
    permission_classes = []