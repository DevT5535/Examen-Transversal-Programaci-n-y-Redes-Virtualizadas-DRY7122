# viaje_chile_argentina.py

import geopy.distance
import webbrowser
import time

def calcular_distancia(ciudad_origen, ciudad_destino):
    # Coordenadas aproximadas de ciudades (en una aplicación real usarías una API)
    ciudades = {
        'santiago': (-33.4489, -70.6693),
        'buenos aires': (-34.6037, -58.3816),
        'mendoza': (-32.8908, -68.8272),
        'valparaíso': (-33.0472, -71.6127),
        'cordoba': (-31.4201, -64.1888),
        'rosario': (-32.9587, -60.6930)
    }
    
    try:
        coords_origen = ciudades[ciudad_origen.lower()]
        coords_destino = ciudades[ciudad_destino.lower()]
    except KeyError:
        print("Una o ambas ciudades no están en la base de datos.")
        return None, None
    
    distancia_km = geopy.distance.distance(coords_origen, coords_destino).km
    distancia_millas = distancia_km * 0.621371
    
    return distancia_km, distancia_millas

def calcular_duracion(distancia_km, transporte):
    velocidades = {
        'auto': 90,    # km/h promedio
        'bus': 80,     # km/h promedio
        'avion': 800, # km/h promedio
        'bicicleta': 20 # km/h promedio
    }
    
    try:
        velocidad = velocidades[transporte]
    except KeyError:
        print("Transporte no válido. Usando velocidad de auto por defecto.")
        velocidad = 80
    
    horas = distancia_km / velocidad
    horas_viaje = int(horas)
    minutos_viaje = int((horas - horas_viaje) * 60)
    
    return horas_viaje, minutos_viaje

def mostrar_narrativa(ciudad_origen, ciudad_destino, transporte):
    narrativas = {
        'auto': f"Emprenderás un emocionante viaje por carretera desde {ciudad_origen.title()} hasta {ciudad_destino.title()}, disfrutando de los paisajes.",
        'bus': f"Viajarás cómodamente en bus desde {ciudad_origen.title()} a {ciudad_destino.title()}, ideal para relajarse y disfrutar del camino.",
        'avion': f"Un rápido vuelo te llevará desde {ciudad_origen.title()} hasta {ciudad_destino.title()}, ahorrando tiempo para disfrutar tu destino.",
        'bicicleta': f"Aventúrate en un desafiante viaje en bicicleta desde {ciudad_origen.title()} hasta {ciudad_destino.title()}, para los más intrépidos."
    }
    
    print("\n--- Narrativa del Viaje ---")
    print(narrativas.get(transporte, "Tu viaje será una gran aventura, sin importar el medio de transporte."))
    print("¡Buen viaje!\n")

def main():
    print("Bienvenido al calculador de viajes Chile-Argentina")
    print("Presiona 's' en cualquier momento para salir\n")
    
    while True:
        # Solicitar ciudades
        ciudad_origen = input("Ingresa la ciudad de origen en Chile (ej: Santiago, Valparaíso): ")
        if ciudad_origen.lower() == 's':
            break
            
        ciudad_destino = input("Ingresa la ciudad de destino en Argentina (ej: Buenos Aires, Mendoza): ")
        if ciudad_destino.lower() == 's':
            break
        
        # Calcular distancia
        distancia_km, distancia_millas = calcular_distancia(ciudad_origen, ciudad_destino)
        
        if distancia_km is None:
            continue
        
        # Mostrar distancia
        print(f"\nDistancia entre {ciudad_origen.title()} y {ciudad_destino.title()}:")
        print(f"{distancia_km:.2f} kilómetros")
        print(f"{distancia_millas:.2f} millas")
        
        # Seleccionar transporte
        print("\nMedios de transporte disponibles: auto, bus, avion, bicicleta")
        transporte = input("Elige tu medio de transporte: ").lower()
        if transporte == 's':
            break
        
        # Calcular y mostrar duración
        horas, minutos = calcular_duracion(distancia_km, transporte)
        print(f"\nDuración estimada del viaje: {horas} horas y {minutos} minutos")
        
        # Mostrar narrativa
        mostrar_narrativa(ciudad_origen, ciudad_destino, transporte)
        
        # Preguntar por otro viaje
        continuar = input("¿Deseas calcular otro viaje? (s/n): ")
        if continuar.lower() == 's':
            break
    
    print("\nGracias por usar el calculador de viajes. ¡Hasta pronto!")

if __name__ == "__main__":
    # Instalar geopy si no está instalado
    try:
        import geopy
    except ImportError:
        print("Instalando la librería geopy...")
        import subprocess
        subprocess.check_call(["python", "-m", "pip", "install", "geopy"])
        import geopy
    
    main()