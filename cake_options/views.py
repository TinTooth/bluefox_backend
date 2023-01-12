from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import CakeOption
from .serializers import CakeOptionSerializer
# Create your views here.


@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_options(request):
    options = CakeOption.objects.all()
    serializer = CakeOptionSerializer(options, many = True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_option(request):
    if  request.user.is_staff == True:
        serializer = CakeOptionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def manage_option(request,pk):
    result = get_object_or_404(CakeOption,pk=pk)
    if request.method == 'GET' and request.user.is_staff == True:
      
        serializer = CakeOptionSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT' and request.user.is_staff == True:
       
        serializer = CakeOptionSerializer(result,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE' and request.user.is_staff == True:
      
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_401_UNAUTHORIZED)