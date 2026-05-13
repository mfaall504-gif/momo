import streamlit as st
st.title("MAMADOU FALL")
with st.sidebar:
   
    st.image("photo0.jpg", width=400)
    
    st.header("PROFIL")
    st.write("Nom: FALL")
    st.write("Prenom : MAMADOU")

    st.write("Date de naissance : 12/01/2004")
    st.write("Adresse : Yeumbeul Sud")
    
st.header("PARCOURS")
st.write("2025-2026: Licence 2 au DST2AN, POLYTECH DIAMNIADIO")
st.write("2023-2025: Licence 1 au DST2AN, POLYTECH DIAMNIADIO")
st.write("2021-2023: Eleve au Lyce EL HADJI IBRAHIMA DIOP de YEUMBEUL")
    
st.header("COMPETENCES")
st.write("Scientifiques: Biologie, Chimie, Nutrion, Geosciences")
st.write("Agricoles: Technique de mesure des parametres agronomiques, preparation et traitement des cultures a base de bio-pesticide et de bio-fertilisants, Desherbage, Tuttorage, Arrosage")
st.write("Suite bureautique: Word, Excel, PowerPoint")
st.write("Python, Anaconda, VScode")
st.write("Relationnelles et organisationnelles: Capacite a travailler en equipe, capacite a rediger des rapports, esprit critique")

st.header("PROJET")
st.write("GESTION DE PLANS DE MAIS A LA DIRECTION DE LA PROTECTION DES VEGETAUX DPV")
st.markdown("""La direction de la protection des vegetaux DPV est une structure technique centrale du Ministere de l' Agriculture et de l'Equipement Rural. Elle est chargee de surveiller, controler et lutter contre les organismes
    nuisibles aux cultures afin de garantir la sante des plantes et la production agricole.""") 
st.header("DESCRIPTION DU PROJET")
st.markdown("""Ce projet de stage d'impreniation d'un mois consister a assurer le suivi d'une culture de mais.Ma mission portait sur la protection phytosanitaire des plants et l'optimisation de leur rendement par une gestion rigoureuse des cultures.""")
st.image("photo1.jpg", width=400)
st.header("PARAMETRES A ETUDIER")
st.write("PARAMETRES AGRONOMIQUES : Diametre du tronc, nombre de feuilles et longueurs des feuilles")
st.write("PARAMETRES IMPLIQUANT LES RAVAGEURS : Cochi ou Aca")
st.header("IDENTIFICATION DES NEMATODES AU LABORATOIRE")
st.image("photo4.jpg", width=400)

st.header("TRAITEMENTS")
st.markdown("""PLANTES UTILISEES: NIIM (Adrata indica) qui joue un role de bio-pesticide et le LESSINA qui a un pouvoir de fertilisants et de bio-pesticides""")
st.write("T0: plante avec des substances chimiques")
st.write("T1: 1kg de NIIM et 5L d'eau")
st.write("T2: 1kg de LESSINA et 5L d'eau")
st.write("T3: 500g de NIIM et 500g de LESSINA et 5L d'eau")
st.image("photo2.jpg", width=400)
        
with st.sidebar:
    
    st.write("CONTACT:")
    st.write("Mail:mfaall504@gmail.com")
    st.write("Numero:777567529")
