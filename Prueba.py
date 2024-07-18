#Prueba Test 
def extraerLinea(linea):
    inicio = linea.find('>') 
    fin = linea.find('<', inicio)
    if inicio != -1 and fin != -1:
        contenido = linea[inicio + 1:fin].strip()
        #print(f'Contenido entre > y <: {contenido}')
        idPartes = contenido.split(';')
        for parte in idPartes:
            if 'ID' in parte:
                #print(f'Parte con "ID": {parte}')
                if '=' in parte:
                    valorPartes = parte.split('=')
                    idValor = valorPartes[1].strip()
                    #print(id_valor)
                    return idValor
    return None 
  
  
def obtenerIDS(datas):
    ids = set()
    with open(datas, 'r') as archivo:
        for linea in archivo:
            idValor = extraerLinea(linea)
            if idValor:
                ids.add(idValor)
                #print(f'ID añadido: {id_valor}')
    return ids


def formatoColumna(idsUnicos, formColum = 4):
    idsUnicos = list(idsUnicos)
    formato = []
    for i in range(0, len(idsUnicos), formColum):
        columna = idsUnicos[i:i+4]
        formato.append(", ".join(f"'{id}'" for id in columna))

    idsFormato = "[ " + ",\n".join(formato) + " ]"

    return idsFormato

            
data15 = 'data_15.txt'
data16 = 'data_16.txt'

idsData15 = obtenerIDS(data15)
idsData16 = obtenerIDS(data16)

idsUnicos = idsData15 - idsData16

print("Los siguientes Imeis no estan en el archivo de las 16 hr: ")
#print(idsUnicos)
idsFormateados = formatoColumna(idsUnicos)
print(idsFormateados)