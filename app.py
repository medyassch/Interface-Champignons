import streamlit as st
import numpy as np
import pickle
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

model = pickle.load(open(r"C:\Users\ACH\OneDrive - OFPPT\Documents\AI\Machine_Learning\Projet_Mushrooms\random_forest_model.pkl", "rb"))

st.title("Prédiction de champignons")
st.header("Veuillez entrer les informations sur le champignon :")

# Forme du chapeau
cap_shape = st.selectbox('Forme du chapeau', ('Conical', 'Convex', 'Bell', 'Flat', 'Knobbed', 'Sunken'))
if cap_shape == 'Conical':
    cap_shape = 1
elif cap_shape == 'Convex':
    cap_shape = 2
elif cap_shape == 'Bell':
    cap_shape = 0
elif cap_shape == 'Flat':
    cap_shape = 3
elif cap_shape == 'Knobbed':
    cap_shape = 4
else:
    cap_shape = 5

# Surface du chapeau
cap_surface = st.selectbox('Surface du chapeau', ('Fibrous', 'Grooves', 'Scaly', 'Smooth'))
if cap_surface == 'Fibrous':
    cap_surface = 0
elif cap_surface == 'Grooves':
    cap_surface = 1
elif cap_surface == 'Scaly':
    cap_surface = 2
else:
    cap_surface = 3

# Couleur du chapeau
cap_color = st.selectbox('Couleur du chapeau', ('Brown', 'Buff', 'Cinnamon', 'Gray', 'Green', 'Pink', 'Purple', 'Red', 'White', 'Yellow'))
if cap_color == 'Brown':
    cap_color = 0
elif cap_color == 'Buff':
    cap_color = 1
elif cap_color == 'Cinnamon':
    cap_color = 2
elif cap_color == 'Gray':
    cap_color = 3
elif cap_color == 'Green':
    cap_color = 4
elif cap_color == 'Pink':
    cap_color = 5
elif cap_color == 'Purple':
    cap_color = 6
elif cap_color == 'Red':
    cap_color = 7
elif cap_color == 'White':
    cap_color = 8
else:
    cap_color = 9

# Meurtrissures
bruises = st.selectbox('Présence de meurtrissures', ('Yes', 'No'))
bruises = 0 if bruises == 'Yes' else 1

# Odeur
Odur = st.selectbox('Odeur', ('Almond', 'Anise', 'Creosote', 'Fishy', 'Foul', 'Musty', 'Pungent', 'Spicy', 'Other'))
if Odur == 'Almond':
    Odur = 0
elif Odur == 'Anise':
    Odur = 1
elif Odur == 'Creosote':
    Odur = 2
elif Odur == 'Fishy':
    Odur = 3
elif Odur == 'Foul':
    Odur = 4
elif Odur == 'Musty':
    Odur = 5
elif Odur == 'Pungent':
    Odur = 6
elif Odur == 'Spicy':
    Odur = 7
else:
    Odur = 8

# Attachement des lamelles
gill_attachment = st.selectbox('Attachement des lamelles', ('Attached', 'Free'))
gill_attachment = 0 if gill_attachment == 'Attached' else 1

# Espacement des lamelles
gill_spacing = st.selectbox('Espacement des lamelles', ('Close', 'Crowded'))
gill_spacing = 0 if gill_spacing == 'Close' else 1

# Taille des lamelles
gill_size = st.selectbox('Taille des lamelles', ('Broad', 'Narrow'))
gill_size = 0 if gill_size == 'Broad' else 1

# Couleur des lamelles
gill_color = st.selectbox('Couleur des lamelles', ('Black', 'Brown', 'Buff', 'Chocolate', 'Gray', 'Green', 'Orange', 'Pink', 'Purple', 'Red', 'White', 'Yellow'))
if gill_color == 'Black':
    gill_color = 0
elif gill_color == 'Brown':
    gill_color = 1
elif gill_color == 'Buff':
    gill_color = 2
elif gill_color == 'Chocolate':
    gill_color = 3
elif gill_color == 'Gray':
    gill_color = 4
elif gill_color == 'Green':
    gill_color = 5
elif gill_color == 'Orange':
    gill_color = 6
elif gill_color == 'Pink':
    gill_color = 7
elif gill_color == 'Purple':
    gill_color = 8
elif gill_color == 'Red':
    gill_color = 9
elif gill_color == 'White':
    gill_color = 10
else:
    gill_color = 11

# Forme du pied
stalk_shape = st.selectbox('Forme du pied', ('Enlarging', 'Tapering'))
stalk_shape = 0 if stalk_shape == 'Enlarging' else 1

