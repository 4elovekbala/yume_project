from datetime import datetime

from django.db.models import Sum, ExpressionWrapper, F, DecimalField
from rest_framework import generics, status
from rest_framework.response import Response

from .models import Order, OrderProduct, Product
from .serializers import OrderSerializer, OrderProductSerializer, ProductSerializer
from .utils import get_order_product_data, count_intervals


class OrderListView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):

        if OrderProduct.objects.filter(product_id__in=request.data.get('products', [])).exists():
            return Response({"error": "Product is already rented."}, status=status.HTTP_400_BAD_REQUEST)

        if Order.objects.filter(start_date__lt=request.data.get('end_date'),
                                end_date__gt=request.data.get('start_date'),
                                products__id__in=request.data.get('products', [])).exists():
            return Response({"error": "Product has overlapping rental periods."},
                            status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

    def perform_create(self, serializer):
        instance = serializer.save()

        rental_duration, rental_price = get_order_product_data(serializer=serializer)

        products = Product.objects.filter(id__in=serializer.data.get('products'))

        for product in products:
            OrderProduct.objects.create(order=instance, product=product, rental_price=rental_price,
                                        rental_duration=rental_duration)


class OrderDetailView(generics.RetrieveDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductListView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderProductDetailView(generics.RetrieveAPIView):
    queryset = OrderProduct.objects.all()
    serializer_class = OrderProductSerializer
    lookup_url_kwarg = 'order_product_pk'


class StatisticView(generics.ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def get(self, request, *args, **kwargs):
        start_interval_date = request.data.get('start_date', datetime(2024, 3, 1))
        end_interval_date = request.data.get('end_date', datetime(2024, 4, 8))

        total_rental_cost = OrderProduct.objects.filter(
                                                        order__start_date__gte=start_interval_date,
                                                        order__end_date__lte=end_interval_date
                                                    ).values(
                                                        'order__start_date',
                                                        'order__end_date',
                                                        'product__name',
                                                        'product_id'
                                                    ).annotate(
                                                        total_cost=ExpressionWrapper(
                                                            Sum(F('rental_price') * F('rental_duration')),
                                                            output_field=DecimalField()
                                                        )
                                                    )

        intervals = count_intervals(start_interval_date, end_interval_date)

        unrented_intervals = []

        for interval_start, interval_end in intervals:
            rented_products = OrderProduct.objects.filter(
                order__start_date__lte=interval_end,
                order__end_date__gte=interval_start
            ).values_list('product_id', flat=True)

            all_products = Product.objects.values_list('id', flat=True)

            unrented_products = set(all_products) - set(rented_products)

            if unrented_products:
                unrented_intervals.append({
                    'start_date': interval_start.strftime('%Y.%m.%d'),
                    'end_date': interval_end.strftime('%Y.%m.%d'),
                    'unrented_products': list(unrented_products)
                })

        return Response(
                        {
                         'start_date': start_interval_date.strftime('%Y.%m.%d'),
                         'end_date': end_interval_date.strftime('%Y.%m.%d'),
                         'total_cost': total_rental_cost,
                         'unrented_intervals': unrented_intervals
                        }, status=status.HTTP_200_OK
                       )


