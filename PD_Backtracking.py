def impr_laberinto(laberinto, camino=None):
    if camino is None:
        camino = set()
    for i in range(len(laberinto)):
        for j in range(len(laberinto[0])):
            if (i, j) in camino:
                print("X", end=" | ")
            else:
                print(laberinto[i][j], end=" | ")
        print()
    print()

def _valida(laberinto, fila, columna, visitadas):
    filas = len(laberinto)
    columnas = len(laberinto[0])
    return (0 <= fila < filas and 0 <= columna < columnas and 
            str(laberinto[fila][columna]) not in ['0'] and (fila, columna) not in visitadas)

def obtener_valor(laberinto, fila, columna):
    celda = laberinto[fila][columna]
    if str(celda) in ['F', 'I']:
        return 1
    return int(celda)

def resolver_laberinto(laberinto, inicio, fin, puntaje_minimo):
    filas = len(laberinto)
    columnas = len(laberinto[0])
    
    direcciones = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    
    mejor_camino = None
    mejor_puntaje = -1
    
    def backtracking(fila_actual, col_actual, visitadas, camino_actual, puntaje_actual):
        nonlocal mejor_camino, mejor_puntaje
        
        if (fila_actual, col_actual) == fin and puntaje_actual >= puntaje_minimo:
            if puntaje_actual > mejor_puntaje:
                mejor_puntaje = puntaje_actual
                mejor_camino = camino_actual.copy()
            return True
        
        for df, dc in direcciones:
            nueva_fila, nueva_col = fila_actual + df, col_actual + dc
            if _valida(laberinto, nueva_fila, nueva_col, visitadas):
                visitadas.add((nueva_fila, nueva_col))
                camino_actual.append((nueva_fila, nueva_col))
                valor_celda = obtener_valor(laberinto, nueva_fila, nueva_col)
                
                encontrado = backtracking(nueva_fila, nueva_col, visitadas, camino_actual, puntaje_actual + valor_celda)
                
                camino_actual.pop()
                visitadas.remove((nueva_fila, nueva_col))
                
                if encontrado and mejor_puntaje >= puntaje_minimo:
                    return True
        return False
    
    fila_inicio, col_inicio = inicio
    visitadas = set([(fila_inicio, col_inicio)])
    camino_actual = [(fila_inicio, col_inicio)]
    puntaje_inicial = obtener_valor(laberinto, fila_inicio, col_inicio)
    
    backtracking(fila_inicio, col_inicio, visitadas, camino_actual, puntaje_inicial)
    
    return mejor_camino, mejor_puntaje

laberinto = [
    ['F', 1, 1, 3, 0, 1, 1, 1, 4],
    [3, 0, 0, 1, 0, 1, 0, 0, 1],
    [1, 1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 1, 1, 3, 1, 1],
    [3, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 1, 1, 1, 3, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 1, 0, 0, 4],
    ['I', 1, 3, 1, 0, 1, 1, 1, 1] 
]

posicion_inicio = (8, 0)  
posicion_fin = (0, 0)     
puntaje_minimo_requerido = 23

print("Laboriginal:")
impr_laberinto(laberinto)

camino_solucion, puntaje_total = resolver_laberinto(laberinto, posicion_inicio, posicion_fin, puntaje_minimo_requerido)


if camino_solucion:
    print(f"\n¡Camino encontrado con puntaje de {puntaje_total}!")
    print("Laberinto camino solución:")
    impr_laberinto(laberinto, set(camino_solucion))
    
else:
    print("no hay un camino ")