a = input()
b = input()
c = input()

meerkat =[a, b, c]

meerkat[0], meerkat[2] = meerkat[2], meerkat[0]
print(meerkat)