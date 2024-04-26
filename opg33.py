# from sympy import *
import numpy as np
from numpy import cos, sin, pi
def intersect_cell_oneliner(i, j, a, N, rho, phi):
    return ((2*a*(i-1)/N-a < (rho-(2*a*(j-1)/N-a)*cos(phi))/sin(phi) <= 2*a*i/N-a) or (2*a*(i-1)/N-a < ((rho-(2*a*j/N-a)*cos(phi))/sin(phi)) <= 2*a*i/N-a))

def intersect_cell(i, j, a ,N, rho, phi):
    ## For vertikale linjer:
    ## Udregn y-værdier for l i intervalendepunkterne:
    lower_x_vert = (rho-(2*a*(j-1)/N-a)*cos(phi))/sin(phi) 
    upper_x_vert = (rho-(2*a*j/N-a)*cos(phi))/sin(phi)

    ## Udregn y-værdier for C_ij:
    lower_y_vert = 2*a*(i-1)/N-a
    upper_y_vert = 2*a*i/N-a

    ## For horisontale linjer:
    lower_x_hor = (rho-(2*a*(i-1)/N-a)*sin(phi))/cos(phi)
    upper_x_hor = (rho-(2*a*i/N-a)*sin(phi))/cos(phi)

    lower_y_hor = 2*a*(j-1)/N-a
    upper_y_hor = 2*a*j/N-a

    ## Returnerer sand hvis l skærer vilkårlige sider af C_ij. Ellers, returnerer falsk:
    return (lower_y_vert < lower_x_vert <= upper_y_vert or 
            lower_y_vert < upper_x_vert <= upper_y_vert or
            lower_y_hor < lower_x_hor <= upper_y_hor or
            lower_y_hor < upper_x_hor <= upper_y_hor)
            
rho = -.8
p = 0.35
arr = np.array([[intersect_cell(6-i, j, 5, 5, rho, p*pi) for j in range(1, 6)] for i in range(1, 6)])
print(arr)