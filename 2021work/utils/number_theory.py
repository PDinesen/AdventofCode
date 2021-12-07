from typing import Tuple, List, Union

from math import gcd

factors_t = List[Tuple[int, int]]
number_t = Union[factors_t, int]


def factorize(n: number_t) -> factors_t:
    if isinstance(n, list):
        return n
    factors = []
    p = 2
    while p * p <= n:
        v_p = 0
        while n % p == 0:
            v_p += 1
            n //= p
        if v_p > 0:
            factors.append((p, v_p))
        p += 1
    if n > 1:
        factors.append((n, 1))
    return factors


def phi(n: number_t) -> int:
    m = 1
    for p, v_p in factorize(n):
        m *= (p - 1) * p ** (v_p - 1)
    return m


def chinese_remainder_theorem(constraints):
    # Constraints on the form [(a, b), .. ] meaning x == a mod b
    b_product = 1
    for a, b in constraints:
        b_product *= b
    x = 0
    for a, b in constraints:
        inv = pow(b_product // b, phi(b) - 1, b)
        x += a * (b_product // b) * inv
    x %= b_product
    return x


class OrderGetter:
    def __init__(self, n: int):
        self.n: int = n
        self.n_factors: factors_t = factorize(n)
        self.phi_n: int = phi(self.n_factors)
        self.phi_n_factors: factors_t = factorize(self.phi_n)

    def get_order(self, g):
        if gcd(self.n, g) > 1:
            raise Exception(f'g={g} is not in (Z_n)* for n={self.n}')
        # xs contains elements x such that g^x = 1 in Z_n^*
        xs = []
        for p, v_p in self.phi_n_factors:
            m = self.phi_n // p ** v_p
            g_m = pow(g, m, self.n)
            for _ in range(v_p):
                if g_m == 1:
                    xs.append(m)
                g_m = pow(g_m, p, self.n)
                m *= p
        order = self.phi_n
        for x in xs:
            order = gcd(order, x)
        return order

    def is_generator(self, g):
        return gcd(g, self.n) == 1 and self.get_order(g) == self.phi_n


def has_no_generators(n):
    if n % 4 == 0 and n > 4:
        return True
    factors = factorize(n)
    if len(factors) > 2 or (len(factors) == 2 and factors[0][0] > 2):
        return True
    return False


if __name__ == '__main__':
    for n in range(1, 1000):
        order_getter = OrderGetter(n)
        generators = [g for g in range(n) if order_getter.is_generator(g)]
        if (len(generators) == 0) != has_no_generators(n):
            print(f'n = {n}. #generators = {len(generators)}. phi(phi(n)) = {phi(phi(n))}')
        if (len(generators) != phi(phi(n))) != has_no_generators(n):
            print(f'n = {n}. #generators = {len(generators)}. phi(phi(n)) = {phi(phi(n))}')