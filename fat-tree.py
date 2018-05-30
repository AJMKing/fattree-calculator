#!/usr/bin/env python3
import math

def main():
    Pe=48 #number of switch edge ports
    Pc=Pe #number of switch core ports note. this assumes same switches are used!

    Bl=2 #blocking factor
    l=2 # levels
    N=Pe**l/(1+(1/Bl)**(l-1)) #number of nodes in the cluster. 36^2/((1+(1/5)^(2-1))
    E=0
    C=0
    PEn = Pe*Bl/(1+Bl) #ports to nodes
    PEc = Pe - PEn # ports to core level

    print("Max Number of number of nodes")
    print(N)

    print("Ports nodes, ports to core")
    print(PEn,PEc)

    Blr = PEn/PEc #blocking factor
    print("Blocking Factor")
    print(Blr)

    E = math.ceil(N/PEn)
    print("No. Edge Switches")
    print(E)

    B = math.floor(Pc/E)
    print("Links in a bundle")
    print(B)

    C = math.ceil(PEc/B)
    print("Number of core switches")
    print(C)

    L = N + E*PEc
    print("Number of total links")
    print(L)

if __name__ == "__main__":
    main()


