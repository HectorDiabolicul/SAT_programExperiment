import time


def resolve(clause1, clause2):
    resolvents = []
    for lit in clause1:
        if -lit in clause2:
            new_clause = list(set(clause1 + clause2))
            new_clause.remove(lit)
            new_clause.remove(-lit)
            resolvents.append(new_clause)
    return resolvents


def resolution(clauses):
    new = set()
    while True:
        n = len(clauses)
        for i in range(n):
            for j in range(i + 1, n):
                resolvents = resolve(clauses[i], clauses[j])
                for r in resolvents:
                    if r == []:
                        return True
                    new.add(tuple(sorted(r)))
        if new.issubset(set(map(tuple, clauses))):
            return False
        for clause in new:
            if list(clause) not in clauses:
                clauses.append(list(clause))


def eliminate_variable(clauses, var):
    pos_clauses = [c for c in clauses if var in c]
    neg_clauses = [c for c in clauses if -var in c]
    new_clauses = []

    for p in pos_clauses:
        for n in neg_clauses:
            resolvent = list(set(p + n))
            if var in resolvent: resolvent.remove(var)
            if -var in resolvent: resolvent.remove(-var)
            if not any((x in resolvent and -x in resolvent) for x in resolvent):
                new_clauses.append(resolvent)

    rest = [c for c in clauses if var not in c and -var not in c]
    return rest + new_clauses


def dp_algorithm(clauses, variables):
    while variables:
        var = variables.pop()
        clauses = eliminate_variable(clauses, var)
        if [] in clauses:
            return False
    return True


def simplify(clauses, assignment):
    simplified = []
    for clause in clauses:
        if any(lit in assignment for lit in clause):
            continue
        new_clause = [lit for lit in clause if -lit not in assignment]
        simplified.append(new_clause)
    return simplified


def dpll(clauses, assignment=[]):
    clauses = simplify(clauses, assignment)
    if [] in clauses:
        return False
    if not clauses:
        return assignment
    literals = {abs(lit) for clause in clauses for lit in clause}
    assigned = {abs(lit) for lit in assignment}
    unassigned = list(literals - assigned)
    if not unassigned:
        return assignment
    var = unassigned[0]
    for val in [var, -var]:
        result = dpll(clauses, assignment + [val])
        if result:
            return result
    return False




def read_formula():
    clauses = []
    num_vars = int(input("Număr de variabile (literali): "))
    num_clauses = int(input("Număr de clauze: "))

    print("\nIntroduceți clauzele în formatul: literal1 literal2 ... (0 pentru a termina clauza)\nExemplu: 1 -2 0")
    for i in range(num_clauses):
        while True:
            try:
                raw = input(f"Clauza #{i + 1}: ").strip().split()
                clause = [int(x) for x in raw if x != "0"]
                if clause:
                    clauses.append(clause)
                    break
            except ValueError:
                print("Input invalid. Introduceți doar numere întregi, terminați cu 0.")

    variables = list(range(1, num_vars + 1))
    return clauses, variables


def main():
    print("=== SAT Solver Interactiv ===\n")
    clauses, variables = read_formula()

    print("\nAlege metoda de rezolvare:")
    print("1. Rezoluție")
    print("2. Davis–Putnam (DP)")
    print("3. DPLL")
    choice = input("Opțiune (1/2/3): ")

    if choice == "1":
        start = time.time()
        result = resolution(clauses.copy())
        end = time.time()
        print("\n[Rezoluție] Rezultat:", "Satisfiabilă" if result else "Nesatisfiabilă")
        print(f"Timp de execuție: {(end - start) * 1000:.3f} ms")

    elif choice == "2":
        start = time.time()
        result = dp_algorithm(clauses.copy(), variables.copy())
        end = time.time()
        print("\n[DP] Rezultat:", "Satisfiabilă" if result else "Nesatisfiabilă")
        print(f"Timp de execuție: {(end - start) * 1000:.3f} ms")

    elif choice == "3":
        start = time.time()
        result = dpll(clauses.copy())
        end = time.time()
        if result:
            print("\n[DPLL] Rezultat: Satisfiabilă")
            print("Atribuire satisfăcătoare:", result)
        else:
            print("\n[DPLL] Rezultat: Nesatisfiabilă")
        print(f"Timp de execuție: {(end - start) * 1000:.3f} ms")

    else:
        print("Opțiune invalidă.")


if __name__ == "__main__":
    main()
