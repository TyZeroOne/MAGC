import random
import math
import copy

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

def list_points(N, k, p, A):
    M = copy.deepcopy(N)
    for i in range(2, k + 1):
        x_, y_ = summ(M[0][0], M[0][1], M[-2][0], M[-2][1], p, A)
        M.append((x_, y_, i))
        M.append((x_, p - y_, -i))
    return M

def points_includes(N, M, k, p):
    tmp_N = copy.deepcopy(N)
    tmp_M = copy.deepcopy(M)
    L = []
    for i in tmp_N:
        for j in tmp_M:
            if i[0] == j[0] and i[1] == j[1]:
                L.append(p + 1 + (2*k + 1) * i[2] - j[2])
                return L
    return L
    
def main():
    with open('output.txt', 'r') as file:
        p, A, N = None, None, None

        for line in file:
            key_value = line.strip().split(' = ')
            if key_value[0] == 'p':
                p = int(key_value[1])
            elif key_value[0] == 'A':
                A = int(key_value[1])
            # elif key_value[0] == 'N':
            #     N = int(key_value[1])
    x = random.randint(1, p - 1)
    x_inc = (x ** 3 + A * x) % p 
    while legendre_symbol(x_inc, p) != 1:
        x = random.randint(1, p - 1)
        x_inc = (x ** 3 + A * x) % p

    y = tonelli_shanks(x_inc, p)
    k = math.ceil(((2 * p) ** (1. / 4.)))

    Q = [(x, y, 1), (x, p - y, -1)]
    Q = list_points(Q, k, p, A)
    Q = [(-1, -1, 0)] + Q
    Q = sorted(Q, key=lambda x: x[0])

    x_p, y_p = mult(2 * k + 1, x, y, p, A)
    x_r, y_r = mult(p + 1, x, y, p, A)
    P = [(x_p, y_p, 1), (x_p, p - y_p, -1)]
    P = list_points(P, k, p, A)
    R = [(x_r, y_r, 0)]
    for i in P:
        x_, y_ = summ(x_r, y_r, i[0], i[1], p, A)
        if x_ == -1:
            x_, y_ = x_r, y_r
        R.append((x_, y_, i[2]))
    R = sorted(R, key=lambda x: x[0])

    N_res = []
    N_res += points_includes(R, Q, k, p)
    # print("Значение, вычисленное при построении криввой из завдания 1:", N)
    print("Значение, вычисленное при помощи алгоритма:", N_res[0])

main()