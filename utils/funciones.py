import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

#CARGAR DATOS
def cargar_datos(path):
#Carga un CSV
    return pd.read_csv(path)


#GENÉTICA
def analizar_genetica(df):
    #Genera un gráfico de barras dobles mostrando el porcentaje de PCOS
    df = df.copy()
    df["PCOS"] = pd.to_numeric(df["PCOS"], errors="coerce")

    habit_cols = [
        "Family_History_PCOS", "Hormonal_Imbalance", "Hyperandrogenism",
        "Hirsutism", "Mental_Health", "Conception_Difficulty",
        "Insulin_Resistance", "Diabetes", "Cardiovascular_Disease"
    ]

    #Guardamos los porcentajes en listas
    pcos_vals = []
    no_pcos_vals = []

    for col in habit_cols:
        con = df[df[col] == 1]
        pcos_con = int(round(con["PCOS"].mean() * 100))
        pcos_vals.append(pcos_con)
        no_pcos_vals.append(100 - pcos_con)

    # Posiciones en el eje Y
    y = np.arange(len(habit_cols))
    height = 0.4

    fig, ax = plt.subplots(figsize=(10, 6))

    #Barras horizontales
    ax.barh(y - height/2, pcos_vals, height, label='% con PCOS', color='salmon')
    ax.barh(y + height/2, no_pcos_vals, height, label='% sin PCOS', color='lightgreen')

    #Texto al lado de cada barra
    for i in range(len(habit_cols)):
        ax.text(pcos_vals[i] + 1, i - height/2, f"{pcos_vals[i]}%", va='center', fontsize=10)
        ax.text(no_pcos_vals[i] + 1, i + height/2, f"{no_pcos_vals[i]}%", va='center', fontsize=10)

    
    #Etiquetas y estilo
    ax.set_xlabel('Porcentaje')
    ax.set_title('Porcentaje de PCOS según características genéticas')
    ax.set_yticks(y)
    ax.set_yticklabels(habit_cols)
    ax.legend()

    plt.tight_layout()
    plt.savefig("../data/img/habitos_geneticos_horizontal.png", dpi=300)
    plt.show()


#DIETA
def analizar_dieta(df):
    df = df.copy()
    df["PCOS"] = pd.to_numeric(df["PCOS"], errors="coerce")

    # Columnas de dieta
    diet_cols = [col for col in df.columns if col.startswith("Diet_")]

    #Traducción de valores numéricos a etiquetas
    niveles = {
        0.00: "Nunca",
        0.25: "1–2 veces/sem",
        0.50: "3–4 veces/sem",
        0.75: "5–6 veces/sem",
        1.00: "Todos los días"
    }

    # Colores personalizados
    colores = ["salmon", "lightgreen", "lightblue", "orange", "violet", "cyan"]

    # Crear dataframes para cada grupo
    resultados_pcos1 = pd.DataFrame()
    resultados_pcos0 = pd.DataFrame()

    for col in diet_cols:
        temp = df.dropna(subset=[col])

        # Grupo PCOS = 1
        temp_pcos1 = temp[temp["PCOS"] == 1]
        freq1 = temp_pcos1[col].value_counts(normalize=True) * 100
        freq1.index = [niveles.get(round(i, 2), str(i)) for i in freq1.index]
        resultados_pcos1[col.replace("Diet_", "")] = freq1

        # Grupo PCOS = 0
        temp_pcos0 = temp[temp["PCOS"] == 0]
        freq0 = temp_pcos0[col].value_counts(normalize=True) * 100
        freq0.index = [niveles.get(round(i, 2), str(i)) for i in freq0.index]
        resultados_pcos0[col.replace("Diet_", "")] = freq0

    #Ordenar filas
    orden_niveles = list(niveles.values())
    resultados_pcos1 = resultados_pcos1.reindex(orden_niveles)
    resultados_pcos0 = resultados_pcos0.reindex(orden_niveles)

    # Heatmap comparativo
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), sharey=True)

    sns.heatmap(resultados_pcos1, ax=axes[0], annot=True, fmt=".1f",
                cmap=sns.color_palette(colores), cbar_kws={'label': '% dentro del grupo'})
    axes[0].set_title("PCOS = 1")
    axes[0].set_xlabel("Alimentos")
    axes[0].set_ylabel("Frecuencia de consumo")

    sns.heatmap(resultados_pcos0, ax=axes[1], annot=True, fmt=".1f",
                cmap=sns.color_palette(colores), cbar_kws={'label': '% dentro del grupo'})
    axes[1].set_title("PCOS = 0")
    axes[1].set_xlabel("Alimentos")
    axes[1].set_ylabel("")

    plt.tight_layout()
    plt.savefig("../data/img/pcos_vs_no_pcos_heatmap.png", dpi=300)
    plt.show()

    return resultados_pcos1, resultados_pcos0


