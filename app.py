import streamlit as st
from dataset import animal_dna
from dna_logic import combine_dna
from utils import (
    validate_dna,
    normalize_dna,
    generate_species_name,
    similarity_score
)

st.set_page_config(page_title="DNA Evolution Lab", layout="centered")

st.title("🧬 DNA Evolution Lab")
st.caption("Educational DNA fusion & mutation simulator")

animal1 = st.selectbox("Select Parent Animal 1", animal_dna.keys())
animal2 = st.selectbox("Select Parent Animal 2", animal_dna.keys())

mutation_rate = st.slider("Mutation Rate", 0.0, 0.5, 0.1)

if st.button("🧪 Generate New Species"):

    dna1 = animal_dna[animal1]
    dna2 = animal_dna[animal2]

    if not (validate_dna(dna1) and validate_dna(dna2)):
        st.error("Invalid DNA detected")
        st.stop()

    dna1, dna2 = normalize_dna(dna1, dna2)

    new_dna, mutations = combine_dna(dna1, dna2, mutation_rate)

    species_name = generate_species_name(animal1, animal2)

    st.subheader("🧬 Parent DNA")
    st.code(f"{animal1}: {dna1}")
    st.code(f"{animal2}: {dna2}")

    st.subheader("🧪 New Species")
    st.success(f"Species Name: **{species_name}**")
    st.code(new_dna)

    st.subheader("📊 Analysis")
    st.write(f"Similarity with {animal1}: {similarity_score(new_dna, dna1)}%")
    st.write(f"Similarity with {animal2}: {similarity_score(new_dna, dna2)}%")
    st.write(f"Total Mutations: {len(mutations)}")

    st.download_button(
        "⬇ Download DNA",
        data=new_dna,
        file_name=f"{species_name}_dna.txt"
    )
