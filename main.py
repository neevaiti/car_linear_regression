# Importer les bibliothèques nécessaires
import streamlit as st
import pandas as pd
import numpy as np
import pickle


# Charger le modèle pré-entraîné
with open('model_car.pkl', 'rb') as file:
    model = pickle.load(file)

df = pd.read_csv('./src/car_dataset_cleaned.csv')

# Obtenir la liste unique des marques
unique_marques = df['marque'].unique().tolist()
unique_modeles = df['modele'].unique().tolist()
unique_carburants = df['carburant'].unique().tolist()
unique_turbos = df['turbo'].unique().tolist()
unique_nombre_portes = df['nombre_portes'].unique().tolist()
unique_type_vehicules = df['type_vehicule'].unique().tolist()
unique_transmissions = df['transmission'].unique().tolist()
unique_emplacement_moteurs = df['emplacement_moteur'].unique().tolist()
unique_type_moteurs = df['type_moteur'].unique().tolist()
unique_systeme_carburants = df['systeme_carburant'].unique().tolist()
unique_etat_de_route = df['etat_de_route'].unique().tolist()


# Fonction pour effectuer les prédictions
def predict_price(features):
    prediction = model.predict(features)
    return prediction

# Faire en sorte que la marque sélectionnée détermine les modèles disponibles
brand_models = {}
for brand in df['marque'].unique():
    brand_models[brand] = df[df['marque'] == brand]['modele'].unique()

# Créer l'interface utilisateur
st.title("Estimation du prix d'une voiture")


empattement = st.number_input("Empattement")
# longueur_voiture = st.number_input("Longueur de voiture")
# largeur_voiture = st.number_input("Largeur de voiture")
# hauteur_voiture = st.number_input("Hauteur de voiture")
poids_vehicule = st.number_input("Poids du véhicule", min_value=500, max_value=7000, value=1500, step=100)
nombre_cylindres = st.number_input("Nombre de cylindres", min_value=2, max_value=12, value=4, step=1)
taille_moteur = st.number_input("Taille du moteur (l/100km)", min_value=1, max_value=12, value=4, step=1)
taux_alésage = st.number_input("Taux d'alésage")
# course = st.number_input("Course")
# taux_compression = st.number_input("Taux de compression")
chevaux = st.number_input("Chevaux")
tour_moteur = st.number_input("Tour du moteur", min_value=2000, max_value=10000, value=3500, step=500)
consommation_ville = st.number_input("Consommation en ville")
consommation_autoroute = st.number_input("Consommation sur autoroute")


# Créer les sélecteurs pour les caractéristiques catégorielles
marque = st.selectbox("Marque", list(brand_models.keys()))
modele = st.selectbox("Modèle", brand_models[marque])
carburant = st.selectbox("Carburant", unique_carburants)
turbo = st.selectbox("Turbo", unique_turbos)
nombre_portes = st.selectbox("Nombre de portes", unique_nombre_portes)
type_vehicule = st.selectbox("Type de véhicule", unique_type_vehicules)
transmission = st.selectbox("Transmission", unique_transmissions)
emplacement_moteur = st.selectbox("Emplacement du moteur", unique_emplacement_moteurs)
type_moteur = st.selectbox("Type de moteur", unique_type_moteurs)
systeme_carburant = st.selectbox("Système de carburant", unique_systeme_carburants)
etat_de_route = st.selectbox("État de la route", unique_etat_de_route)


predict_button = st.button("Prédire le prix")

if predict_button:

    input_data = pd.DataFrame(
        {
        "etat_de_route": [etat_de_route],
        "marque": [marque],
        "modele": [modele],
        "carburant": [carburant],
        "turbo": [turbo],
        "nombre_portes": [nombre_portes],
        "type_vehicule": [type_vehicule],
        "transmission": [transmission],
        "emplacement_moteur": [emplacement_moteur],
        "empattement": [empattement],
        "poids_vehicule": [poids_vehicule],
        "type_moteur": [type_moteur],
        "nombre_cylindres": [nombre_cylindres],
        "taille_moteur": [taille_moteur],
        "systeme_carburant": [systeme_carburant],
        "taux_alésage": [taux_alésage],
        # "course": [course],
        # "taux_compression": [taux_compression],
        "chevaux": [chevaux],
        "tour_moteur": [tour_moteur],
        "consommation_ville": [consommation_ville],
        "consommation_autoroute": [consommation_autoroute],
    }
        )
    
    prediction = model.predict(input_data)
    st.write(f"Le prix estimé de la voiture est de : {prediction[0]:.2f} €")