# Base du pied
stalk_root = st.selectbox('Base du pied', ('Bulbous', 'Club', 'Cup', 'Equal', 'Rhizomorphs', 'Rooted', 'Other'))
if stalk_root == 'Bulbous':
    stalk_root = 0
elif stalk_root == 'Club':
    stalk_root = 1
elif stalk_root == 'Cup':
    stalk_root = 2
elif stalk_root == 'Equal':
    stalk_root = 3
elif stalk_root == 'Rhizomorphs':
    stalk_root = 4
elif stalk_root == 'Rooted':
    stalk_root = 5
else:
    stalk_root = 6

# Surface du pied au-dessus de l’anneau
stalk_surface_above_ring = st.selectbox("Surface du pied au-dessus de l'anneau", ('Fibrous', 'Scaly', 'Silky', 'Smooth'))
if stalk_surface_above_ring == 'Fibrous':
    stalk_surface_above_ring = 0
elif stalk_surface_above_ring == 'Scaly':
    stalk_surface_above_ring = 1
elif stalk_surface_above_ring == 'Silky':
    stalk_surface_above_ring = 2
else:
    stalk_surface_above_ring = 3

# Surface du pied sous l’anneau
stalk_surface_below_ring = st.selectbox("Surface du pied sous l'anneau", ('Fibrous', 'Scaly', 'Silky', 'Smooth'))
if stalk_surface_below_ring == 'Fibrous':
    stalk_surface_below_ring = 0
elif stalk_surface_below_ring == 'Scaly':
    stalk_surface_below_ring = 1
elif stalk_surface_below_ring == 'Silky':
    stalk_surface_below_ring = 2
else:
    stalk_surface_below_ring = 3

# Couleur du pied au-dessus de l’anneau
stalk_color_above_ring = st.selectbox("Couleur du pied au-dessus de l'anneau", ('Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'))
stalk_color_above_ring = ['Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'].index(stalk_color_above_ring)

# Couleur du pied sous l’anneau
stalk_color_below_ring = st.selectbox("Couleur du pied sous l'anneau", ('Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'))
stalk_color_below_ring = ['Brown', 'Buff', 'Cinnamon', 'Gray', 'Orange', 'Pink', 'Red', 'White', 'Yellow'].index(stalk_color_below_ring)

# Couleur du voile
veil_color = st.selectbox("Couleur du voile", ('Brown', 'Orange', 'White', 'Yellow'))
veil_color = ['Brown', 'Orange', 'White', 'Yellow'].index(veil_color)

# Nombre d’anneaux
ring_number = st.selectbox("Nombre d'anneaux", ('One', 'Two', 'Other'))
if ring_number == 'Other':
    ring_number = 0
elif ring_number == 'One':
    ring_number = 1
else:
    ring_number = 2

# Type d’anneau
ring_type = st.selectbox("Type d'anneau", ('Cobwebby', 'Evanescent', 'Flaring', 'Large', 'Pendant', 'Other'))
if ring_type == 'Cobwebby':
    ring_type = 0
elif ring_type == 'Evanescent':
    ring_type = 1
elif ring_type == 'Flaring':
    ring_type = 2
elif ring_type == 'Large':
    ring_type = 3
elif ring_type == 'Pendant':
    ring_type = 4
else:
    ring_type = 5

# Couleur de l'empreinte de spores
spore_print_color = st.selectbox("Couleur de l'empreinte de spores", ('Black', 'Brown', 'Buff', 'Chocolate', 'Green', 'Orange', 'Purple', 'White', 'Yellow'))
spore_print_color = ['Black', 'Brown', 'Buff', 'Chocolate', 'Green', 'Orange', 'Purple', 'White', 'Yellow'].index(spore_print_color)

# Population
population = st.selectbox("Taille de la population", ('Abundant', 'Clustered', 'Numerous', 'Scattered', 'Several', 'Solitary'))
population = ['Abundant', 'Clustered', 'Numerous', 'Scattered', 'Several', 'Solitary'].index(population)

# Habitat
habitat = st.selectbox("Habitat", ('Grasses', 'Leaves', 'Meadows', 'Paths', 'Waste', 'Woods'))
habitat = ['Grasses', 'Leaves', 'Meadows', 'Paths', 'Waste', 'Woods'].index(habitat)

# Valeur fixe
veil_type = 0

