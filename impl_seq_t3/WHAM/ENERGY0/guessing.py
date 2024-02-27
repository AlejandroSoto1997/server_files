#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 22 09:11:02 2024

@author: alejandrosoto
"""
import random
import numpy as np
from scipy.optimize import minimize

# Define the number of pairs of bases
num_pairs = 27

# Generate random initial values for weights
initial_weights = [random.uniform(0, 100) for _ in range(num_pairs)]

# Define the objective function to minimize
def objective_function(weights):
    # Here you would put your code to run simulations and evaluate the free energy
    # For now, let's just return a random value as an example
    return random.uniform(0, 100)

# Define bounds for weights (optional but can be useful to prevent weights from becoming negative)
bounds = [(0, None) for _ in range(num_pairs)]

# Run optimization
result = minimize(objective_function, initial_weights, bounds=bounds)

# Extract optimized weights
optimized_weights = result.x

# Print optimized weights
for i, weight in enumerate(optimized_weights):
    print(f"{i} {weight}")
    
    
# Nombre del archivo de salida
output_file = "wfile.txt"

# Escribir los pesos optimizados en el archivo de salida
with open(output_file, "w") as file:
    for i, weight in enumerate(optimized_weights):
        file.write(f"{i} {weight}\n")

print(f"Optimized weights saved to {output_file}")


