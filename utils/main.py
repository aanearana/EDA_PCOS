from funciones import cargar_datos, analizar_genetica, analizar_dieta, analizar_ejercicio, analizar_habitos
#Cargar datasets
df_genetica = cargar_datos("../data/pcos_genetica.csv")
df_dieta = cargar_datos("../data/pcos_diet.csv")
df_ejercicio = cargar_datos("../data/pcos_ejercicio.csv")
df_habitos = cargar_datos("../data/pcos_habitos.csv")

#Ejecutar análisis
analizar_genetica(df_genetica)
analizar_dieta(df_dieta)
analizar_ejercicio(df_ejercicio)
analizar_habitos(df_habitos)
