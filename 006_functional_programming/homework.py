# В переменной order храниться заказ на изготовление прямоугольных ковриков
# Для изготовления коврика используются 2 типа материалов
# 1. Материал из которого изготовлен сам коврик (площадь)
# 2. Материал из которого изготовлен кантик коврика (периметр)
# Написать программу которая считает общее количество материала на изготовление всего заказа
# carpet_material, edge_material
# Общее кол-во материала на каждый размер коврика

order = {
    'small': {'height': 40, 'width': 60, 'qty': 30},
    'medium': {'height': 70, 'width': 90, 'qty': 54},
    'large': {'height': 90, 'width': 120, 'qty': 15},
}

def area(a, b):
    return a * b


def perimeter(a, b):
    return (a + b) / 2


def material_counter(amount, material_amount):
    return material_amount * amount


def single_size(unit):
    result = {
        'total_area': material_counter(unit['qty'], area(unit['height'], unit['width'])),
        'total_perimeter': material_counter(unit['qty'], perimeter(unit['height'], unit['width'])),
    }
    return result


def total_material(order):
    result = {
        'total_carpet_material': 0,
        'total_edge_material': 0
    }
    for unit in order:
        unit_size = single_size(order[unit])
        result['total_edge_material'] += unit_size['total_perimeter']
        result['total_carpet_material'] += unit_size['total_area']
    return result


print(total_material(order))
print('Small', single_size(order['small']))
print('Medium', single_size(order['medium']))
print('Large', single_size(order['large']))