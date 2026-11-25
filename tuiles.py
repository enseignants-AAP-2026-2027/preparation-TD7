#! /usr/bin/env python3

"""  """
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from PIL import Image


def write_plot(filename,  titre): 
    # produit une courbe à partir des données du graphique en mémoire, 
    # stockée dans le fichier indiqué par l'argument filename

    plt.title(titre)
    fichier = Path(__file__).with_name(filename)
    plt.savefig(fichier, dpi=200, bbox_inches="tight")
    print(f"Graphique enregistré dans : {fichier}")
    plt.close()

if __name__ == "__main__":

    # Charger la banque de tuiles
    # 2D_Maze_Tiles_Red.png:   PNG image data, 320 x 64, 8-bit/color RGBA, non-interlaced
    # 2D_Maze_Tiles_White.png: PNG image data, 320 x 64, 8-bit colormap, non-interlaced
    tileset = Image.open("tiles/2D_Maze_Tiles_White.png")
    tuile4 = tileset.crop((0, 0, 64, 64))
    tuile2BG = tileset.crop((64, 0, 128, 64))
    tuile1B = tileset.crop((128, 0, 192, 64))
    tuile3BGH = tileset.crop((192, 0, 256, 64))
    tuile2HB = tileset.crop((256, 0, 320, 64))

    # # 2D_Path_Tiles.png:       PNG image data, 640 x 128, 8-bit gray+alpha, non-interlaced
    # tileset = Image.open("tiles/2D_Path_Tiles.png")
    # tuile4 = tileset.crop((0, 0, 128, 128))
    # tuile2BG = tileset.crop((128, 0, 256, 128))
    # tuile1B = tileset.crop((256, 0, 384, 128))
    # tuile3BGH = tileset.crop((384, 0, 512, 128))
    # tuile2HB = tileset.crop((512, 0, 640, 128))

    tuile4.save("tuileHDBG.png")
    tuile1B.save("tuileB.png")
    tuile2BG.save("tuileBG.png")
    tuile2HB.save("tuileHB.png")
    tuile3BGH.save("tuileHBG.png")
    
    images1 = [
        tuile1B,             # B
        tuile1B.rotate(90),  # D
        tuile1B.rotate(180), # H
        tuile1B.rotate(270)  # G
    ]

    images3BGH = [
        tuile3BGH,             # BGH
        tuile3BGH.rotate(90),  # GHD
        tuile3BGH.rotate(180), # HDB
        tuile3BGH.rotate(270)  # DBG
    ]

    images2BG = [
        tuile2BG,             # BG
        tuile2BG.rotate(90),  # DB
        tuile2BG.rotate(180), # HD
        tuile2BG.rotate(270)  # GH
    ]

    images2HB = [
        tuile2HB,             # HB
        tuile2HB.rotate(90),  # GD
    ]

    # Création de la figure
    plt.figure(figsize=(3, 3))
    plt.xticks([1])
    plt.yticks([1])
    

    plt.imshow(images1[1], extent=[0, 1, 0, 1]) # extent = [xmin, xmax, ymin, ymax] 
    plt.imshow(images2BG[2], extent=[0, 1, 1, 2])
    plt.imshow(images2BG[1], extent=[0, 1, 2, 3])

    plt.imshow(images2BG[3], extent=[1, 2, 0, 1])
    plt.imshow(images2BG[0], extent=[1, 2, 1, 2])
    plt.imshow(images2HB[1], extent=[1, 2, 2, 3])

    plt.imshow(images1[2], extent=[2, 3, 0, 1])
    plt.imshow(images2HB[0], extent=[2, 3, 1, 2])
    plt.imshow(images2BG[0], extent=[2, 3, 2, 3])
    


    # Configuration de l'affichage (repère informatique standard)
    plt.axis("equal") 
    write_plot("test.png", "titre")


    # plt.imshow(tuile)
    # plt.axis("off")
    # plt.show()



