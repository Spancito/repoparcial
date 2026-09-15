import math

n1 = float(input("Escribe el primer número: "))
n2 = float(input("Escribe el segundo número: "))

s1 = "+" if n1 >= 0 else "-"
e1 = math.floor(math.log10(abs(n1))) + 1 if n1 != 0 else 0
m1 = abs(n1) / (10**e1)
e1_str = f"{'+' if e1 >= 0 else '-'}{abs(e1):03d}"
m1_str = f"{m1:.11f}".replace(".", "")[1:12].ljust(11, "0")

s2 = "+" if n2 >= 0 else "-"
e2 = math.floor(math.log10(abs(n2))) + 1 if n2 != 0 else 0
m2 = abs(n2) / (10**e2)
e2_str = f"{'+' if e2 >= 0 else '-'}{abs(e2):03d}"
m2_str = f"{m2:.11f}".replace(".", "")[1:12].ljust(11, "0")

print(f"\nNúmero 1: [{s1}] [{e1_str}] [{m1_str}]")
print(f"Número 2: [{s2}] [{e2_str}] [{m2_str}]")

s_mult = "+" if s1 == s2 else "-"
e_mult = e1 + e2
m_mult = float("0." + m1_str) * float("0." + m2_str)
e_mult_str = f"{'+' if e_mult >= 0 else '-'}{abs(e_mult):03d}"
m_mult_str = f"{m_mult:.11f}".replace(".", "")[1:12].ljust(11, "0")

print(f"Multiplicación: [{s_mult}] [{e_mult_str}] [{m_mult_str}]")

s_div = "+" if s1 == s2 else "-"
e_div = e1 - e2
m_div = float("0." + m1_str) / float("0." + m2_str)
e_div_str = f"{'+' if e_div >= 0 else '-'}{abs(e_div):03d}"
m_div_str = f"{m_div:.11f}".replace(".", "")[1:12].ljust(11, "0")

print(f"División: [{s_div}] [{e_div_str}] [{m_div_str}]")