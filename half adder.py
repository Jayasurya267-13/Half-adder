def half_adder(a, b):
    sum_bit = a ^ b
    carry_bit = a & b
    return sum_bit, carry_bit

def full_adder(a, b, carry_in):
    sum_bit = a ^ b ^ carry_in
    carry_out = (a & b) | (b & carry_in) | (a & carry_in)
    return sum_bit, carry_out

print("HALF ADDER TRUTH TABLE")
print("----------------------")
for a in [0, 1]:
    for b in [0, 1]:
        s, c = half_adder(a, b)
        print(f"a={a}, b={b} -> Sum={s}, Carry={c}")

print("\nFULL ADDER TRUTH TABLE")
print("----------------------")
for a in [0, 1]:
    for b in [0, 1]:
        for carry_in in [0, 1]:
            s, c = full_adder(a, b, carry_in)
            print(f"a={a}, b={b}, carry_in={carry_in} -> Sum={s}, Carry_out={c}")
