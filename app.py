# app.py

import streamlit as st
from dataset import animal_dna
from dna_logic import combine_dna

st.set_page_config(page_title="DNA Fusion Simulator", layout="centered")

st.title("🧬 DNA Fusion Simulator")
st.write("Combine DNA of two animals to create a new species (Simulation)")

# Dropdowns
animal1 = st.selectbox("Select First Animal", animal_dna.keys())
animal2 = st.selectbox("Select Second Animal", animal_dna.keys())

mutation_rate = st.slider("Mutation Rate", 0.0, 0.5, 0.1)

if st.button("Generate New Species DNA"):
    dna1 = animal_dna[animal1]
    dna2 = animal_dna[animal2]

    new_dna = combine_dna(dna1, dna2, mutation_rate)

    st.subheader("🧬 Parent DNA")
    st.text(f"{animal1}: {dna1}")
    st.text(f"{animal2}: {dna2}")

    st.subheader("🧪 New Species DNA")
    st.code(new_dna)

    st.success("New DNA Generated Successfully!")
