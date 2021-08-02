escribir("2.5")
S = {'1HH', '1HT', '1TH', '1TT', '2H', '2T', 
     '3HH', '3HT', '3TH', '3TT', '4H', '4T', 
     '5HH', '5HT', '5TH', '5TT', '6H', '6T'}
escribir('S = ' + str(S))

escribir("2.9")
S = {'1HH', '1HT', '1TH', '1TT', '2H', '2T', 
     '3HH', '3HT', '3TH', '3TT', '4H', '4T', 
     '5HH', '5HT', '5TH', '5TT', '6H', '6T'}
escribir('S = ' + str(S))
A = {'1HH', '1HT', '1TH', '1TT', '2H', '2T'}
escribir('a) A = ' + str(A))
B = {'1TT', '3TT', '5TT'}
escribir('b) B = ' + str(B))
escribir('c) A\' = ' + str(S - A))
escribir('d) A\' ∩ B = ' + str( (S - A) & B))
escribir('e) A ∪ B = ' + str(A | B))

escribir("2.11")
S = {'M1M2', 'M1F1', 'M1F2', 
     'M2M1', 'M2F1', 'M2F2', 
     'F1M1', 'F1M2', 'F1F2', 
     'F2M1', 'F2M2', 'F2F1'}
escribir('a) S = ' + str(S))
A = {'M1M2', 'M1F1', 'M1F2', 
     'M2M1', 'M2F1', 'M2F2'}
escribir('b) A = ' + str(A))
B = {'M1F1', 'M1F2', 'M2F1', 'M2F2',
     'F1M1', 'F1M2', 'F2M1', 'F2M2'}
escribir('c) B = ' + str(B))
C = {'F1F2', 'F2F1'}
escribir('d) C = ' + str(C))
escribir('e) A ∩ B = ' + str(A & B))
escribir('f) A ∪ C = ' + str(A | C))

escribir("2.15")
S = {'cobre', 'sodio',
'nitrógeno', 'potasio', 'uranio', 'oxígeno', 'cinc'}
escribir('S = ' + str(S))
A = {'cobre', 'sodio', 'cinc'}
escribir('A = ' + str(A))
B = {'sodio', 'nitrógeno', 'potasio'}
escribir('B = ' + str(B))
C = {'oxígeno'}
escribir('C = ' + str(C))
escribir('a) A\' = ' + str(S - A))
escribir('b) A ∪ C = ' + str(A | C))
escribir('c) (A ∩ B\') ∪ C\' = ' + str((A & (S - B)) | (S - C)))
escribir('d) B\' ∩ C\' = ' + str((S - B) & (S - C)))
escribir('e) A ∩ B ∩ C = ' + str(A & B & C))
escribir('f) (A\'∪ B\') ∩ (A\'∩ C) = ' + str(((S - A) | (S - B)) & ((S - A) & C)))