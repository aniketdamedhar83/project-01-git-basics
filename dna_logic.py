# dna_logic.py

import random
from utils import DNA_BASES

def combine_dna(dna1, dna2, mutation_rate=0.1):
    new_dna = ""
    mutation_positions = []

    for i, (b1, b2) in enumerate(zip(dna1, dna2)):
        chosen = random.choice([b1, b2])

        if random.random() < mutation_rate:
            chosen = random.choice(DNA_BASES)
            mutation_positions.append(i)

        new_dna += chosen

    return new_dna, mutation_positions
