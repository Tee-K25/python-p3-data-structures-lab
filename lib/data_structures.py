spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    return [food["name"] for food in spicy_foods]


def get_spiciest_foods(spicy_foods):
    return [food for food in spicy_foods if food["heat_level"]>5]


def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat = "🌶" * food['heat_level']
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")


def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if  cuisine == food['cuisine']:
            return dict(food)

def print_spiciest_foods(spicy_foods):
        for food in spicy_foods:
            heat = "🌶" * food['heat_level']
            if food["heat_level"] > 5:
                print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat}")

def get_average_heat_level(spicy_foods):
    all_elements = len(spicy_foods)
    total_heat_level=0
    for food in spicy_foods:
        total_heat_level += food["heat_level"]
    return total_heat_level/all_elements

def create_spicy_food(spicy_foods, spicy_food):
        spicy_foods.append(spicy_food)
        return spicy_foods
