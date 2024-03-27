from datetime import datetime, timedelta


def get_order_product_data(serializer):

    end_date = datetime.strptime(serializer.data.get('end_date'), '%Y-%m-%d').date()
    start_date = datetime.strptime(serializer.data.get('start_date'), '%Y-%m-%d').date()

    rental_duration = (end_date - start_date).days
    rental_price = round(float(serializer.data.get('total_cost')) / rental_duration, 2)

    return rental_duration, rental_price


def count_intervals(start_date, end_date):
    interval = timedelta(days=1)
    intervals = []

    current_date = start_date
    while current_date <= end_date:
        intervals.append((current_date, current_date + interval))
        current_date += interval

    return intervals
