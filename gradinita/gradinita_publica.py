from gradinita.gradinitaABC import GradinitaABC


class Gradinita_Publica(GradinitaABC):
    def __init__(self):
        self.elevi = {}
    def activitate_practica(self):
        print("Copiii invata sa deseneze")

    def ora_de_somn(self):
        print("Copiii trebuie sa doarma la ora 5")

    def adauga_elev(self, nume_elev, varsta_elev, an_inscriere):
        #(<nume_elev>:{"varsta": <varsta_elev>, "an_inscriere":<an_inscriere>)
        self.elevi[nume_elev] = {
            # "nume_elev": nume_elev,
            "varsta": varsta_elev,
            "an_inscriere": an_inscriere
        }

    def afisare_elevi(self):
        # # implementare 1
        # print(f"Elevii inscrisi la gradinita publica sunt: {self.elevi}")


        # # implementare 2 - INCOMPLETA, nevoie acces la nume elev (key from self.elevi dictionary)
        # print(f"Elevii inscrisi la gradinita publica sunt:")
        # for elev in self.elevi.values():
        #     print(f"Elevul {elev} are {elev["varsta"]} ani si a fost inscris in anul {elev["an_inscriere"]}.")


        # implementare 3
        print(f"Elevii inscrisi la gradinita publica sunt: \n")

        lista_nume_elevi = list(self.elevi.keys())
        # print(lista_nume_elevi)

        lista_valori_dict_elevi = list(self.elevi.values())
        # print(lista_valori_dict_elevi)

        for i in range(len(lista_nume_elevi)):
            var_nume_elev = lista_nume_elevi[i]
            lista_date_elev = lista_valori_dict_elevi[i]
            print(f"Elevul {var_nume_elev} care are {lista_date_elev['varsta']} ani si a fost inscris in anul {lista_date_elev['an_inscriere']}.")



# TEMA: implementare metoda afisare_elevi + de apelat in fisierul main.py - DONE
