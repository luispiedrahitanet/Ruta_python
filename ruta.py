import urllib.parse
import requests, os

os.system("cls")

print()
print('╔════════════════════════════════════╗')
print('║          Luis Piedrahita           ║')
print('║  luispiedrahita.net@gmail.com      ║')
print('╠════════════════════════════════════╣')
print('║      OBTENER RUTA DE LLEGADA       ║')
print('╚════════════════════════════════════╝')
print()

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key      = "tu_clave_de_Mapquest"


while True:
    orig = input( "\nCiudad de origen ('q' para salir): " )  # Pedimos datos de origen
    if orig.lower() in ("q","quit"):
        break
    
    dest = input( "Ciudad de destino ('q' para salir): " )   # Pedimos datos de destino
    if dest.lower() in ("q","quit"):
        break
    
    # Codificamos de tipo url
    url = main_api + urllib.parse.urlencode( {"key":key, "from":orig, "to":dest} )

    print( "url: " + url )

    # Hacemos uso de la API y almacenamos como tipo json
    json_data   = requests.get(url).json()
    # Almacenamos el codigo del estado
    json_status = json_data["info"]["statuscode"]

    if json_status == 0:
        
        print( f"\nAPI Estado: {str(json_status)} = Llamada exitosa a la ruta. \n" )

        print("=======================================")
        print(f'Recorrido de {orig} a {dest}')
        print(f'Duración del viaje: {json_data["route"]["formattedTime"]}')
        print(f'Millas: {json_data["route"]["distance"]:.2f}')  # redondea a 2 decimales
        print(f'Kilómetros: {json_data["route"]["distance"]*1.61:.3f}') # redondea a 3 decimales
        print("=======================================")
        
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print( (each["narrative"]) + " (" + str( "{:.2f}".format( (each["distance"]*1.61) )) + " km)" )
        print("=======================================")

    elif json_status == 402:
        print("**********************************************")
        print("Código de estado: " + str(json_status) + "; Entradas de usuario no válidas para una o ambas ubicaciones.")
        print("**********************************************\n")
    elif json_status == 611:
        print("**********************************************")
        print("Código de estado: " + str(json_status) + "; Falta una entrada para una o ambas ubicaciones.")
        print("**********************************************\n")
    else:
        print("************************************************************************")
        print("Para Código de estado: " + str(json_status) + "; Referirse a:")
        print("https://developer.mapquest.com/documentation/directions-api/status-codes")
        print("************************************************************************\n")


