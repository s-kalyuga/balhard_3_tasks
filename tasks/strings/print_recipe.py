"""
ЗАДАНИЕ
--------------------------------------------------------------------------------
На вход получаем название блюда и его рецепт
Нужно вернуть результат в следующем виде, используя константы TITLE и RECIPE:
Рецепт НАЗВАНИЕ:
ингредиент1,
ингредиент2,

ПРИМЕРЫ
--------------------------------------------------------------------------------
Рецепт ОМЛЕТ:
Яйцо куриное - 5 шт,
Молоко - 100 мл,
Мука пшеничная - 0,5 ст.л.,
Соль - 0,5 ч.л.,
Масло растительное - 2 ст.л.
"""
TITLE = 'ОМЛЕТ'

RECIPE = (
    'Яйцо куриное - 5 шт',
    'Молоко - 100 мл',
    'Мука пшеничная - 0,5 ст.л.',
    'Соль - 0,5 ч.л.',
    'Масло растительное - 2 ст.л.'
)


def print_recipe() -> str:
    """Выводит рецепт в удобном виде

    :return: отформатированная строка
    :rtype: str
    """
    result = f"Рецепт {TITLE}:\n" +
    return result


if __name__ == '__main__':
    print(print_recipe())
