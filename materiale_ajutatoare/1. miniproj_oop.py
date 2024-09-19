"""
Miniproiect Piloni OOP - Sesiunea 11
"""


"""
1. Creaza o clasa abstracta numita Gradinita,
cu urmatoarele metode abstracte:
- activitate_practica()
- ora_de_somn()
"""


"""
2. Implementati doua clase, numite GradinitaPublica si
GradinitaPrivata care sa implementeze clasa abstracta Gradinita.

GradinitaPublica:
- activitate_practica() - printeaza "copiii invata sa deseneze"
- ora_de_somn() - printeaza "copiii trebuie sa doarma la ora 5"

GradinitaPrivata:
- activitate_practica() - printeaza "copiii invata sa modeleze cu plastilina"
"""


"""
3.
a. Rulati codul. Se intampla ceva?
b. Instantiati un obiect din clasa GradinitaPublica si rulati codul.
Se printeaza ceva pe ecran? De ce?
c. Apelati metoda activitate_practica() si rulati codul. Ce observati?
d. Instantiati un obiect din clasa GradinitaPrivata si rulati codul.
De ce va da eroare? Cum putem rezolva eroarea?
"""


"""
4. Creati o clasa, GradinitaPublica25, care sa mosteneasca clasa GradinitaPublica.
Implementati metoda activitate_practica() in felul urmator:
- printati mesajul "Copiii se joaca in curte pe balansoar.

- Instantiati un obiect din clasa GradinitaPublica25.
- Prin intermediul obiectului instantiat, apelati toate metodele disponibile
si observati rezultatele.
"""


"""
5. Adauga un atribut pe obiect, numit elevi,
in clasele GradinitaPublica si GradinitaPrivata.
Initial, acesta va fi un dictionar gol.

Implementeaza o metoda in fiecare in aceste clase,
numita adauga_elev:

 In clasa GradinitaPublica, primeste urmatorii parametri:
- nume_elev, varsta_elev, an_inscriere
- salveaza aceste informatii in atributul elevi, sub forma
{<nume_elev>:{"varsta": <varsta_elev>, "an_inscriere":<an_inscriere>}

 In clasa GradinitaPrivata, primeste urmatorii parametri:
- nume_elev, varsta_elev, an_inscriere, taxa_platita
- salveaza aceste informatii in atributul elevi, sub forma
{<nume_elev>:{"varsta": <varsta_elev>, "an_inscriere":<an_inscriere>, "taxa_platita": <taxa_platita"}

- apeleaza aceasta metoda pe un obiect din fiecare clasa pentru a ilustra
polimorfismul
"""


"""
6. 
Adauga un atribut privat in clasa GradinitaPrivata,
numit valoare_taxa.
Creeaza o proprietate care sa incapsuleze atributul privat valoare_taxa:
- sa aiba un getter:
    - sa returneze taxa ca string cu moneda atasata ("5000 lei")
- sa aiba un setter:
    - care verifica noua taxa ce se doreste a fi platita:
    - daca e mai mica decat 5000, nu se seteaza noua taxa, si se afiseaza mesajul 
"Taxa e de 5000 lei. Trebuie achitata toata suma o data."
    - daca e mai mare de 5000, setam taxa ca fiind 5000 si afisam un mesaj
in care spunem utilizatorului ca taxa e de 5000 lei, a fost platita cu succes si
restul de bani ce ii dam inapoi.
    - daca e exact 5000, atunci setam taxa.
"""
