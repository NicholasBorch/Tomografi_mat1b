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
            
# rho = -.8
# p = 0.35
# arr = np.array([[intersect_cell(6-i, j, 5, 5, rho, p*pi) for j in range(1, 6)] for i in range(1, 6)])
# print(arr)

def get_length(i,j,a,N,rho,phi):
    ## Hvis l ikke skærer C_ij, returner None
    if not intersect_cell(i,j,a,N,rho,phi):
        return None
    ## Ellers fortsætter vi:

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

    ## Laver liste til skæringspunkter
    skæring = []

    ## Undersøg, om y-værdien i venstre x-intervalendepunkt er indenfor C_ij:
    if lower_y_vert < lower_x_vert <= upper_y_vert:
        ## Hvis ja, tilføj skæringspunktet (2a(i-1)/N-a, lower_x_vert) til listen
        skæring.append(((2*a*(j-1)/N-a),lower_x_vert))

    ## Undersøg, om y-værdien i højre x-intervalendepunkt er indenfor C_ij:
    if lower_y_vert < upper_x_vert <= upper_y_vert:
        ## Hvis ja, tilføj skæringspunktet (2ai/N-a, upper_x_vert) til listen
        skæring.append(((2*a*j/N-a),upper_x_vert))

    ## Undersøg, om x-værdien i nederste y-intervalendepunkt er indenfor C_ij:
    if lower_y_hor < lower_x_hor <= upper_y_hor:
        ## Hvis ja, tilføj skæringspunktet (lower_x_hor, 2a(i-1)/N-a) til listen
        skæring.append((lower_x_hor, 2*a*(i-1)/N-a))
    
    ## Undersøg, om x-værdien i øverste y-intervalendepunkt er indenfor C_ij:
    if lower_y_hor < upper_x_hor <= upper_y_hor:
        ## Hvis ja, tilføj skæringspunktet (upper_x_hor, 2ai/N-a) til listen
        skæring.append((upper_x_hor, 2*a*i/N-a))
    
    ## Returner længden mellem skæringspunkterne (vi er sikret, at der kun findes 2)
    p1, p2 = skæring
    return np.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2) ## Returnerer euklidisk distance mellem skæringspunkter


rho = 1
p = 0.35
arr = np.array([[get_length(6-i, j, 5, 5, rho, p*pi) for j in range(1, 6)] for i in range(1, 6)])
print(arr)
    
def create_matrix(a:float, N:int, rho:np.ndarray, phi:np.ndarray):
    ## Check, at rho og phi har samme længde
    assert rho.shape == phi.shape, 'rho og phi skal have samme længde'
    ## Definér M
    M = len(rho)

    ## Definér matrix A, så elementer kan indsættes
    A = np.zeros((M,N**2))

    ## Lav en række i A for hver rho-phi par
    for k, (r, p) in enumerate(zip(rho,phi)):
        ## 'col' holder styr på, hvilken kolonne, vi arbejder med
        col = 0
        for i in range(1,N+1):
            ## Gennemgå hver j-værdi for hver i-værdi
            for j in range(1,N+1):
                ## Få længden af nuværende skæring, og indsæt i A
                A[k,col] = get_length(i,j,a,N,r,p)
                ## Gå til næste kolonne
                col += 1
    ## Når vi er færdige, returnerer vi A
    return A

A = create_matrix(5,5,np.array([1,1.5,1.75]),np.array([0.1,0.2,0.3]))
print('\n\n',A)