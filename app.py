def add(a, b):
    """Ajoute deux nombres."""
    return a + b


def multiply(x, y):
    return x * y


def divide(x, y):
    if y != 0:
        return x / y
    return None  # Retourne None si y est égal à 0


def greet(name):
    """Greet fonction."""
    if name == "":
        return "Hello, World!"
    else:
        return "Hello, " + name  # Ajout d'un espace après la virgule
