# MINE4213-Taller2
Presentado por:

- Lina Maria Bejarano - 
- Juan Diego Enríquez - 
- Juan Manuel Rivera  - 201534131
- Johana Alejandra Rátiva - 202513844

# En el repositorio se encuentra:
1. Informe ejecutivo con el nombre: Proyecto_final_CD_entrega2.pdf
2. Presentación con el nombre: Proyecto-Ciencia-de-Datos-Aplicada_ENTREGA2.pdf
3. Cuaderno limpieza consolidado de jupyter: Analisis_exploratorio_consolidado.ipynb
4. Cuderno consolidado del EDA en jupyter: EDA_BD_trasplante_hepatico_JDER.ipynb
5. En la carpeta EDAs están los análisis individuales por cada integrante del grupo.
6. En la carpeta "Modelo de clasificación", se encuentra el cuaderno de los modelos y los archivos de la API
7. Diccionario con el nombre: Diccionario_de_datos_txHepato.xlsx
   
**Notas:** 
- El dataset sera enviado por correo por confidencialidad, se debe subir a la carpeta ya que se usó rutas relativas.
- El video entrega 2, se encuentra en la siguiente dirección: [Video 2](https://youtu.be/huUyG3ejCTM)

# Objetivo

El objetivo de este proyecto es explorar el dataset de datos clinicos de trasplantes hepaticos de la Fundación Santa Fe de Bogotá que cuenta con 736 registros y 286 varaibles. A partir de esta exploración se busca generar una base de datos limpia que permita el desarrollo de un tablero de control en Power BI que apoye la generación de reportes, la investigación clinica y mejore la toma de decisiones clinicas a partir de una comprensión mas clara del estado del paciente y sus posibles complicaciones postrasplante. Para ello se hará uso de la metodología ASUM-DM, analisis exploratorio y se implementará clasificación supervisada a partir de un algoritmo de random forest.   


# Alcance

EL siguiente proyecto de ciencia de datos hace uso de la metodología ASUM-DM, para esta entrega se abordaron las etapas de comprensión del negocio, enfoque analitico, recopilación y comprensión de los datos, preparación de los datos, modelado y evaluación del modelo, finalmente se propone una implementación de este mediante una API. 


## Fase 1: Comprensión del negocio

La Fundación Santa Fe de Bogotá cuenta con un servicio de cirugía hepatobiliar y de trasplantes que, de la mano de sus médicos rurales y bajo el acompañamiento de la médica Valentina Mejía, ha venido consolidando información de pacientes sometidos a trasplante hepático. Esta información, antes dispersa en diversas fuentes, fue integrada en una base de datos que representa un esfuerzo significativo de consolidación de variables operativas, clínicas, quirúrgicas y epidemiológicas. A partir de ella se busca:

* Desarrollar un panel interactivo o Power BI que permita consolidar esta base de datos, facilitando análisis clínico, operativo y epidemiológico de los pacientes sometidos a trasplante hepático. <br/>
* Facilitar la generación de reportes del año rural y obtener un panorama general poblacional de los trasplantes. <br/>
* Apoyar la toma de decisiones clínicas mediante una comprensión más clara del estado del paciente y sus posibles complicaciones postrasplante. <br/>
* Impulsar la investigación clínica al permitir el análisis de supervivencia y otros indicadores como factores de riesgo por grupos poblacionales o por año de trasplante.

Con la implementación de estre proyecto de datos se busca mejorar los KPIS de negocio

* Crecimiento anual en el numero de trasplantes. <br/> 
* Reducción del tiempo Fast Track. <br/>
* Disminución de la tasa de mortalidad postoperatoria. <br/>
* Reducción del tiempo de elaboración de reportes clinicos <br/>
* Aumento de la productividad cientrifica <br/>


## Fase 2: Enfoque analítico

### Ideación 

Dentro del servicio de cirugía hepatobiliar y de trasplantes, los médicos rurales constituyen el principal grupo de usuarios que alimenta y consulta la base de datos consolidada de trasplante hepático. Como se mencionó previamente, estos usuarios realizan dos usos principales de la información: generan reportes operativos y realizan investigación clínica. 
Adicionalmente, los médicos buscan que esta información sirva para identificar tempranamente factores de riesgo o vulnerabilidad frente a posibles complicaciones postrasplante. Sin embargo, esta necesidad se ve limitada por la complejidad y extensión de la base de datos, así como por problemas de calidad y limpieza de los registros, lo que dificulta el análisis y la identificación de patrones relevantes. Por eso se plantea como solución el uso de un tablero de control en power BI en donde se proponen 3 vistas principales.

* Panorama general de trasplantes: permite la generación de reportes operativos y la descripción poblacional de las cirugías realizadas. Incluye filtros por grupo etario, sexo, año y otras variables demográficas o clínicas de interés. <br/>
* Perfil del paciente: muestra información individual asociada a complicaciones (infección, cáncer postrasplante, inmunodeficiencia, entre otras) y a las variables identificadas como relevantes en las etapas de análisis exploratorio y modelamiento. Facilita la comprensión del estado del paciente y de sus riesgos asociados. <br/>
* Análisis de sobrevida poblacional: proyecta los resultados del análisis exploratorio, mostrando tasas de supervivencia por grupo etario, sexo o año de trasplante, junto con las dependencias o variables que más inciden en estos resultados.

Cabe aclarar, que antes de cargar la base de datos a power BI se desarrolla la elección de variables clínicas relevantes y un script en python para llevar a cabo un proceso de limpieza de la data. 

### Responsible

De acuerdo con la Resolución 8430 de 1993 del Ministerio de Salud de Colombia, la investigación realizada se clasifica como sin riesgo, dado que se emplean datos retrospectivos anonimizados.
El acceso a la información se realizó bajo un acuerdo de confidencialidad suscrito con el Servicio de Trasplantes, garantizando el uso ético, seguro y conforme a la Ley 1581 de 2012 sobre protección de datos personales.

Nota: Se anexa el acuerdo de confidencialidad firmado por las partes, el cual respalda el cumplimiento de los principios de confidencialidad, legalidad y finalidad en el manejo de la información.

### Enfoque analítico

El análisis se guía por tres preguntas de negocio principales: ¿Qué factores clínicos y demográficos se asocian con un mayor riesgo de complicación postoperatoria?
A partir de esta pregunta, se plantean hipótesis que sugieren que variables como edad, estadio del tumor, antecedentes de consumo (tabaquismo o alcohol), marcadores bioquímicos como la alfa-fetoproteína, obesidad, entre otras, pueden influir significativamente en la probabilidad de complicación. 
Se propone un enfoque analítico mixto que combina técnicas estadísticas y de visualización para caracterizar el panorama clínico, junto con modelos de machine learning supervisado para predecir complicaciones, experimentando con cuatro algoritmos: Regresión Logística, Random Forest, Árboles de Decisión y AdaBoost. Cada modelo será entrenado mediante búsqueda de hiperparámetros con GridSearchCV y validación cruzada estratificada.
La métrica principal para seleccionar el mejor modelo será el F1-score ponderado, dado que permite equilibrar precisión y recall en un contexto con desbalance de clases, maximizando la correcta identificación de pacientes con complicación sin incrementar excesivamente los falsos positivos. Adicionalmente se reportarán métricas complementarias como accuracy, precisión, recall y matriz de confusión, para evaluar la solidez y capacidad de cada modelo.


## Fase 3: Requisitos de datos

La base de datos de trasplantes hepáticos fue recibida el 25 de septiembre de 2025, con un total de 736 registros y 285 variables clínicas. A partir de esta información se diseñó una estrategia de priorización de datos estructurada en cuatro etapas principales:

1. Selección inicial basada en la pregunta de negocio: Se realizó una primera selección de variables relevantes (114 en total) que permitieron iniciar el proceso de limpieza y exploración. <br/>
2. Evaluación de completitud de datos: Tras el tratamiento de valores nulos, se aplicó un conteo de completitud utilizando la función df.info(). En esta etapa se eliminaron aquellas variables completamente vacías o con ausencia total de registros útiles. <br/>
3. Medición de variabilidad y consistencia de los datos: Se calculó la frecuencia relativa del valor más común sobre el total de datos no nulos. Se descartaron aquellas variables con baja variabilidad (por ejemplo, donde el valor más frecuente representaba más del 40% de los datos no nulos), así como aquellas con niveles de completitud muy bajos (entre 1% y 20%). <br/>
4. Validación con el stakeholder: Finalmente, se realizó una revisión conjunta para asegurar la pertinencia de las variables en función de los objetivos clínicos y analíticos, descartando aquellas que no fueron priorizadas por el equipo experto.

Como resultado, se obtuvo una base depurada de 121 variables seleccionadas para el proceso de limpieza avanzada y el análisis estadístico posterior.

A continuación se muestra el resultado de la estrategia de priorización de datos

![ Resultado_Priorizacion_Datos ](./Variables_Priorizadas.jpg)

Nota: Adjunto al repositorio se encuentra el diccionario de datos detallado.

## Fase 4: Comprensión de los datos

En esta etapa se realizaron actividad de limpieza y preparacón de datos como también analisis exploratorio univaraido y bivariado, los resultados se pueden encontrar en los cuadernillos adjuntos de limpieza de datos y EDA. 

## Fase 5: Preparación de los datos 

A partir del dataset original se aplicó una limpieza inicial que incluyó la estandarización de NaN, corrección de tipos de datos y depuración de rangos clínicos clave (p. ej., MELD ≤ 40, Child-Pugh a formato ordinal y filtros válidos para Causa_Tx_Renal y BMI). Además, se homogenizaron variables clínicas binarias para garantizar valores verdaderamente booleanos. (Enfermedad_Coronaria_Pre_Tx, Falla_Cardiaca_Pre_Tx, Infarto_Cardiaco_Pre_Tx, Diabetes_Mellitus_Pre_Tx, Hipertensión_Arterial_Pre_Tx, entre otros)
Con este dataset correctamente depurado se inició la etapa de preparación para el modelado, siguiendo estos pasos:
1.	Imputación de la variable ¿Complicación? A partir de: Tipo de complicaciones, infección posoperatoria,  Arritmia posoperatoria, Falla cardiaca, Infarto, # de complicaciones.
2.	Selección inicial de variables según su tipo (numéricas, booleanas y ordinales), priorizando únicamente aquellas que ya no requerían procesos adicionales de limpieza. Esto conformó un dataframe base df_model con 70 características.
3.	Procesamiento de variables categóricas, aplicando OneHotEncoder o MultiLabelBinarizer según correspondiera. Luego de integrarlas a df_model se obtuvieron 173 columnas.
4.	Filtro por porcentaje de no nulidad, aplicando un umbral mínimo del 16% para excluir columnas con demasiados valores faltantes.
Se obtuvo df_filtered con 143 columnas.
5.	Eliminación de filas completamente nulas, conservando únicamente registros con información útil. El resultado final fue un dataframe df_filtered con 466 filas y 143 columnas.
Este dataframe constituye la base final para el modelado y fue dividido en un 70% para entrenamiento y 30% para prueba.


## Fase 6: Estrategia de validación y selección de modelo

Para seleccionar el mejor, se implementó una estrategia de experimentación basada en validación cruzada estratificada de 5 folds, garantizando que cada partición mantuviera la proporción original de clases. Sobre esta estructura se aplicó una búsqueda de hiperparámetros mediante GridSearchCV evaluando 4 algoritmos (regresión logística, random forest, árboles de decisión y Adaboost) a partir de grillas específicas para cada modelo. La métrica empleada para comparar configuraciones fue el F1-score ponderado (F1_weighted), seleccionada por priorizar la identificación de pacientes con complicación sin incrementar excesivamente las predicciones de complicación a pacientes que realmente no la presentaron.

## Fase 7 Construcción y evaluación del modelo

El algoritmo Random Forest obtuvo el mejor desempeño, alcanzando un F1-Score ponderado de 69,3%.
Al analizar la matriz de confusión correspondiente a la muestra de 140 pacientes, se observa que el modelo logró identificar correctamente 59 de los 81 pacientes que sí presentaron complicaciones, lo que equivale a un recall del 73%, es decir, capturó la mayoría de los casos reales positivos.
Por otro lado, el modelo clasificó como complicados a 21 pacientes que en realidad no presentaron complicaciones, lo cual se refleja en una precisión del 74%, indicando que tres de cada cuatro predicciones positivas fueron correctas.
En conjunto, estos resultados muestran que Random Forest ofrece un equilibrio adecuado entre sensibilidad y precisión, siendo el algoritmo con mejor capacidad predictiva para este caso. 


# Conclusiones (insights)

* La variable “¿Complicación?” requiere un proceso adicional de depuración y homologación antes de avanzar hacia la modelación predictiva, ya que presenta inconsistencias con variables complementarias como:
Complejidad_asociada, #_de_complicaciones, arritmia_pop, falla_cardiaca, infección, rechazo_agudo, rechazo_cronico e infarto.
Estas discrepancias pueden afectar la coherencia de los resultados y la validez del modelo.

* Se evidencia que los pacientes que requieren soporte intraoperatorio tienden a presentar mayor frecuencia de complicaciones postoperatorias.
Este comportamiento podría estar relacionado con el uso de hormonas vasoactivas como vasopresina y noradrenalina, las cuales —según la literatura— podrían estar asociadas con la aparición de complicaciones tras el trasplante.

* Variables como Estadio y Grado_HCC muestran tendencias clínicas relevantes:

* Los estadios tumorales más avanzados y los grados histológicos más altos presentan mayor proporción de complicaciones y aunque no resultaron estadísticamente significativas, estas variables tienen sentido clínico, dado que una menor diferenciación celular suele asociarse con mayor agresividad tumoral y, en consecuencia, mayor riesgo de complicaciones.

* Dada la complejidad inherente a los datos clínicos, se recomienda continuar con análisis multivariados que permitan capturar la interacción entre variables y profundizar en la identificación de factores asociados a las complicaciones postoperatorias.


# Instrucciones de ejecución

La ejecución tiene el siguiente orden: Primero se ejecuta el cuadernillo de limpieza con el cual se obtendrá una sabana de datos limpia que será importada en el cuadernillo de Analisis exploratorio. En ambos cuadernillos se puede encontrar información relevante de la ejecución y interpretación de resultados. Para el caso de los ML y Power BI, en cada carpeta están sus instrucciones de ejecución.

# Dependencias

Antes de la ejecución asegurarse de tener las librerias

pandas numpy matplotlib seaborn scipy scikit-learn joblib lime shap



