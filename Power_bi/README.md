# Dashboard (Power BI) 

El dashboard se realizó empleando Power BI, enlazado con un script de Python que permitió hacer la limpieza y la codificación de las variables necesarias para realizar el reporte. Este reporte se divide en tres hojas principales: Panorama general, panoramas y supervivencia poblacional. 

En la primera hoja, de panorama general se presentan características base de los pacientes como: edad, sexo, aseguradora y grupo sanguíneo. 

La segunda hoja, permite visualizar gracias a paneles interactivos, las diferentes variables presentes en los eventos de pre-trasplante, intra-quirúrgico y pos-trasplante de acuerdo con el número de trasplantes. Adicional a una visualización relacionada con los donantes del órgano.  

Finalmente, se muestra la hoja de supervivencia poblacional, que, de acuerdo con la edad, permite ver la supervivencia global de los pacientes a 1, 3 y 5 años, post cirugía.  

Es importante destacar que al abrir el Power BI es necesario tener instalada una versión de Python, ya que la sección de supervivencia poblacional se realizó con un script empleando este lenguaje de programación. Al abrir el Power BI, es necesario realizar la configuración. 

Indicaciones: Al abrir el Power BI, ir archivo > opciones y configuraciones > opciones > creación de scripts > seleccionar ruta y versión de Python > Aceptar.  

Adicional a esto, es necesario actualizar las rutas a la carpeta donde está el Power BI, dado que de lo contrario no permitirá actualizar.  

*Ruta:* Transformar Datos > Escoger tabla > Source  y actualizar el path en el codigo que aparece en la pestaña. 

Esta carpeta de BI, contiene todo lo necesario para ejecutar de manera local el proyecto. Contiene: Dashboard, Data, Scripts.
En dashboard esta presente el documento BI, que va a permitir visualizar el proyecto. Se incluyen además las imágenes del BI.
En Data se encuentran dos carpetas, Raw y Processed, en Raw, se encuentra la data cruda y en la segunda la data procesada.
Finalmente, en scripts, están los códigos python necesarios para el procesamiento de la data (Transplante_Hepatico) y en Calendar el necesario para incluir un calendario en BI, que permitiera visualizar las fechas. 





