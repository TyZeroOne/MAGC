# import random


def add_points(x0, y0, x1, y1, p, a=0):
    if x0 == -1:
        return (x1, y1)
    if x1 == -1:
        return (x0, y0)
    
    # Приведение координат к диапазону от 0 до p-1
    x0, y0 = x0 % p, y0 % p
    x1, y1 = x1 % p, y1 % p
    
    if x0 == x1 and y0 == y1:
        
        if y0 == 0:
            print("x1 == x2, y1 == y2 == 0:")
            # Точка на бесконечности (удвоение точки, у которой y = 0)
            return -1, -1
        print("x1 == x2, y1 == y2 != 0:")
        # Вычисление λ для удвоения точки
        numerator = (3 * x0 ** 2 + a) % p
        denominator = (2 * y0) % p
        lambda_ = (numerator * pow(denominator, -1, p)) % p
        print(f"    l = (3x1**2 + a) / 2y1) mod (p) = (3*{x1} ** 2  + {a}) / 2 * {y1}) mod ({p}) = {lambda_}")
    else:

        if x0 == x1:
            # Если x0 = x1, а y0 != y1, то это точка на бесконечности
            return -1, -1
        print("x1 != x2:")
        numerator = (y1 - y0) % p
        denominator = (x1 - x0) % p
        lambda_ = (numerator * pow(denominator, -1, p)) % p
        print(f"    l = (y1 - y2 / x1 - x2) mod (p) = ({y0} - {y1} / {x0} - {x1}) mod ({p}) = {lambda_}")
        
        print(f"    l = {lambda_}")

    x2 = (lambda_ ** 2 - x0 - x1) % p
    y2 = (lambda_ * (x0 - x2) - y0) % p

    print(f"    x3 = l^2 - x1 - x2 (mod p) => {lambda_}^2 - {x0} - {x1} (mod {p})")
    print(f"    y3 = l*(x1 - x3) - y1 (mod p) => {lambda_}*({x0} - {x2}) - {y0} (mod {p})")
    print(f"    x3 = {x2}, y = {y2}")

    return x2, y2

print(add_points(1,7,6,7,11,1))
def main(x1, y1, p, a):
    x2 = x1
    y2 = y1
    count = 1  # Начинаем с 1, так как первая точка уже включена
    
    while (x2, y2) != (-1, -1):
        print(f"Шаг {count}: Точка P = {x2, y2} Вычислим {count + 1}*P = {x2, y2} + {x1, y1}")
        x2, y2 = add_points(x2, y2, x1, y1, p, a)
        count += 1  # Правильное увеличение счетчика
    
    print("Порядок:", count)
main(7, 1, 11, 1)
# def summ(x0, y0, x1, y1, p, A):
#     if x0 == x1 and y0 == y1:
#         a = A
#         print(f"{l} = 3 * {x0}^2 + {a} * 2 * {}")
#         l = (3 * pow(x0, 2, p) + a) * pow(2 * y0, -1, p) % p
#         x3 = (pow(l, 2, p) - 2 * x0) % p
#         y3 = (l * (x0 - x3) - y0) % p    
#     elif x0 != x1 or y0 != y1:  
#         l = (y1 - y0) * pow(x1 - x0, -1, p) % p
#         x3 = (pow(l, 2, p) - x1 - x0) % p
#         y3 = (l * (x0 - x3) - y0) % p
#     return x3, y3

# x3, y3 = summ(2, 5, 2, 5, 11, 5)
# print(x3, y3)
# x3, y3 = summ(2, 5, x3, y3, 11, 5)
# print(x3, y3)
# x3, y3 = summ(2, 5, x3, y3, 11, 5)
# print(x3, y3)
# x3, y3 = summ(2, 5, x3, y3, 11, 5)
# print(x3, y3)

# def legendre_symbol(a, p):
#     return pow(a, (p - 1) // 2, p)

# def tonelli_shanks(a, p):
#     if legendre_symbol(a, p) != 1:
#         return None  
#     if p % 4 == 3:
#         return pow(a, (p + 1) // 4, p)
#     s = 0
#     q = p - 1
#     while q % 2 == 0:
#         s += 1
#         q //= 2
#     z = 2
#     while legendre_symbol(z, p) != p - 1:
#         z += 1
#     m = s
#     c = pow(z, q, p)
#     t = pow(a, q, p)
#     r = pow(a, (q + 1) // 2, p)
#     while t != 0 and t != 1:
#         t2 = t
#         i = 0
#         for i in range(1, m):
#             t2 = pow(t2, 2, p)
#             if t2 == 1:
#                 break
#         b = pow(c, 2 ** (m - i - 1), p)
#         m = i
#         c = pow(b, 2, p)
#         t = (t * c) % p
#         r = (r * b) % p
#     return r

# while True:
#     a = int(input("Введите x: "))
#     b = 11
#     y = pow(a, 3) + a + 3
#     print("Ответы:\nВычет:", legendre_symbol(y % 11, b))
#     print("y:", tonelli_shanks(y % 11, b), -tonelli_shanks(y % 11, b) % 11 if tonelli_shanks(y % 11, b) is not None else None)
#     print("y^2:", y)
#     print("y^2 mod 11:", y % 11)


# def summ(x0, y0, x1, y1, p, A):
#     if x1 == -1:
#         return x0, y0
#     if x0 == x1 and y0 == y1:
#         if y0 == 0:
#             return -1, -1
#         a = A
#         l = (3 * pow(x0, 2, p) + a) * pow(2 * y0, -1, p) % p
#         x3 = (pow(l, 2, p) - 2 * x0) % p
#         y3 = (l * (x0 - x3) - y0) % p    
#     elif x0 != x1 or y0 != y1:  
#         if x0 == x1:
#             return -1, -1  
#         l = (y1 - y0) * pow(x1 - x0, -1, p) % p
#         x3 = (pow(l, 2, p) - x1 - x0) % p
#         y3 = (l * (x0 - x3) - y0) % p
#     return x3, y3

# def mult(N, x0, y0, p, A):
#     x1 = x0
#     y1 = y0
#     for i in range(N - 1):
#         x1, y1 = summ(x0, y0, x1, y1, p, A)
#     return x1, y1

# print(mult(5, 0, 6, 11, 1))