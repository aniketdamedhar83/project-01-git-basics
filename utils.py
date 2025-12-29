# utils.py

import random

DNA_BASES = ["A", "T", "G", "C"]

def validate_dna(dna):
    return all(base in DNA_BASES for base in dna)

def normalize_dna(dna1, dna2):
    min_len = min(len(dna1), len(dna2))
    return dna1[:min_len], dna2[:min_len]

def generate_species_name(animal1, animal2):
    return animal1[:3] + animal2[-3:] + str(random.randint(100, 999))

def similarity_score(dna_a, dna_b):
    matches = sum(1 for x, y in zip(dna_a, dna_b) if x == y)
    return round((matches / len(dna_a)) * 100, 2)
