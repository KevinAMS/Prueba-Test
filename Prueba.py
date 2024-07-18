#Prueba Test 
def extraer_linea(linea):
    inicio = linea.find('>') 
    fin = linea.find('<', inicio)
    if inicio != -1 and fin != -1:
        contenido = linea[inicio + 1:fin].strip()
        #print(f'Contenido entre > y <: {contenido}')
        id_partes = contenido.split(';')
        for parte in id_partes:
            if 'ID' in parte:
                #print(f'Parte con "ID": {parte}')
                if '=' in parte:
                    id_valor_partes = parte.split('=')
                    id_valor = id_valor_partes[1].strip()
                    #print(id_valor)
                    return id_valor
    return None 
  
  
def obtenerIDS(datas):
    ids = set()
    with open(datas, 'r') as archivo:
        for linea in archivo:
            id_valor = extraer_linea(linea)
            if id_valor:
                ids.add(id_valor)
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

ids_data15 = obtenerIDS(data15)
ids_data16 = obtenerIDS(data16)

idsUnicos = ids_data15 - ids_data16

print("Los siguientes Imeis no estan en el archivo de las 16 hr: ")
#print(idsUnicos)
idsFormateados = formatoColumna(idsUnicos)
print(idsFormateados)