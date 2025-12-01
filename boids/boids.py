"""
A deliberately bad implementation of 
[Boids](http://dl.acm.org/citation.cfm?doid=37401.37406)
for use as an exercise on refactoring.
This code simulates the swarming behaviour of bird-like objects ("boids").
"""

from matplotlib import pyplot as plt
from matplotlib import animation

import random

# Set initial position for the two boids
boids_x=[random.uniform(-450,50.0) for x in range(50)]
boids_y=[random.uniform(300.0,600.0) for x in range(50)]

# Set initial velocities for the two boids 
boid_x_velocities=[random.uniform(0,10.0) for x in range(50)]
boid_y_velocities=[random.uniform(-20.0,20.0) for x in range(50)]

boids=(boids_x,boids_y,boid_x_velocities,boid_y_velocities)

# Create a function to update the position and velocity of the boids
def update_boids(boids_tuple):
    positions_x, positions_y, velocities_x, velocities_y = boids_tuple
    boids_number = len(positions_x)
    dx = positions_x[neighbor_boid] - positions_x[current_boid]
    dy = positions_y[neighbor_boid] - positions_y[current_boid]

    # Fly towards the middle
    for current_boid in range(boids_number):
        for neighbor_boid in range(boids_number):
            velocities_x[current_boid] =+ (dx)*0.01/boids_number

    for current_boid in range(boids_number):
        for neighbor_boid in range(boids_number):
            velocities_y[current_boid] =+ (dy)*0.01/boids_number

    # Fly away from nearby boids
    for current_boid in range(boids_number):
        for neighbor_boid in range(boids_number):
            if (dx)**2 + (dy)**2 < 100:
                velocities_x[current_boid] += (-(dx))
                velocities_y[current_boid] += (-(dy))

    # Try to match speed with nearby boids
    for current_boid in range(boids_number):
        for neighbor_boid in range(boids_number):
            if (dx)**2 + (dy)**2 < 10000:
                velocities_x[current_boid] += (velocities_x[neighbor_boid]-velocities_x[current_boid])*0.125/boids_number
                velocities_y[current_boid] += (velocities_y[neighbor_boid]-velocities_y[current_boid])*0.125/boids_number

    # Move according to velocities
    for current_boid in range(boids_number):
        positions_x[current_boid] += velocities_x[current_boid]
        positions_y[current_boid] += velocities_y[current_boid]

    return(positions_x, positions_y, velocities_x, velocities_y)
