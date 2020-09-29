from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import MeetacUser, Tag, Graph_history, Message


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/list/',
        'Detail View': '/detail/<str:pk>',
        'Graph': '/graph',
        'Tags List': '/tags',
        'Detail Tag': '/tag/<str:pk>'
    }
    return Response(api_urls)


@api_view(['GET'])
def get_graph(request):
    return Response({})
