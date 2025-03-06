class FlowersBase:

    def __init__(self, title, color, size, is_bush_flower, blooming_season, fading_time, price):
        self.title = title
        self. color = color
        self.size = size
        self.is_bush_flower = is_bush_flower
        self.blooming_season = blooming_season
        self.price = price
        self.fading_time = fading_time  # определяется в днях

    def get_info(self):
        return ""

    def description(self):
        is_bush_flower = "кустовой" if self.is_bush_flower else "одиночный"
        get_info = self.get_info()
        return (f"цветок: {self.title}, цвет: {self.color}, размер: {self.size}, тип растения: {is_bush_flower}, "
                f"сезон цветения: {self.blooming_season}, цена: {self.price}{get_info}")


class Rose(FlowersBase):

    def __init__(self, color, size, is_bush_flower, fading_time, price, has_thorns):
        super().__init__("роза", color, size, is_bush_flower, "лето", fading_time, price)
        self.has_thorns = has_thorns

    def get_info(self):
        has_thorns = "есть шипы" if self.has_thorns else "нет шипов"
        return f", особенность: {has_thorns}"


class Tulip(FlowersBase):

    def __init__(self, color, size, is_bush_flower, fading_time, price, is_dome_shape):
        super().__init__("тюльпан", color, size, is_bush_flower, "весна", fading_time, price)
        self.is_dome_shape = is_dome_shape

    def get_info(self):
        is_dome_shape = "куполообразная форма" if self.is_dome_shape else "махровый"
        return f", особенность: {is_dome_shape}"


class Chamomile(FlowersBase):

    def __init__(self, color, size, is_bush_flower, fading_time, price, is_medicinal_properties):
        super().__init__("ромашка", color, size, is_bush_flower, "лето", fading_time, price)
        self.is_medicinal_properties = is_medicinal_properties

    def get_info(self):
        if self.is_medicinal_properties:
            is_medicinal_properties = "лечебные свойства"
            return f", особенность: {is_medicinal_properties}"
        else:
            return ""


class Bouquet:

    def __init__(self):
        self.flowers = []

    def add_flower(self, flower):
        self.flowers.append(flower)

    def total_price(self):
        return sum(flower.price for flower in self.flowers)

    def fading_time(self):
        """
        Функция считает среднее время жизни букета в днях, и возвращает целое число
        """
        return int(sum(flower.fading_time for flower in self.flowers) / len(self.flowers))

    def sort_bouquet(self, key, reverse):
        if key == 'price':
            self.flowers = sorted(self.flowers, key=lambda flower: flower.price, reverse=reverse)
        elif key == 'color':
            self.flowers = sorted(self.flowers, key=lambda flower: flower.color, reverse=reverse)
        elif key == 'size':
            self.flowers = sorted(self.flowers, key=lambda flower: flower.size, reverse=reverse)
        elif key == 'is_bush_flower':
            self.flowers = sorted(self.flowers, key=lambda flower: flower.is_bush_flower, reverse=reverse)
        elif key == 'blooming_season':
            self.flowers = sorted(self.flowers, key=lambda flower: flower.blooming_season, reverse=reverse)
        else:
            print(f"Некорректный параметр {key} для сортировки")

    def find_flowers_by_color(self, color):
        return [flower for flower in self.flowers if color.lower() == flower.color]

    def desc_bouquet(self):
        if not self.flowers:
            print("Букет пуст")
            return

        print("Состав букета:")
        for flower in self.flowers:
            print(f"- {flower.description()}")
        print(f"Общая стоимость букета: {self.total_price()} руб\nВремя затухания: {self.fading_time()} дней")


rose_1 = Rose("красный", "средний", False, 5, 350, True)
rose_2 = Rose("белый", "высокий", False, 4, 500, False)
rose_3 = Rose("розовый", "низкий", True, 7, 300, True)
tulip_1 = Tulip("белый", "средний", False, 6, 120, True)
tulip_2 = Tulip("желтый", "высокий", False, 5, 180, True)
tulip_3 = Tulip("синий", "средний", False, 3, 120, False)
chamomile_1 = Chamomile("белый", "средний", True, 7, 330, True)
chamomile_2 = Chamomile("синий", "низкий", True, 10, 270, False)

bouquet = Bouquet()
bouquet.add_flower(rose_1)
bouquet.add_flower(rose_2)
bouquet.add_flower(rose_3)
bouquet.add_flower(chamomile_1)
bouquet.add_flower(chamomile_2)
bouquet.desc_bouquet()

print("\nСортировка по цене (по убыванию):")
bouquet.sort_bouquet("price", True)
bouquet.desc_bouquet()

print("\nСортировка по цвету (А-Я):")
bouquet.sort_bouquet("color", False)
bouquet.desc_bouquet()

found_flowers = bouquet.find_flowers_by_color("Белый")
print("\nЦветы белого цвета:")
for f in found_flowers:
    print(f"- {f.description()}")
