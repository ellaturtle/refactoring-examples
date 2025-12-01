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
def update_boids(boids):
    global boids_x, boids_y, boid_x_velocities, boid_y_velocities
    xs,ys,xvs,yvs= boids_x, boids_y, boid_x_velocities, boid_y_velocities
    boids_number = len(xs)

    # Fly towards the middle
    for current_boid in range(boids_number):
        for neighbor_boid in range(boids_number):
            xvs[current_boid]=xvs[current_boid]+(xs[neighbor_boid]-xs[current_boid])*0.01/boids_number
    for current_boid in range(boids_number):
        for neighbor_boid in range(boids_number):
            yvs[current_boid]=yvs[current_boid]+(ys[neighbor_boid]-ys[current_boid])*0.01/boids_number

    # Fly away from nearby boids
    for current_boid in range(boids_number):
        for neighbor_boid in range(boids_number):
            if (xs[neighbor_boid]-xs[current_boid])**2 + (ys[neighbor_boid]-ys[current_boid])**2 < 100:
                xvs[current_boid]=xvs[current_boid]+(xs[current_boid]-xs[neighbor_boid])
                yvs[current_boid]=yvs[current_boid]+(ys[current_boid]-ys[neighbor_boid])

    # Try to match speed with nearby boids
    for current_boid in range(boids_number):
        for neighbor_boid in range(boids_number):
            if (xs[neighbor_boid]-xs[current_boid])**2 + (ys[neighbor_boid]-ys[current_boid])**2 < 10000:
                xvs[current_boid]=xvs[current_boid]+(xvs[neighbor_boid]-xvs[current_boid])*0.125/boids_number
                yvs[current_boid]=yvs[current_boid]+(yvs[neighbor_boid]-yvs[current_boid])*0.125/boids_number

    # Move according to velocities
    for current_boid in range(boids_number):
        xs[current_boid]=xs[current_boid]+xvs[current_boid]
        ys[current_boid]=ys[current_boid]+yvs[current_boid]
