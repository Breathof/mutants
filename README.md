# MELI examen Magneto

Examen de ingreso a MELI

## Solución

La solución se bada en los fundamentos de la programación dinámica, el cual cachea y utiliza resultados procesados anteriormente. Simplemente se intentan encontrar dos genes raros (secuencia de 4 bases iguales) preguntando si podes moverte 4 veces para la misma dirección.

### Optimizaciones
- Debido a la naturalidad del problema, no fue preciso cachear resultados anteriores, el algoritmo son dos for anidados, que recorren la matriz de derecha a izquierda y de arriba para bajo. Dado un momento K en el algoritmo, me puedo mover para las distintas 8 direcciones, pero dado a que las direcciones arriba, arribaIzquierda, arribaDerecha, e izquierda ya fueron procesadas en un paso anterior (por como recorremos la matriz), me quedo con las 4 direcciones restantes, reduciendo así un 50% de los casos a procesar.
- Se preguntó en un mail si se podrían repetir las bases para formar un "gen raro", siendo la respuesta negativa, no se pueden cruzar bases, por lo que de haber encontrado un gen raro, en las próximas iteraciones no se pregunta por la base ya encontrada.
- Al encontrarse un gen raro, no se empieza la búsqueda de nuevo en el array, sino que se comienza a buscar una posición después del que ya se encontró
- Como son solo necesarios dos genes raros para determinar si la persona es mutante, no es necesario recorrer toda la matriz en caso de haber encontrado dos genes extraños

## Arquitectura de la solución

Debido a que la API puede presentar fluctuaciones agresivas de trafico, se diseño una arquitectura acorde para poder responder adecuadamente.

### /mutant
Asumiendo que las matrices de ADN no son excesivamente grandes, se puede hacer este calculo y responder a las peticiones inmediatamente, lo que es costoso es ingresar los datos a la base de datos, por lo que en cada request aparte de hacer el calculo, se guarda el resultado en una cola, la cual consumidores en threads aparte van agarrando estos mensajes (resultados) y los van guardando en la base de datos.


Lo ideal seria implementar una cola para los request, por ejemplo usando RabbieMQ, el cual cada vez que se recibe una request, retorna un 201 con un código de task. En este caso se tienen dos opciones, dejar que el cliente haga pool preguntando por el task, o que se devuelva el task al cliente una vez este este completo.
Esto le saca la carga al webserver de esperar a calcular el ADN para después retornar la respuesta. No se implemento esta solución pero se deja la idea de la misma.

### /stats
Para los stats, como se tiene que buscar la cantidad de humanos y mutantes en la base de datos para hacer el calculo, se implemento un cache, el cual un worker va actualizando cada 5 segundos, entonces cada vez que se consume el endpoint, en vez de ir a base de datos para hacer los calculo, se retorna la respuesta cacheada, no afectando así la performance de las respuestas.

## Prerequisitos

Se necesita tener instalado en el entorno 
- Python 3.8+
- pip3

### Instalación

Se proporciona un script init.sh el cual inicializa la base de datos e instala las dependencias.

Para correrlo, primero se necesitan permisos de ejecución

```
sudo chmod +x ./init.sh
```
Luego se corre el script
```
./init.sh
```

Si por acaso el script no llegase a funcionar, se pueden instalar las dependencias manualmente e inicializar la base de datos desde el archivo data_base_init.py

```
sudo pip3 -r requirements.txt
sudo python3 data_base_init.py
```
Nota: puede que solo tenga la version de Python3.8+ instalada (y no tenga la 2), por lo que el comando podría ser python en vez de python3.


Por ultimo, para correr el servidor simplemente inicia el archivo main.py
```
python3 ./src/main.py
```

## Probando cliente
Se proporciona un archivo client.py el cual proporciona ejemplos de ejecución, peticiones al servidor, para esto elija el contexto en cual lo quiere ejecutar asignando a la variable ENVIRONMENT el valor de PROD o DEV dentro del mismo archivo.
También podrá elegir a qué endpoint consumir comentando o descomentando funciones en la función main.


Por ultimo corra al archivo
```
python3 ./src/client.py
```


## Unit testing

Se emplea la libreria pytest y pytest-cov para realizar el unit testing y cooverage del código.


Para ejecutarlo se para en la raíz del proyecto y ejecuta
```
pytest -v --cov=mutant --cov-report=html
```
El mismo comando generara un reporte .html que podrá encontrarlo en la carpeta ./htmlcov/index.html

Nota: Se excluyen de los test las funciones calculate_adn_ratio(ya que depende de la data actual en la base de datos) y ratio_worker (ya que no tiene sentido testear un worker).

## CI
Se implemento continuos integration con la herramienta de GitHub Actions. El cual se encarga de correr los testing unitarios cada vez que se hace un push de la solución.

## Deployment

Se utilizo una instancia EC2 de AWS para publicar esta solución. Los endpoints para probar la solución son:
```
18.188.95.255/mutant (POST con JSON)

18.188.95.255/stats (GET)
```
