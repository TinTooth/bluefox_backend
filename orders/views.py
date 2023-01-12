from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Order
from .serializers import OrderSerializer
# Create your views here.s


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def get_create(request):
    if request.method == 'GET' and request.user.is_staff == True:
        result = Order.objects.all()
        serializer = OrderSerializer(result, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user= request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(status=status.HTTP_401_UNAUTHORIZED)

@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def manage(request,pk):
    result = get_object_or_404(Order,pk=pk)
    if request.method == 'GET' and request.user.is_staff == True:
        serializer = OrderSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT' and request.user.is_staff == True or request.method == 'PUT' and request.user == result.user :
        serializer = OrderSerializer(result,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE' and request.user.is_staff == True:
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_401_UNAUTHORIZED)