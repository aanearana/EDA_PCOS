EDA: PCOS — Exploratory Data Analysis del Síndrome de Ovario Poliquístico

📖 Descripción del proyecto

El Síndrome de Ovario Poliquístico (PCOS) es un trastorno hormonal que afecta a mujeres en edad reproductiva. Se caracteriza por un desequilibrio hormonal —particularmente por niveles elevados de andrógenos— y, en muchos casos, por la presencia de quistes en los ovarios.

Este proyecto realiza un Análisis Exploratorio de Datos (EDA) con el objetivo de comprender mejor los factores y patrones asociados al PCOS, explorando la influencia de variables como la edad, la dieta, el ejercicio y los niveles hormonales.

El análisis se realiza sobre un dataset proveniente de Kaggle: 📂 Fuente: Diet, Exercise, and PCOS Insights (Kaggle)

🧩 Estructura del dataset

El dataset contiene 173 registros y 36 columnas, que abarcan variables relacionadas con la salud, hábitos de vida y antecedentes médicos de mujeres con y sin PCOS.

Principales grupos de variables: Categoría Variables principales Datos personales y físicos Age, Weight_kg, Height_ft, Marital_Status Aspectos médicos PCOS, Family_History_PCOS, Hormonal_Imbalance, Hirsutism, Diabetes, Cardiovascular_Disease Salud mental Mental_Health, Childhood_Trauma, Stress_Level Hábitos alimenticios Diet_Fruits, Diet_Vegetables, Diet_Sweets, Diet_Fats, Vegetarian, Diet_Multivitamin Ejercicio y estilo de vida Exercise_Frequency, Exercise_Type, Exercise_Duration, Sleep_Hours, Smoking Tratamiento PCOS_Medication 

🎯 Objetivo del análisis

El proyecto busca detectar patrones y relaciones entre distintos factores que puedan influir en la aparición del PCOS, a través de cuatro hipótesis principales:

Factor genético: La genética influye en la probabilidad de padecer PCOS.

Factor alimenticio: Mantener una dieta equilibrada reduce la probabilidad de desarrollar PCOS.

Factor de ejercicio: Las mujeres con mayor frecuencia de ejercicio presentan menor incidencia de PCOS.

Hábitos generales: Dormir bien, evitar el estrés y no fumar disminuyen el riesgo de PCOS.

🧹 Limpieza y preparación de datos

Antes del análisis, se realizó una limpieza exhaustiva del dataset:

Eliminación de espacios y tabulaciones en nombres de columnas.

Conversión de valores categóricos (Yes/No) a binarios (1/0).

Reagrupamiento de variables continuas (Age, Weight_kg, Height_ft) en rangos.

Corrección de formatos numéricos (cambio de comas a puntos).

Creación de nuevas columnas con rangos agrupados: Weight_Range y Height_range.

Además, se generaron subconjuntos del dataset para cada hipótesis, facilitando el análisis temático.

🧬 Hipótesis 1: Factor Genético

Objetivo: Analizar la relación entre los antecedentes familiares, desequilibrios hormonales y otros indicadores médicos con la presencia de PCOS.

Variables analizadas: Family_History_PCOS, Hormonal_Imbalance, Hyperandrogenism, Hirsutism, Mental_Health, Insulin_Resistance, Diabetes, Cardiovascular_Disease.

Hallazgos principales:

El 22.09% del total de la muestra presenta PCOS.

Las mujeres con antecedentes familiares de PCOS tienen el doble de probabilidad de padecerlo.

La resistencia a la insulina y la diabetes presentan una fuerte correlación positiva con el PCOS.

El desequilibrio hormonal y el hiperandrogenismo son los factores más determinantes.

Visualización: Gráfico de barras horizontales que muestra el porcentaje de PCOS según cada característica genética.

🥗 Hipótesis 2: Factor Alimenticio

