#1. Ejercicio 2.1 (Página 63)
class Persona:
    """Clase que representa a una persona con sus datos básicos."""
    def __init__(self, nombre: str, apellidos: str, numero_documento: str, ano_nacimiento: int):
        self.nombre = nombre
        self.apellidos = apellidos
        self.numero_documento = numero_documento
        self.ano_nacimiento = ano_nacimiento

    def imprimir(self):
        """Muestra los datos de la persona por consola."""
        print(f"Nombre: {self.nombre}")
        print(f"Apellidos: {self.apellidos}")
        print(f"Número de documento: {self.numero_documento}")
        print(f"Año de nacimiento: {self.ano_nacimiento}")


if __name__ == "__main__":
    # Creación e instanciación de dos objetos de la clase Persona
    p1 = Persona("Pedro", "Pérez", "1053123456", 1998)
    p2 = Persona("Luis", "León", "1053789101", 2001)

    print("--- Datos de la Persona 1 ---")
    p1.imprimir()
    print("\n--- Datos de la Persona 2 ---")
    p2.imprimir()

#2. Ejercicio 2.2 (Página 66)
from enum import Enum

class TipoPlaneta(Enum):
    GASEOSO = "Gaseoso"
    TERRESTRE = "Terrestre"
    ENANO = "Enano"

class Planeta:
    def __init__(self, nombre: str, cantidad_satelites: int, masa_kg: float,
                 volumen_km3: float, diametro_km: int, distancia_sol_millones_km: int,
                 tipo: TipoPlaneta, es_observable: bool):
        self.nombre = nombre
        self.cantidad_satelites = cantidad_satelites
        self.masa_kg = masa_kg
        self.volumen_km3 = volumen_km3
        self.diametro_km = diametro_km
        self.distancia_sol_millones_km = distancia_sol_millones_km
        self.tipo = tipo
        self.es_observable = es_observable

    def calcular_densidad(self) -> float:
        """Calcula la densidad del planeta (Masa / Volumen)."""
        if self.volumen_km3 == 0:
            return 0.0
        return self.masa_kg / self.volumen_km3

    def es_planeta_exterior(self) -> bool:
        """Determina si es un planeta exterior (distancia > 3.4 UA ≈ 508.63 Millones km)."""
        limite_kilometros = 508.63
        return self.distancia_sol_millones_km > limite_kilometros

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cantidad de Satélites: {self.cantidad_satelites}")
        print(f"Masa (kg): {self.masa_kg}")
        print(f"Volumen (km³): {self.volumen_km3}")
        print(f"Diámetro (km): {self.diametro_km}")
        print(f"Distancia media al Sol (Millones km): {self.distancia_sol_millones_km}")
        print(f"Tipo de Planeta: {self.tipo.value}")
        print(f"Es observable a simple vista: {self.es_observable}")
        print(f"Densidad: {self.calcular_densidad():.4f} kg/km³")
        print(f"Es planeta exterior: {self.es_planeta_exterior()}")


if __name__ == "__main__":
    p1 = Planeta("Tierra", 1, 5.972e24, 1.08321e12, 12742, 150, TipoPlaneta.TERRESTRE, True)
    p2 = Planeta("Júpiter", 79, 1.898e27, 1.43128e15, 139820, 778, TipoPlaneta.GASEOSO, True)

    print("=== PLANETA 1 ===")
    p1.imprimir()
    print("\n=== PLANETA 2 ===")
    p2.imprimir()

#3. Ejercicio 2.3 (Página 66)
from enum import Enum

class TipoCombustible(Enum):
    GASOLINA = "Gasolina"
    BIOETANOL = "Bioetanol"
    DIESEL = "Diésel"
    GAS_NATURAL = "Gas natural"

class TipoAutomovil(Enum):
    CIUDAD = "Ciudad"
    SUBCOMPACTO = "Subcompacto"
    COMPACTO = "Compacto"
    FAMILIAR = "Familiar"
    EJECUTIVO = "Ejecutivo"
    SUV = "SUV"

