def update_sale_price(car, sale_price):
    if car['sold'] is True:
        raise Exception("Car has already been sold.")
    car['sale_price'] = sale_price


def create_car(description, cost, sale_price, condition):
    return {
        'description': description,
        'cost': cost,
        'sale_price': sale_price,
        'condition': condition,
        'sold': False
    }


def sell(car, sold_for=None):
    if sold_for:
        update_sale_price(car, sold_for)
    car['sold'] = True
    profit = car['sale_price'] - car['cost']
    return profit

car = create_car('Jeep Renegade', 100, 150, 0.5)

update_sale_price(car, 350)

print(sell(car))
