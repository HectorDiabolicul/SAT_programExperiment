Acest program permite testarea interactivă a 3 metode clasice de rezolvare a problemei SAT:

- 1 Rezoluție
- 2 Davis–Putnam (DP)
- 3 DPLL (Davis–Putnam–Logemann–Loveland)

Este scris în Python și rulează în linia de comandă, fără biblioteci externe.


## Cum funcționează

1. Introduci numărul de variabile și clauze.
2. Scrii fiecare clauză folosind literali (ex: `1 -2 0`).
3. Alegi algoritmul (1, 2 sau 3).
4. Programul îți spune dacă formula este satisfiabilă și, pentru DPLL, dă o atribuire validă.


## Exemplu de rulare

=== SAT Solver Interactiv ===

Număr de variabile (literali): 2
Număr de clauze: 2

Clauza #1: 1 -2 0
Clauza #2: -1 2 0

Alege metoda de rezolvare:
1. Rezoluție
2. Davis–Putnam (DP)
3. DPLL
Opțiune (1/2/3): 3

[DPLL] Rezultat: Satisfiabilă
Atribuire satisfăcătoare: [1, 2]
Timp de execuție: 0.035 ms
