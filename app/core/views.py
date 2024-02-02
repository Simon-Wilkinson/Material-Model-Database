from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from core.models import Material
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serialisers import MaterialSerializer, MaterialNameSerializer


@api_view(['GET'])
def getMaterial(request):
    if request.method == 'GET':
        material_name = request.GET.get('material_name')
        if not material_name:
            return Response({'error': 'Material name is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        if material_name == 'all_names':
            materials = Material.objects.all()
            serialiser = MaterialNameSerializer(materials, many=True)
            return Response(serialiser.data, status=status.HTTP_200_OK)
        else:
            material = Material.objects.get(name=material_name)
            serialiser = MaterialSerializer(material)
            return Response(serialiser.data, status=status.HTTP_200_OK)
        
    else:
        return HttpResponse('Invalid request')