from gradinita.gradinita_publica import Gradinita_Publica
from gradinita.gradinita_privata import Gradinita_Privata
from gradinita.gradinita_publica_25 import Gradinita_Publica_25


gradinita_publica_1 = Gradinita_Publica()
# gradinita_publica_1.activitate_practica()
# gradinita_publica_1.ora_de_somn()
gradinita_publica_1.adauga_elev("Georgel", 4, 2020)
gradinita_publica_1.adauga_elev("Damian", 4, 2019)
gradinita_publica_1.adauga_elev("Andrei", 3, 2020)

print("---" * 25)

gradinita_privata_1 = Gradinita_Privata()
# gradinita_privata_1.activitate_practica()
gradinita_privata_1.adauga_elev("Daniela", 3, 2021, True)
gradinita_privata_1.adauga_elev("Carmen", 4, 2021, True)
gradinita_privata_1.adauga_elev("Raluca", 3, 2020, False)
# gradinita_privata_1.valoare_taxa = 4000
# gradinita_privata_1.valoare_taxa = 5000
# gradinita_privata_1.valoare_taxa = 6000
# print(gradinita_privata_1.valoare_taxa)

# print("---" * 25)

# gradinita_publica_25_1 = Gradinita_Publica_25()
# gradinita_publica_25_1.ora_de_somn()
# gradinita_publica_25_1.activitate_practica()


gradinita_publica_1.afisare_elevi()

print("---" * 25)

gradinita_privata_1.afisare_elevi()
