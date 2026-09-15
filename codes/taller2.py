D = [False, True]

def verificar_leyes():
    ley_conmutativa1 = all(((x or y) or z) == ((x or (y or z))) for x in D for y in D for z in D)
    ley_conmutativa2 = all((x and y) == (y and x) for x in D for y in D)
    ley_asociativa1 = all(((x or y) or z) == ((x or (y or z))) for x in D for y in D for z in D)
    ley_asociativa2 = all(((x and y) and z) == ((x and (y and z))) for x in D for y in D for z in D)
    ley_distributiva2 = all((x and (y or z)) == ((x and y) or (x and z)) for x in D for y in D for z in D)
    ley_distributiva1 = all((x or (y and z)) == ((x or y) and (x or z)) for x in D for y in D for z in D)
    ley_morgan2 = all(not (x and y) == (not x or not y) for x in D for y in D)
    ley_morgan1 = all(not (x or y) == (not x and not y) for x in D for y in D)

    print("Ley Conmutativa (OR):", ley_conmutativa1)
    print("Ley Conmutativa (AND):", ley_conmutativa2)
    print("Ley Asociativa (OR):", ley_asociativa1)
    print("Ley Asociativa (AND):", ley_asociativa2)
    print("Ley Distributiva (AND):", ley_distributiva2)
    print("Ley Distributiva (OR):", ley_distributiva1)
    print("Ley de Morgan (AND):", ley_morgan2)
    print("Ley de Morgan (OR):", ley_morgan1)

if __name__ == "__main__":
    verificar_leyes()
