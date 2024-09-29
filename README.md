# Cliente-Servidor
Ejercicio realizado en arquitectura cliente-servidor en 3 capas 
## Arquitectura
La arquitectura de 3 capas se compone de los siguientes 3 archivos:
 **Capa de Datos (`data_server.py`)**:Encargado de manejar y almacenar los datos.
 **Capa de Lógica (`logic_server.py`)**: Encargado de recibir las solicitudes del cliente y obtener la información desde la capa de datos.
 **Capa de Presentación (`client.py`)**: Interfaz la cual permite al usuario realizar solicitudes y visualizar los resultados.
 ## Requisitos Previos
 Antes de comenzar, se debe  tener instalado:
  **Python 3.11 o superior**.
  **Editor de Código** (**Visual Studio Code**.).
  ## Ejecución
  Para ejecutar el sistema, es necesario abrir tres terminales distintas en cmd y seguir estos pasos:
**Ejecutar el Servidor de Datos**:
 python data_server.py
 Lo anterior inicia el servidor de datos en el puerto `5001`.
 **Ejecutar el Servidor de Lógica**:
  Abrir una nueva terminal y ejecuta:
  python logic_server.py
  **Ejecutar el Cliente**:
  Abrir la tercera terminal y ejecuta:
  python client.py
  El cliente comenzará a comunicarse con el servidor de lógica
