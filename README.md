# Geolocalizador: Localizador de atentados en Ucrania
Repositorio del proyecto final de la clase de Programación, Universidad del Rosario 2022-1. <br>
Profesor: Andrés Mauricio Perez. 

**Identificación del problema:**  
A raíz del conflicto geopolítico entre Rusia y Ucrania, ha sido
difícil hacer seguimiento a los diferentes ataques que ha promovido Rusia y los lugares en
Ucrania que los han sufrido. Es por ello que se decidió hacer una visualización de eventos
bélicos que han ocurrido en territorio ucraniano desde que Rusia atacó por primera vez el 24
de febrero.

## Objetivos del proyecto
### General: 
- Se busca visualizar los numerosos eventos bélicos que ha sufrido Ucrania, teniendo en
cuenta una base de datos que contiene fecha, hora, ubicación y coordenadas de cada
evento registrado hasta el momento.

### Específicos:
- Depurar la base de datos, a cargo de Felipe Bobadilla.
- Transformar la base de datos en una lista, a cargo de Sofia Barreto.
- Crear tablas ordenadas con la información encontrada, a cargo de David Gamba.
- Aplicar las extensiones de la librería `Plotly express` para el modelado de las ubicaciones
de los eventos, a cargo de todos los integrantes.
- Exposición gráfica de los datos sobre el mapa de Ucrania, a cargo de todos.

## Herramientas y conceptos de programación:

### Librerias:
- [`Requests`](https://docs.python-requests.org/en/latest/), para extraer información.
- [`Pandas`](https://pandas.pydata.org/), para tabular la información encontrada.
- [`Plotly express`](https://plotly.com/python/plotly-express/), para generar el mapa de Ucrania.

### Herramientas:
- Listas.
- Ciclos `for` y `while`.
- Condicionales.
- Diccionarios.
- Tuplas.
- Json.

Las herramientas están sujetas a modificación a lo largo del proyecto.

## Base de datos: 
La base de datos proviene del grupo de periodismo investigativo [Bellingcat](https://en.wikipedia.org/wiki/Bellingcat), ubicado en los Paises Bajos. 
Para este proyecto se utilizarán los datos encontrados en [este](https://ukraine.bellingcat.com/ukraine-server/api/ukraine/export_events/deeprows) link.

## Limitaciones:
- Lograr una visualización clara para el usuario. 
- Lograr que el proyecto sea desarrollado en el tiempo establecido en el programa.
- Coordinar y adecuar los conocimientos de los integrantes con su respectivo trabajo. 

## Autores
Sofía Barreto Ojeda ([@FiaOjeda](https://github.com/Fiaojeda)), Néstor Felipe Bobadilla ([@Felipe-Bobadilla](https://github.com/Felipe-Bobadilla)).
