relationships = [7, 4, 9]  # массив с relationships
relation_relationships = [3, 7, 9]  # БД

c = set([])

def func():
    for relationship in relationships:
        for row in relation_relationships:
            if row == relationship:
                print(relationship, " этот элемент в массиве - это обновление записей в БД")
                break
            if row != relationship and row is relation_relationships[-1]:
                print(relationship, " этого элемента нет в массиве - это добавление записей в БД")


func()
print(*relationships)


# 4 этот элемент есть в массиве
# 5 этого элемента нет в массиве
# 7 этого элемента нет в массиве
# удалить элемент 9 в массиве b