from gradinita.gradinitaABC import GradinitaABC


class Gradinita_Privata(GradinitaABC):
    def __init__(self):
        self.elevi = {}
        self.__valoare_taxa = None
    def activitate_practica(self):
        print("Copiii invata sa modeleze cu plastilina")

    def ora_de_somn(self):
        print("Ora de somn este 15:00")

    def adauga_elev(self, nume_elev, varsta_elev, an_inscriere, taxa_platita):
        # (<nume_elev>:{"varsta": <varsta_elev>, "an_inscriere": <an_inscriere>, "taxa_platita": <taxa_platita>)
        self.elevi[nume_elev] = {
            # "nume_elev": nume_elev,
            "varsta": varsta_elev,
            "an_inscriere": an_inscriere,
            "taxa_platita": taxa_platita
        }

# TEMA: implementare metoda afisare_elevi + de apelat in Main

    @property
    def valoare_taxa(self):
        return self.__valoare_taxa

    @valoare_taxa.getter
    def valoare_taxa(self):
        return f"{self.__valoare_taxa} lei"

    @valoare_taxa.setter
    def valoare_taxa(self, taxa_noua):
        if taxa_noua < 5000:
            print("Taxa e de 5000 lei. Trebuie achitata toata suma o data.")
        elif taxa_noua > 5000:
            self.__valoare_taxa = 5000
            print(f"Taxa este de 5000 lei. A fost platita cu succes. Restul sumei de bani: {taxa_noua - 5000} - lei va fi returnata.")
        else:
            self.__valoare_taxa = 5000
            print("Taxa a fost platita cu succes.")


    def afisare_elevi(self):
        # # implementare 1
        # print(f"Elevii inscrisi la gradinita privata sunt: {self.elevi}")


        # implementare 2
        print(f"Elevele inscrise la gradinita privata sunt: \n")

        lista_nume_elevi = list(self.elevi.keys())
        # print(lista_nume_elevi)

        lista_valori_dict_elevi = list(self.elevi.values())
        # print(lista_valori_dict_elevi)

        for i in range(len(lista_nume_elevi)):
            var_nume_elev = lista_nume_elevi[i]
            lista_date_elev = lista_valori_dict_elevi[i]

            if lista_date_elev["taxa_platita"] == True:
                print(f"Eleva {var_nume_elev} care are {lista_date_elev['varsta']} ani, a fost inscrisa in anul {lista_date_elev['an_inscriere']} si are taxa platita.")
            else:
                print(f"Eleva {var_nume_elev} care are {lista_date_elev['varsta']} ani, a fost inscrisa in anul {lista_date_elev['an_inscriere']} si NU are taxa platita.")
