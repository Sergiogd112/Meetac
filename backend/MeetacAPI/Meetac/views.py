from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def apiOverview(request):
    api_urls={
        'List':'/list/',
        'Detail View':'/detail/<str:pk>',
        'Graph':'/graph'
    }
    return Response(api_urls)

@api_view(['GET'])
def get_graph(request):
    return Response({})