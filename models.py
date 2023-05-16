class Persona:
    def __init__(self, edad, altura, peso, sexo):
        self.edad      = edad
        self.altura    = altura
        self.peso      = peso
        self.sexo      = sexo
        self.productos = []
        
    def comprar_producto(self, producto):
        self.productos.append(producto)
        print(f"Haz comprado {producto.nombre} por ${producto.precio}.")
        
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
