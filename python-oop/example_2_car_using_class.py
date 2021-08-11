class Car:
    def __init__(self, description, cost, sale_price, condition):
        self.description = description
        self.cost = cost
        self.sale_price = sale_price
        self.condition = condition

    def sell(self, sold_for=None):
        if sold_for:
            self.update_sale_price(sold_for)
        self.sold = True
        self.profit = self.sale_price - self.cost
        return self.profit

    def update_sale_price(self, sale_price):
        if self.sold:
            raise Exception("Car has already been sold.")
        self.sale_price = sale_price


from example_2_car_using_class import Car

if __name__ == "__main__":
    car = Car('Jeep Renegade', 100, 150, 0.5)
    car.sell(300)
    print(car.profit)
