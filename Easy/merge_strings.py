import itertools

inp1 = 'acegi'
inp2 = 'bdfh'
out1 = ''.join(''.join(f for f in tup if f is not None) for tup in itertools.zip_longest(inp1, inp2))
print(out1)
