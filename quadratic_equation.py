

def get_roots(a, b, c):
    discriminant = b ** 2 - 4 * a * c
    root1 = (-b - discriminant**0.5) / (2 * a)
    root2 = (-b + discriminant**0.5) / (2 * a)
    if discriminant == 0:
        return root1, None
    else:
        return root1, root2
