# dna_logic.py

import random

def combine_dna(dna1, dna2, mutation_rate=0.1):
    new_dna = ""

    for base1, base2 in zip(dna1, dna2):
        # Randomly choose one base from parents
        chosen = random.choice([base1, base2])

        # Mutation logic
        if random.random() < mutation_rate:
            chosen = random.choice(["A", "T", "G", "C"])

        new_dna += chosen

    return new_dna
