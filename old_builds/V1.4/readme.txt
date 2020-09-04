V1.4:
• Se agrega la funcionalidad de descargar en carpetas.

Problemas a mejorar:
• No oculta contraseña.
• Verifica si hay actualizaciones pero se sigue ejecutando el programa, lo cual es un problema si hay un bug importante.

PROBLEMAS DETECTADOS LUEGO DE SUBIRSE <Por eso esta build se eliminó de releases>:
• Cuando se elige la opción de descargar por carpetas: Si la carpeta fue creada con un espacio al final del nombre provoca que Windows
no reconozca la carpeta al querer eliminarla. (SOLUCION: Comprimir las carpetas que se desean eliminar y tildar la opción "Eliminar luego de comprimir").