V = abs(int(input()))
A = abs(int(input()))
F = abs(int(input()))
P = abs(int(input()))

if V > 2000:
    print('ERROO')
    
elif F > 1000 or A > 1000 or P > 1000:
    print(f'O valor das contas não pode ultrapassar 1000')

elif A < 1 or F < 1 or P < 1:
    print(f'O valor das contas não pode ser menor que 1')

if A + F + P <= V:
    print(3)
elif A + F <= V or A + P <= V or P + F <= V:
    print(2)
elif A <= V or F <= V or P <= V:
    print(1)
else:
    print(0)