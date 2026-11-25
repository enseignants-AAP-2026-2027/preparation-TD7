#! /usr/bin/env python3

"""  """
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

def final():
    # Création de la figure
    plt.figure(figsize=(3, 3))

    # Configuration de l'affichage (repère informatique standard)
    plt.xlim(0, 3)
    plt.ylim(3, 0) 
    plt.axis("equal")
    plt.xticks([1])
    plt.yticks([1])

    start = (0, 2)
    end = (2, 2)
    chemin = [(0, 2), (1, 2), (1, 1), (0, 1), (0, 0), (1, 0), (2, 0), (2,1), (2,2)]
    walls= [ [[0,1],[2,2]], [[1,2],[1,1]], [[2,2],[1,2]], [[2,2],[2,3]] ]

    # Départ et arrivée
    plt.scatter(start[0]+0.5,start[1]+0.5,color="green", s=100, zorder=3)
    plt.scatter(end[0]+0.5,end[1]+0.5,color="blue", s=100, zorder=3)
    
    plt.plot([0, 0], [0, 3], color="black", linewidth=4)    # Mur gauche
    plt.plot([3, 3], [0, 3], color="black", linewidth=4)    # Mur droit
    plt.plot([0, 3], [0, 0], color="black", linewidth=4)    # Mur inférieur
    plt.plot([0, 3], [3, 3], color="black", linewidth=4)    # Mur supérieur

    for m in walls: 
        plt.plot(m[0],m[1], color="black", linewidth=4)    # Mur

    if chemin:
        xs = [c + 0.5 for c, r in chemin]
        ys = [r + 0.5 for c, r in chemin]
        plt.plot(xs, ys, color="red", linewidth=3)

def write_plot(filename,  titre): 
    # produit une courbe à partir des données du graphique en mémoire, 
    # stockée dans le fichier indiqué par l'argument filename

    plt.title(titre)
    fichier = Path(__file__).with_name(filename)
    plt.savefig(fichier, dpi=200, bbox_inches="tight")
    print(f"Graphique enregistré dans : {fichier}")
    plt.close()

if __name__ == "__main__":

    final()
    write_plot("test.png", "titre")

