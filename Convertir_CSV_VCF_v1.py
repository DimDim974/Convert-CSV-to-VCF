"""
Auteur : SAUTRON Dimitri
Description : Convertisseur CSV en VCF.
Date : 20/09/2019
Version : 1.2

"""

import os
import csv
import sys 

#os.chdir(os.environ["HOME"])
#==> Fonctionnel manuellement

FileIn = sys.argv[1]
FileOut = sys.argv[2]

# cette boucle parcourt toutes les lignes du fichier csv
with open(FileIn , newline='') as d:
	reader = csv.reader(d)
	for ligne in reader:
		Data = str(ligne[0]).split(';')
		sortie = open(FileOut , 'a')
		sortie.write("BEGIN:VCARD\n")
		sortie.write("VERSION:2.1\n")
		sortie.write("N:"+Data[0]+"\n")#";"+Data[1]+"\n")
		sortie.write("TEL;HOME:"+Data[1]+"\n")
		#sortie.write("TEL;CELL:"+Data[3]+"\n")
		#sortie.write("TEL;WORK:"+Data[4]+"\n")
		sortie.write("END:VCARD\n")
		sortie.write("\n")
	sortie.close()
