import random
import matplotlib.pyplot as plt
import sympy
def is_prime(n, k=100):
    if n <= 1:
        return False
    if n == 2:
        return True
    for _ in range(k):
        a = random.randint(2, n - 2)
        if pow(a, n - 1, n) != 1:
            return False
    return True

def legendre_symbol(a, p):
    return pow(a, (p - 1) // 2, p)

def find_prime(l):
    prime = []
    if l < 9:
        for p in range(2**(l-1), 2**l):
            if p % 4 == 1 and sympy.isprime(p):
                prime.append(p)
    else:
        p = random.randint(2**(l-1), 2**l)
        while True:
            if p % 4 == 1 and sympy.isprime(p):
                break
            p = random.randint(2**(l-1), 2**l)
        prime.append(p)
    return prime
            
def decompose_p(p):
    for a in range(2, int(p ** 0.5) + 1):
        b_sq = p - a * a
        if b_sq >= 0:
            b = int(b_sq ** 0.5)
            if a * a + b * b == p:
                return a, b
    return None, None

def check_powers(p, r, m):
    for i in range(1, m + 1):
        if pow(p, i, r) == 1:
            return False
    return True

def generate_N(p, a, b):
    for T in [2 * a, -2 * a, 2 * b, -2 * b]:
        N = p + 1 + T
        if (N % 2 == 0 and is_prime(N // 2)):
            r = N // 2
            return r, N
        elif (N % 4 == 0 and is_prime(N // 4)):
            r = N // 4
            return r, N
    return 0, 0

def generate_point(p, N, r):    
    while True:
        x0 = random.randint(1, p - 1)
        y0 = random.randint(1, p - 1)
        A = (pow(y0, 2, p) - pow(x0, 3, p)) * pow(x0, -1, p) % p
        if (pow(p - A, (p - 1) // 2, p) == 1 and N // r == 4) or \
            (pow(p - A, (p - 1) // 2, p) == p - 1 and N // r == 2):  
            return x0, y0, A
        else:
            continue

def summ(x0, y0, x1, y1, p, A):
    if x1 == -1:
        return x0, y0
    if x0 == x1 and y0 == y1:
        if y0 == 0:
            return -1, -1
        a = A
        l = (3 * pow(x0, 2, p) + a) * pow(2 * y0, -1, p) % p
        x3 = (pow(l, 2, p) - 2 * x0) % p
        y3 = (l * (x0 - x3) - y0) % p    
    elif x0 != x1 or y0 != y1:  
        if x0 == x1:
            return -1, -1  
        l = (y1 - y0) * pow(x1 - x0, -1, p) % p
        x3 = (pow(l, 2, p) - x1 - x0) % p
        y3 = (l * (x0 - x3) - y0) % p
    return x3, y3

def mult(N, x0, y0, p, A):
    x1 = x0
    y1 = y0
    for i in range(N - 1):
        x1, y1 = summ(x0, y0, x1, y1, p, A)
    return x1, y1

def curve_generation(l, m):
    prime = find_prime(l)
    if len(prime) == 0:
        return None, None, None, None, None
    k = random.randint(0, len(prime) - 1)
    for i in range(k, len(prime)):
        p = prime[i]
        a, b = decompose_p(p)
        if a is None or b is None:
            if i == len(prime) - 1:
                return None, None, None, None, None
            else:
                continue
        r, N = generate_N(p, a, b)
        if (r == 0 or N == 0) and i == len(prime) - 1:
            return None, None, None, None, None
        elif (r == 0 or N == 0):
            continue
        if p != r and check_powers(p, r, m):
            break  
        if i == len(prime) - 1:
            return None, None, None, None, None
    x0, y0, A = generate_point(p, N, r)
    x1, y1 = mult(N, x0, y0, p, A)
    while x1 != -1:
        x0, y0, A = generate_point(p, N, r)
        x1, y1 = mult(N, x0, y0, p, A)
    x3, y3 = mult(N // r, x0, y0, p, A)
    Q = (x3, y3)
    return p, A, Q, r, N

def legendre_symbol(a, p):
    return pow(a, (p - 1) // 2, p)

def tonelli_shanks(a, p):
    if legendre_symbol(a, p) != 1:
        return None  
    if p % 4 == 3:
        return pow(a, (p + 1) // 4, p)
    s = 0
    q = p - 1
    while q % 2 == 0:
        s += 1
        q //= 2
    z = 2
    while legendre_symbol(z, p) != p - 1:
        z += 1
    m = s
    c = pow(z, q, p)
    t = pow(a, q, p)
    r = pow(a, (q + 1) // 2, p)
    while t != 0 and t != 1:
        t2 = t
        i = 0
        for i in range(1, m):
            t2 = pow(t2, 2, p)
            if t2 == 1:
                break
        b = pow(c, 2 ** (m - i - 1), p)
        m = i
        c = pow(b, 2, p)
        t = (t * c) % p
        r = (r * b) % p
    return r

def generate_points_on_curve(A, p, Q):
    points = [Q]
    points.append(summ(Q[0], Q[1], Q[0], Q[1], p, A))
    while ((points[0][0] == points[-1][0] and points[0][1] == points[-1][1] and points[-1][1] != 0) \
        or ((points[0][0] != points[-1][0] or points[0][1] != points[-1][1]) and points[-1][0] - points[0][0] != 0)):
           points.append(summ(points[-1][0], points[-1][1], Q[0], Q[1], p, A))
    return points

def generate_curve(A, p, points):
    x_vals = [point[0] for point in points]
    y_vals = [point[1] for point in points]
    plt.figure(figsize=(8, 6))
    plt.scatter(x_vals, y_vals, color='blue', label="Точки на кривой")
    x, y = points[0] 
    # Отображаем заданную точку красным цветом 
    plt.scatter(x, y, color='green', s=50, label=f'Точка Q ({x}, {y})') 
    plt.title(f'Эллиптическая кривая: $y^2 = x^3 + {A}x$ (mod {p})')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.show()

def main():
    l = int(input("Введите длину бит характеристики поля: "))
    m = int(input("Введите параметр безопасности: "))
    p, A, Q, r, N = curve_generation(l, m)
    while p == None:
        l = int(input("Не найдено подходящего значения. Введите другую длину бит характеристики поля: "))
        p, A, Q, r, N = curve_generation(l, m)
    points = generate_points_on_curve(A, p, Q)
    txt = ["p", "A", "Q", "r", "N", "points"]
    i = 0
    with open('output.txt', 'w') as file:
        for element in [p, A, Q, r, N, points]:
            file.write(f"{txt[i]} = {element}\n")
            i += 1
    generate_curve(A, p, points)
    
main()