Objetivo: Evaluar si una dieta saludable se asocia con una menor probabilidad de desarrollar PCOS.

Transformaciones realizadas:

Las variables dietéticas (0–7 días/semana) se normalizaron a escala binaria (0–1).

Se crearon funciones automáticas para aplicar el mapeo y mantener consistencia.

Variables incluidas: Diet_Bread_Cereals, Diet_Milk_Products, Diet_Fruits, Diet_Vegetables, Diet_Sweets, Diet_Fried_Food, Diet_Tea_Coffee, Diet_Multivitamin, Vegetarian.

Correlaciones destacadas:

Variable Correlación con PCOS Diet_Sweets +0.15 Diet_Fried_Food +0.13 Diet_Fruits −0.11 Diet_Vegetables −0.03

Conclusión: Aunque se observa que las personas con PCOS parecen tener una dieta más saludable (más frutas y menos frituras o dulces), esto no apoya la hipótesis de que una buena alimentación reduce el riesgo de PCOS.

🏋️‍♀️ Hipótesis 3: Factor de Ejercicio

Objetivo: Analizar cómo la frecuencia, el tipo y la duración del ejercicio físico influyen en la incidencia del PCOS.

Variables:
Exercise_Frequency, Exercise_Type, Exercise_Duration.

Hallazgos:

Las mujeres que realizan ejercicio 3–4 veces por semana muestran menores tasas de PCOS.

La práctica regular de ejercicio moderado o aeróbico está asociada con una menor probabilidad de desarrollar el síndrome.

Conclusión:

Aunque la mayoría no realiza ejercicio regularmente, se observa que quienes lo practican con mayor frecuencia presentan menos casos de PCOS, lo que apoya parcialmente la hipótesis de que la actividad física reduce su probabilidad de aparición.

🌙 Hipótesis 4: Hábitos Generales

Objetivo: Analizar el nivel de estrés, el tabaquismo y la medicación cómo afectan la incidencia del PCOS.

Variables:
Stress_Level, PCOS_Medication, Smoking.

Hallazgos:

Altos niveles de estrés están relacionados con un aumento del riesgo.

Conclusión: 

Las personas con PCOS tienden a fumar más, presentar mayores niveles de estrés y consumir más medicación, lo que respalda la hipótesis de que mantener buenos hábitos y evitar el consumo de tabaco se asocia con una menor probabilidad de desarrollar PCOS.

📊 Librerías utilizadas

import pandas as pd

import numpy as np

import matplotlib.pyplot as plt

import seaborn as sns

💾 Archivos generados

Durante el proyecto se exportaron subconjuntos limpios de los datos:

pcos_genetica.csv → Datos del factor genético

pcos_diet.csv → Datos del factor alimenticio

Cleaned-Data.csv → Dataset original limpiado

📈 Resultados generales

La prevalencia de PCOS aumenta significativamente en mujeres de 25 a 30 años.

Factores metabólicos y hormonales (como insulina o hiperandrogenismo) muestran las correlaciones más altas.

Los hábitos saludables (alimentación equilibrada, ejercicio regular y sueño adecuado) se asocian con una menor incidencia del síndrome.

📚 Conclusión

Este análisis exploratorio demuestra cómo factores genéticos, hormonales y de estilo de vida influyen conjuntamente en la aparición del Síndrome de Ovario Poliquístico (PCOS). El trabajo sienta las bases para futuros modelos predictivos o de clasificación que permitan identificar perfiles de riesgo y fomentar hábitos preventivos entre las mujeres jóvenes.

🎨 Presentacion

https://prezi.com/view/V1YRoOTTgDxrATATTTL2/?referral_token=yEGlRYlnB3FN


👩‍💻 Autoría

Proyecto de EDA: PCOS Elaborado por: Ane Arana Alonso Dataset original: Kaggle – Diet, Exercise and PCOS Insights Lenguaje: Python 3 Entorno: Jupyter Notebook
