stock = {
"CPU": 10,
"RAM": 50,
"SSD": 20,
"Mouse": 0
}

pedidos = ["CPU", "RAM", "RAM", "Teclado", "Mouse"]

def procesar_pedidos(pedidos : list, stock : dict):
    for p in pedidos:
        if p in stock and stock[p] > 0:
            stock[p] -= 1
        if p in stock and stock[p] == 0:
            print('Sin stock de:', p)
        if p not in stock:
            print('Producto desconocido:', p)
    print(stock)

print(procesar_pedidos(pedidos, stock))

