# Геометрический калькулятор

Библиотека на Python для расчёта площади и периметра круга и прямоугольника, с (unit) тестами.

## Файлы
* `circle.py` — расчёт параметров круга.
* `rectangle.py` — расчёт параметров прямоугольника.
* `test_circle.py` — unit-тесты для круга.
* `test_rectangle.py` — unit-тесты для прямоугольника.

## Описание функций

### Круг (`circle.py`)
* `area(r)` — возвращает площадь круга по радиусу `r` (($\pi r^2$).
* `perimeter(r)` — возвращает длину окружности по радиусу `r` ($2 \pi r$).

**Пример:**
```python
from circle import area, perimeter

print(area(5))       # 78.53981633974483
print(perimeter(5))  # 31.41592653589793
```

### Прямоугольник (`rectangle.py`)
* `area(a, b)` — возвращает площадь прямоугольника со сторонами `a` и `b` ($a \cdot b$).
* `perimeter(a, b)` — возвращает периметр прямоугольника со сторонами `a` и `b` ($2(a + b)$).

**Пример:**
```python
from rectangle import area, perimeter

print(area(5, 10))       # 50
print(perimeter(5, 10))  # 30
```

## Запуск тестов

Выполните в терминале в папке проекта:
```bash
python -m unittest discover
```

Успешный результат:
```text
Ran 11 tests in 0.001s

OK
```
