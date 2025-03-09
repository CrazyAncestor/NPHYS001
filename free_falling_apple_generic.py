import numpy as np
import matplotlib.pyplot as plt


#   Part 1.
#   Define the equation of motion of the system given the analytical form of the Hamiltonian equations of motion
def free_falling_apple_eom(dynamical_var, coefficients, t):
    x, p = dynamical_var
    m, g = coefficients
    dx_dt = p/m
    dp_dt = -m*g
    return np.array([dx_dt, dp_dt])

#   Part 2.
#   Solver for the time evolution of the dyanmical variables (coordinates, momenta, and etc.)
def generic_solver(system_eom, dynamical_var, coefficients, t, dt):
    var0 = np.copy(dynamical_var)
    k1 = system_eom(var0, coefficients, t)
    var1 = var0 + dt * k1
    return var1

#   Part 3.
#   Give coefficients, initial conditions

#       Give the coefficients in the equations of motion, like masses, spring constants, gravity, and etc.
m = 1.
g = 9.8

coefficients = m, g

#       Give the initial conditions of the dynamical variables
x0 = 0
p0 = 0

dynamical_var0 = x0, p0
dynamical_var_generic = dynamical_var0

#   Part 4.
#   Set the time condition and the main loop for the simulation

#       Give the time period we want to see the evolution of the system, also considering the time resolution
time = np.linspace(0., 10., 1000)
dt = time[1] - time[0]

#       Define the lists containing the dyanmical variables for different times
#           Initialize with the initial coordinate and momentum
coordinate_x_generic = [x0]
momentum_x_generic = [p0]

#       Main loop for solving the equations of motion
for i in range(len(time)-1):    #   Only need to update n-1 times since the lists has been initialized once
    #   Gerneric solver update
    dynamical_var_generic = generic_solver(free_falling_apple_eom, dynamical_var_generic, coefficients, time[i], dt)
    coordinate_x_generic.append(dynamical_var_generic[0])
    momentum_x_generic.append(dynamical_var_generic[1])

#   Part 5.
#   Plot the results
def analytical_results(t, x0, coefficients):
    m, g = coefficients
    x = x0 * np.ones(len(t)) - g * t**2 / 2.
    return x

plt.plot(time, coordinate_x_generic, label='generic solver')
plt.plot(time, analytical_results(time, x0, coefficients), label='analytical')
plt.legend()
plt.show()