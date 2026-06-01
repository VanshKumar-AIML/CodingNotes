'''
print('full side triangles')
for i in range(2):
    for i in range(1,8):
        print(' * '*i)
    for  i in range(8,0,-1):
        print(' * '*i)

print('half side triangles:')
for i in range(8,1,-1):
    print(' * '*i)
for i in range(0,8):
    print(' * '*i)

print('pyramid:')
for i in range(1,6):
    print(' * '.center*i)
'''