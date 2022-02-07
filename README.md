# uni-size
Написать декоратор класса под названием sizer, который будет добавлять в класс поле size. При обращении к этому полю возвращается len() объекта, если объёкт имеет длину, иначе же abs() объекта, если от него вычисляется модуль, и 0 в противном случае.

Input:
```
@sizer
class S(str):
    pass

@sizer
class N(complex):
    pass

@sizer
class E(Exception):
    pass

for obj in S("QWER"), N(3+4j), E("Exceptions know no lengths!"):
    print(obj, obj.size)
```

Output:
```
QWER 4
(3+4j) 5.0
Exceptions know no lengths! 0
```