# Prédiction
if st.button('Prédire'):
    features = np.array([[habitat, population, spore_print_color, stalk_root, stalk_shape, ring_number,
                          ring_type, veil_color, stalk_color_below_ring, stalk_color_above_ring, veil_type,
                          stalk_surface_below_ring, stalk_surface_above_ring, gill_color, gill_size,
                          gill_spacing, gill_attachment, cap_color, bruises, Odur, cap_surface, cap_shape]])
    
    prediction = model.predict(features)
    st.success(f"Résultat de la prédiction : {int(prediction)}")

    # with st.expander("📝 Données saisies"):
    #     st.write(f"- **Forme du chapeau** : {population}")
    #     st.write(f"- **Surface du chapeau** : {habitat}")
    #     st.write(f"- **Couleur du chapeau** : {stalk_color_below_ring}")
    #     st.write(f"- **Présence de meurtrissures** : {bruises}")


# Visualisation des données
data = pd.read_csv(r"C:\Users\ACH\OneDrive - OFPPT\Documents\AI\Machine_Learning\Projet_Mushrooms\mushrooms.csv")
st.title("Visualisation des données sur les champignons")


st.header("Distribution de la surface des chapeaux")
fig1, ax1 = plt.subplots(figsize=(9, 4))
bp_counts = data['cap-surface'].value_counts()
ax1.pie(bp_counts, labels=bp_counts.index, colors=['gold', 'lightblue', 'lightgreen', 'gray'], autopct='%1.1f%%')
ax1.set_title('Distribution de la surface des chapeaux')
st.pyplot(fig1)


st.header("Distribution des champignons avec et sans ecchymoses")
bruises_class = data.groupby(['class', 'bruises']).size().reset_index(name='count')
fig2, ax2 = plt.subplots()
sns.histplot(data=bruises_class, x='bruises', hue='class', weights='count', multiple='stack', ax=ax2)
ax2.set_title('Champignons avec/sans ecchymoses')
ax2.set_xlabel('Ecchymoses')
ax2.set_ylabel('Nombre')
st.pyplot(fig2)


st.header("Taille des lamelles selon la classe")
fig3, ax3 = plt.subplots(figsize=(8, 5))
sns.countplot(data=data, x='gill-size', hue='class', palette='Set2', ax=ax3)
ax3.set_title('Comparaison de la taille des lamelles')
ax3.set_xlabel('Taille des lamelles (gill-size)')
ax3.set_ylabel('Nombre')
ax3.legend(title='Classe', labels=['Comestible (e)', 'Toxique (p)'])
st.pyplot(fig3)


st.header("Fréquence des types d'anneaux")
fig4, ax4 = plt.subplots(figsize=(10, 6))
sns.countplot(data=data, x='ring-type', palette='Set3', ax=ax4)
ax4.set_title("Fréquence des types d'anneaux")
ax4.set_xlabel("Type d'anneau (ring-type)")
ax4.set_ylabel('Nombre')
st.pyplot(fig4)


st.header("Visualisation dynamique : distribution d'une variable")
col_pour_viz = st.selectbox("Choisir une variable à visualiser", data.columns)
fig5, ax5 = plt.subplots()
sns.countplot(x=col_pour_viz, data=data, ax=ax5)
ax5.set_title(f'Distribution de {col_pour_viz}')
ax5.set_ylabel('Nombre')
st.pyplot(fig5)


st.header("Nuage de points entre deux variables")
cols_categoric = data.columns.tolist()
x_col = st.selectbox("Choisir la première variable", cols_categoric, index=0)
y_col = st.selectbox("Choisir la deuxième variable", cols_categoric, index=1)

if x_col != y_col:
    fig6, ax6 = plt.subplots()
    sns.stripplot(data=data, x=x_col, y=y_col, alpha=0.5, ax=ax6)
    ax6.set_title(f"La Relation entre {x_col} et {y_col}")
    st.pyplot(fig6)


st.markdown(
    """
    <style>
    .stApp {
        background-image:linear-gradient(rgba(0,0,0,0.5), rgba(0,0,0,0.5)), url("https://plus.unsplash.com/premium_photo-1704737966313-746586e51913?w=600&auto=format&fit=crop&q=60&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8MXx8bXVzaHJvb218ZW58MHx8MHx8fDA%3D");
        background-size: cover;
        background-repeat: no-repeat;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown("---")  # Ligne de séparation

st.markdown("""
### ℹ️ À propos de cette application
Cette application utilise un modèle de machine learning pour prédire si un champignon est comestible ou toxique, en fonction de ses caractéristiques visuelles et biologiques.

**Projet développé par :** Mohamed Yassine Chalbat  
**Technologies utilisées :** Streamlit, Random Forest, Python  
**Source des données :** [Kaggle - Mushroom Dataset](https://www.kaggle.com/uciml/mushroom-classification)
""")
