from collections import defaultdict

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

class User:
    def __init__(self, login, money=0):
        self.login = login
        self.__balance = money

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        self.__balance = amount

    def __str__(self):
        return f'Пользователь {self.login}, баланс - {self.balance}'

    def deposit(self, money):
        self.__balance += money  # Добавляем средства к текущему балансу

    def is_money_enough(self, money):
        return self.balance >= money

    def payment(self, money):
        if self.is_money_enough(money):
            self.balance -= money  # Правильное вычитание из баланса
            return True  # Возвращаем True для успешной оплаты
        else:
            print(f'Не хватает средств на балансе. Пополните счет')
            return False  # Возвращаем False для неуспешной оплаты

class Cart:
    def __init__(self, user):
        self.user = user
        self.goods = defaultdict(int)  # Словарь для хранения товаров и их количества
        self.__total = 0  # Защищенный атрибут для хранения итоговой суммы

    def add(self, product, quantity=1):
        self.goods[product] += quantity  # Увеличиваем количество товара
        self.__total += product.price * quantity  # Пересчитываем общую сумму

    def remove(self, product, quantity=1):
        if product in self.goods:
            if self.goods[product] >= quantity:
                self.goods[product] -= quantity  # Уменьшаем количество товара
                self.__total -= product.price * quantity  # Пересчитываем общую сумму
                if self.goods[product] == 0:
                    del self.goods[product]  # Удаляем товар, если его количество стало 0
            else:
                # Уменьшаем количество товара до 0 и пересчитываем общую сумму
                total_removal_price = product.price * self.goods[product]
                self.__total -= total_removal_price
                del self.goods[product]  # Удаляем товар
        else:
            print("Товар не найден в корзине.")

    @property
    def total(self):
        return self.__total

    def order(self):
        if self.user.payment(self.__total):
            print("Заказ оплачен")
            self.goods.clear()  # Очищаем корзину после успешной оплаты
            self.__total = 0  # Сбрасываем общую сумму
        else:
            print("Проблема с оплатой")

    def print_check(self):
        print("---Your check---")
        for product in sorted(self.goods.keys(), key=lambda p: p.name):
            quantity = self.goods[product]
            total_price = product.price * quantity
            print(f"{product.name} {product.price} {quantity} {total_price}")
        print(f"---Total: {self.total}---")


# Пример использования
billy = User('billy@rambler.ru')

lemon = Product('lemon', 20)
carrot = Product('carrot', 30)

cart_billy = Cart(billy)
print(cart_billy.user)  # Пользователь billy@rambler.ru, баланс - 0

# Добавляем товары в корзину
cart_billy.add(lemon, 2)
cart_billy.add(carrot, 1)
cart_billy.print_check()
# Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 2 40
# ---Total: 70---

cart_billy.add(lemon, 3)
cart_billy.print_check()
# Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 5 100
# ---Total: 130---

cart_billy.remove(lemon, 6)
cart_billy.print_check()
# Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# ---Total: 30---

print(cart_billy.total)  # 30

cart_billy.add(lemon, 5)
cart_billy.print_check()
# Печатает текст ниже
# ---Your check---
# carrot 30 1 30
# lemon 20 5 100
# ---Total: 130---

cart_billy.order()
# Печатает текст ниже
# Не хватает средств на балансе. Пополните счет
# Проблема с оплатой

cart_billy.user.deposit(150)  # Пополнение баланса
cart_billy.order()  # Заказ оплачен
print(cart_billy.user.balance)  # 20