#EJERCICIO
def analizar_ejercicio(df):
    df["PCOS"] = pd.to_numeric(df["PCOS"], errors="coerce")

    # Filtrar solo los casos con PCOS = 1
    df_pcos = df[df["PCOS"] == 1]

    # Crear grupos de frecuencia
    df_pcos["Freq_Group"] = pd.cut(
        df_pcos["Exercise_Frequency"],
        bins=[-0.1, 0.25, 0.5, 0.75, 1],
        labels=["Nunca", "Rara vez", "1-2/sem", "Frecuente"]
    )

    # Calcular porcentajes dentro de los casos con PCOS
    pcos_freq = df_pcos["Freq_Group"].value_counts(normalize=True).sort_index() * 100
    pcos_dur = df_pcos["Exercise_Duration"].value_counts(normalize=True).sort_index() * 100
    pcos_ben = df_pcos["Exercise_Benefit"].value_counts(normalize=True).sort_index() * 100

    # Etiquetas personalizadas
    benefit_labels = {
        0: "Nada",
        0.5: "Algo",
        1: "Mucho"
    }

    duration_labels = {
        '0': "Nada",
        '1-29': "-30 minutos",
        '30' : '30 minutos',
        '31-59' : '+30 minutos',
        '60' : '1 hora'
    }

    mis_colores = ["salmon", "lightgreen", "lightblue", "orange", "violet"]

    fig, axes = plt.subplots(1, 3, figsize=(25, 10))

    # Frecuencia
    if not pcos_freq.empty:
        axes[0].pie(
            pcos_freq.values,
            labels=pcos_freq.index,
            autopct="%1.1f%%",
            textprops={'fontsize': 10},
            colors=mis_colores[:len(pcos_freq)]
        )
    axes[0].set_title("Frecuencia de ejercicio (mujeres con PCOS)", fontsize=24)

    # Duración
    if not pcos_dur.empty:
        axes[1].pie(
            pcos_dur.values,
            labels=[duration_labels.get(i, str(i)) for i in pcos_dur.index],
            autopct="%1.1f%%",
            textprops={'fontsize': 10},
            colors=mis_colores[:len(pcos_dur)]
        )
    axes[1].set_title("Duración del ejercicio (mujeres con PCOS)", fontsize=24)

    # Beneficio percibido
    if not pcos_ben.empty:
        axes[2].pie(
            pcos_ben.values,
            labels=[benefit_labels.get(i, str(i)) for i in pcos_ben.index],
            autopct="%1.1f%%",
            textprops={'fontsize': 10},
            colors=mis_colores[:len(pcos_ben)]
        )
    axes[2].set_title("Beneficio percibido del ejercicio (mujeres con PCOS)", fontsize=24)

    plt.tight_layout()
    plt.savefig("../data/img/ejercicio_pcos.png", dpi=300)
    plt.show()


#HÁBITOS
def analizar_habitos(df):
    bin_cols = ["Stress_Level", "Smoking", "PCOS_Medication"]
    resultados = {}

    df["PCOS"] = pd.to_numeric(df["PCOS"], errors="coerce")

    for col in bin_cols:
        con = df[df[col] == 1]
        sin = df[df[col] == 0]

        pcos_con = con["PCOS"].mean() * 100
        pcos_sin = sin["PCOS"].mean() * 100

        resultados[col] = [pcos_con, pcos_sin]

    res_df = pd.DataFrame(resultados, index=["Sí", "No"]).T

    res_df.plot(kind="bar", figsize=(8, 5), color=['salmon', 'lightgreen'])
    plt.title("Influencia de los hábitos en la presencia de PCOS")
    plt.xlabel("Hábito")
    plt.ylabel("% de mujeres con PCOS")
    plt.xticks(rotation=0, fontsize=9)
    plt.legend(title="Tienen el hábito")
    plt.grid(axis="y", linestyle="--", alpha=0.6)
    plt.tight_layout()
    plt.savefig("../data/img/pcos_habitos.png", dpi=300)
    plt.show()
