from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .models import OrderItem
from .serializers import OrderItemSerializer, OrderItemPostSerializer
# Create your views here.


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all_byOrder(request,order_pk):
    if request.user.is_staff == True:
        result = OrderItem.objects.filter(order_id = order_pk)
        serializer = OrderItemSerializer(result, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_all(request,order_pk):
    if request.user.is_staff == True:
        result = OrderItem.objects.all()
        serializer = OrderItemSerializer(result, many = True)
        return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create(request,order_pk):
    serializer = OrderItemPostSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT','DELETE'])
@permission_classes([IsAuthenticated])
def manage(request,pk,order_pk):
    result = get_object_or_404(OrderItem,pk=pk)
    if request.method == 'GET' and request.user.is_staff == True:
        serializer = OrderItemSerializer(result)
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'PUT' and request.user.is_staff == True:
        serializer = OrderItemSerializer(result,data = request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    if request.method == 'DELETE' and request.user.is_staff == True:
        result.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    return Response(status=status.HTTP_401_UNAUTHORIZED)

# Create your views here.