class Automovil:
    def __init__(self, marca: str, modelo: int, motor: float, tipo_combustible: TipoCombustible,
                 tipo_automovil: TipoAutomovil, numero_puertas: int, cantidad_asientos: int,
                 velocidad_maxima: int, color: str):
        self.marca = marca
        self.modelo = modelo
        self.motor = motor
        self.tipo_combustible = tipo_combustible
        self.tipo_automovil = tipo_automovil
        self.numero_puertas = numero_puertas
        self.cantidad_asientos = cantidad_asientos
        self.velocidad_maxima = velocidad_maxima
        self.color = color
        self.velocidad_actual = 0

    def acelerar(self, incremento: int):
        if self.velocidad_actual + incremento > self.velocidad_maxima:
            self.velocidad_actual = self.velocidad_maxima
            print(f"Alerta: Se alcanzó la velocidad máxima ({self.velocidad_maxima} km/h).")
        else:
            self.velocidad_actual += incremento

    def desacelerar(self, decremento: int):
        if self.velocidad_actual - decremento < 0:
            self.velocidad_actual = 0
            print("El automóvil se ha detenido totalmente.")
        else:
            self.velocidad_actual -= decremento

    def frenar(self):
        self.velocidad_actual = 0

    def calcular_tiempo_llegada(self, distancia_km: float) -> float:
        if self.velocidad_actual == 0:
            print("No se puede calcular el tiempo: El automóvil está detenido.")
            return 0.0
        return distancia_km / self.velocidad_actual

    def imprimir(self):
        print(f"Marca: {self.marca}")
        print(f"Modelo: {self.modelo}")
        print(f"Motor: {self.motor} L")
        print(f"Combustible: {self.tipo_combustible.value}")
        print(f"Tipo: {self.tipo_automovil.value}")
        print(f"Puertas: {self.numero_puertas}")
        print(f"Asientos: {self.cantidad_asientos}")
        print(f"Velocidad Máxima: {self.velocidad_maxima} km/h")
        print(f"Color: {self.color}")
        print(f"Velocidad Actual: {self.velocidad_actual} km/h")


if __name__ == "__main__":
    auto = Automovil("Toyota", 2023, 2.0, TipoCombustible.GASOLINA,
                     TipoAutomovil.COMPACTO, 4, 5, 200, "Rojo")

    auto.imprimir()
    print("\n--- Operaciones de Conducción ---")
    auto.acelerar(100)
    print(f"Velocidad tras acelerar: {auto.velocidad_actual} km/h")
    print(f"Tiempo para recorrer 250 km: {auto.calcular_tiempo_llegada(250):.2f} horas")

    auto.desacelerar(50)
    print(f"Velocidad tras desacelerar: {auto.velocidad_actual} km/h")

    auto.frenar()
    print(f"Velocidad tras frenar: {auto.velocidad_actual} km/h")

#4. Ejercicio 2.4 (Página 86)
import math

class TrianguloRectangulo:
    """Clase que representa un triángulo rectángulo y calcula sus propiedades."""
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calcular_area(self) -> float:
        return (self.base * self.altura) / 2

    def calcular_hipotenusa(self) -> float:
        return math.sqrt(self.base**2 + self.altura**2)

    def calcular_perimetro(self) -> float:
        return self.base + self.altura + self.calcular_hipotenusa()

    def determinar_tipo_triangulo(self) -> str:
        hipotenusa = self.calcular_hipotenusa()
        if self.base == self.altura == hipotenusa:
            return "Equilátero"
        elif self.base != self.altura and self.base != hipotenusa and self.altura != hipotenusa:
            return "Escaleno"
        else:
            return "Isósceles"


if __name__ == "__main__":
    t1 = TrianguloRectangulo(3, 4)
    print(f"Base: {t1.base}, Altura: {t1.altura}")
    print(f"Área: {t1.calcular_area()}")
    print(f"Hipotenusa: {t1.calcular_hipotenusa():.2f}")
    print(f"Perímetro: {t1.calcular_perimetro():.2f}")
    print(f"Tipo de Triángulo: {t1.determinar_tipo_triangulo()}")

#5. Ejercicio 2.5 (Página 95)
class CuentaBancaria:
    """Modela una cuenta bancaria con operaciones de depósito y retiro."""
    def __init__(self, nombres_titular: str, apellidos_titular: str, numero_cuenta: str, tipo_cuenta: str):
        self.nombres_titular = nombres_titular
        self.apellidos_titular = apellidos_titular
        self.numero_cuenta = numero_cuenta
        self.tipo_cuenta = tipo_cuenta  # "Ahorros" o "Corriente"
        self.saldo = 0.0

    def consultar_saldo(self) -> float:
        return self.saldo

    def consignar(self, valor: float) -> bool:
        if valor > 0:
            self.saldo += valor
            print(f"Consignación exitosa de ${valor:,.2f}. Nuevo saldo: ${self.saldo:,.2f}")
            return True
        else:
            print("El valor a consignar debe ser mayor a cero.")
            return False

    def retirar(self, valor: float) -> bool:
        if valor <= 0:
            print("El valor a retirar debe ser mayor a cero.")
            return False
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Retiro exitoso de ${valor:,.2f}. Nuevo saldo: ${self.saldo:,.2f}")
            return True
        else:
            print(f"Retiro rechazado. Fondos insuficientes. Saldo actual: ${self.saldo:,.2f}")
            return False

    def imprimir_datos(self):
        print(f"Titular: {self.nombres_titular} {self.apellidos_titular}")
        print(f"Número de Cuenta: {self.numero_cuenta}")
        print(f"Tipo de Cuenta: {self.tipo_cuenta}")
        print(f"Saldo Actual: ${self.saldo:,.2f}")


if __name__ == "__main__":
    cuenta = CuentaBancaria("Walter", "Arboleda", "123456789", "Ahorros")
    cuenta.imprimir_datos()

    print("\n--- Transacciones ---")
    cuenta.consignar(500000)
    cuenta.retirar(150000)
    cuenta.retirar(400000)  # Intento de retiro superior al saldo