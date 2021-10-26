print("2.5")
S = {'1HH', '1HT', '1TH', '1TT', '2H', '2T',
     '3HH', '3HT', '3TH', '3TT', '4H', '4T',
     '5HH', '5HT', '5TH', '5TT', '6H', '6T'}
print("S =", S)

print("")
print("2.9")
S = {'1HH', '1HT', '1TH', '1TT', '2H', '2T',
     '3HH', '3HT', '3TH', '3TT', '4H', '4T',
     '5HH', '5HT', '5TH', '5TT', '6H', '6T'}
print("S =", S)
A = {'1HH', '1HT', '1TH', '1TT', '2H', '2T'}
print("a) A =", A)
B = {'1TT', '3TT', '5TT'}
print("b) B =", B)
print("c) A' =", S - A)
print("d) A' ∩ B =", (S - A) & B)
print("e) A ∪ B =", A | B)

print("")
print("2.11")
S = {'M1M2', 'M1F1', 'M1F2',
     'M2M1', 'M2F1', 'M2F2',
     'F1M1', 'F1M2', 'F1F2',
     'F2M1', 'F2M2', 'F2F1'}
print("a) S =", S)
A = {'M1M2', 'M1F1', 'M1F2',
     'M2M1', 'M2F1', 'M2F2'}
print("b) A =", A)
B = {'M1F1', 'M1F2', 'M2F1', 'M2F2',
     'F1M1', 'F1M2', 'F2M1', 'F2M2'}
print("c) B =", B)
C = {'F1F2', 'F2F1'}
print("d) C =", C)
print("e) A ∩ B =", A & B)
print("f) A ∪ C =", A | C)

print("")
print("2.15")
S = {'cobre', 'sodio', 'nitrógeno', 'potasio',
     'uranio', 'oxígeno', 'cinc'}
print("S =", S)
A = {'cobre', 'sodio', 'cinc'}
print("A =", A)
B = {'sodio', 'nitrógeno', 'potasio'}
print("B =", B)
C = {'oxígeno'}
print("C =", C)
print("a) A' =", S - A)
print("b) A ∪ C =", A | C)
print("c) (A ∩ B') ∪ C' =", (A & (S - B)) | (S - C))
print("d) B' ∩ C' =", (S - B) & (S - C))
print("e) A ∩ B ∩ C =", A & B & C)
print("f) (A'∪ B') ∩ (A'∩ C) =", ((S - A) | (S - B)) & ((S - A) & C))
