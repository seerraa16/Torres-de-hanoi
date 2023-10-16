from pilaHanoi import Pila

def getTablero(n):
    pila1 = Pila()
    pila2 = Pila()
    pila3 = Pila()

    for i in range(n, 0, -1):
        pila1.push(i)

    return (pila1, pila2, pila3)

def imprimirTablero(tablero):
    print(f"Torre 1: {tablero[0]}")
    print(f"Torre 2: {tablero[1]}")
    print(f"Torre 3: {tablero[2]}")
    print()

def solve(tablero, n, origen, destino, auxiliar, movimientos):
    if n == 1:
        disco = origen.pop()
        destino.push(disco)
        movimientos.append(f"D{disco} from T{origen} to T{destino}")
    else:
        solve(tablero, n-1, origen, auxiliar, destino, movimientos)
        disco = origen.pop()
        destino.push(disco)
        movimientos.append(f"D{disco} from T{origen} to T{destino}")
        solve(tablero, n-1, auxiliar, destino, origen, movimientos)

if __name__ == "__main__":
    n = 5
    tablero = getTablero(n)

    print("Estado inicial del tablero:")
    imprimirTablero(tablero)

    movimientos = []
    solve(tablero, n, tablero[0], tablero[2], tablero[1], movimientos)

    print("Lista de movimientos:")
    for movimiento in movimientos:
        print(movimiento)

    print("\nEstado final del tablero:")
    imprimirTablero(tablero)
