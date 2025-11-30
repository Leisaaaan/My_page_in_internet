# Тут будет жить Python. Он не знает об интернете и заведует логикой внутри
class Service:

    def __init__(self):
        self.useful_materials_db = [
            {"title" : "Постановление 1", "Год" : 2024},
            {"title": "Постановление 2", "Год": 2025},
        ]

    # Метод, которые возвращает все материалы
    def get_all_materials(self):
        return self.useful_materials_db



service = Service()