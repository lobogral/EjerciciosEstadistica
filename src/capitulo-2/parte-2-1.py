escribir("2.5")
S = {'1HH', '1HT', '1TH', '1TT', '2H', '2T', 
     '3HH', '3HT', '3TH', '3TT', '4H', '4T', 
     '5HH', '5HT', '5TH', '5TT', '6H', '6T'}
escribir("S =", S)

escribir("")
escribir("2.9")
S = {'1HH', '1HT', '1TH', '1TT', '2H', '2T', 
     '3HH', '3HT', '3TH', '3TT', '4H', '4T', 
     '5HH', '5HT', '5TH', '5TT', '6H', '6T'}
escribir("S =", S)
A = {'1HH', '1HT', '1TH', '1TT', '2H', '2T'}
escribir("a) A =", A)
B = {'1TT', '3TT', '5TT'}
escribir("b) B =", B)
escribir("c) A' =", S - A)
escribir("d) A' ∩ B =", (S - A) & B)
escribir("e) A ∪ B =", A | B)

escribir("")
escribir("2.11")
S = {'M1M2', 'M1F1', 'M1F2', 
     'M2M1', 'M2F1', 'M2F2', 
     'F1M1', 'F1M2', 'F1F2', 
     'F2M1', 'F2M2', 'F2F1'}
escribir("a) S =", S)
A = {'M1M2', 'M1F1', 'M1F2', 
     'M2M1', 'M2F1', 'M2F2'}
escribir("b) A =", A)
B = {'M1F1', 'M1F2', 'M2F1', 'M2F2',
     'F1M1', 'F1M2', 'F2M1', 'F2M2'}
escribir("c) B =", B)
C = {'F1F2', 'F2F1'}
escribir("d) C =", C)
escribir("e) A ∩ B =", A & B)
escribir("f) A ∪ C =", A | C)

escribir("")
escribir("2.15")
S = {'cobre', 'sodio',
'nitrógeno', 'potasio', 'uranio', 'oxígeno', 'cinc'}
escribir("S =", S)
A = {'cobre', 'sodio', 'cinc'}
escribir("A =", A)
B = {'sodio', 'nitrógeno', 'potasio'}
escribir("B =", B)
C = {'oxígeno'}
escribir("C =", C)
escribir("a) A' =", S - A)
escribir("b) A ∪ C =", A | C)
escribir("c) (A ∩ B') ∪ C' =", (A & (S - B)) | (S - C))
escribir("d) B' ∩ C' =", (S - B) & (S - C))
escribir("e) A ∩ B ∩ C =", A & B & C)
escribir("f) (A'∪ B') ∩ (A'∩ C) =", ((S - A) | (S - B)) & ((S - A) & C))