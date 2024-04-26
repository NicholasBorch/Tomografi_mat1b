from sympy import *
def intersect_cell(i, j, a, N, rho, phi):
    return ((2*a*(i-1)/N-a < (rho-(2*a*(j-1)/N-a)*cos(phi))/sin(phi) <= 2*a*i/N-a) or (2*a*(i-1)/N-a < ((rho-(2*a*j/N-a)*cos(phi))/sin(phi)) <= 2*a*i/N-a))

def intersect_cell_readable(i, j, a ,N, rho, phi):
    lower_x = (rho-(2*a*(j-1)/N-a)*cos(phi))/sin(phi) 
    upper_x = (rho-(2*a*j/N-a)*cos(phi))/sin(phi)

    lower_y = 2*a*(i-1)/N-a
    upper_y = 2*a*i/N-a
    return lower_y < lower_x <= upper_y or lower_y < upper_x <= upper_y


print(intersect_cell_readable(1,1, 5, 5, 2, 0.25*pi))