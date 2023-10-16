class NodoPila:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class Pila:
    def __init__(self):
        self.tope = None

    def push(self, valor):
        nuevo_nodo = NodoPila(valor)
        if not self.tope:
            self.tope = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.tope
            self.tope = nuevo_nodo

    def pop(self):
        if not self.tope:
            return None
        else:
            valor = self.tope.valor
            self.tope = self.tope.siguiente
            return valor

    def __str__(self):
        if not self.tope:
            return "Pila vacía"
        else:
            actual = self.tope
            resultado = ""
            while actual:
                resultado += str(actual.valor) + "\n"
                actual = actual.siguiente
            return resultado.strip()
