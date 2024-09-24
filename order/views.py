from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework import status

from product.models import Product
from .serializers import OrderSerializer
from .models import Order, OrderItem


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_orders(request):
    orders = Order.objects.all()
    serializer = OrderSerializer(orders, many=True)
    return Response({'orders': serializer.data})


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    serializer = OrderSerializer(order, many=False)
    return Response({'order': serializer.data})


@api_view(['PUT'])
@permission_classes([IsAuthenticated, IsAdminUser])
def process_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    status_value = request.data.get('status')
    if status_value is None:
        return Response({'error': 'Status is required'}, status=status.HTTP_400_BAD_REQUEST)

    order.status = status_value
    order.save()

    serializer = OrderSerializer(order, many=False)
    return Response({'order': serializer.data})


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_order(request, pk):
    order = get_object_or_404(Order, id=pk)
    order.delete()
    return Response({'details': "Order has been deleted"}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_order(request):
    user = request.user
    data = request.data
    order_items = data.get('order_Items', [])

    if not order_items:
        return Response({'error': 'No order received'}, status=status.HTTP_400_BAD_REQUEST)

    total_amount = 0
    order = Order.objects.create(
        user=user,
        city=data['city'],
        zip_code=data['zip_code'],
        street=data['street'],
        phone_no=data['phone_no'],
        country=data['country'],
        total_amount=0,  
    )

    for item in order_items:
        product = get_object_or_404(Product, id=item['product'])
        quantity = item['quantity']
        price = product.price  
        item_total = price * quantity
        total_amount += item_total

        OrderItem.objects.create(
            product=product,
            order=order,
            name=product.name,
            quantity=quantity,
            price=price 
        )
        
        product.stock -= quantity
        product.save()

    order.total_amount = total_amount
    order.save()

    serializer = OrderSerializer(order, many=False)
    return Response(serializer.data, status=status.HTTP_201_CREATED)
