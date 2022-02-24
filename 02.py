k = ['coco', 'caca', 'cece']
for c in k:
    if c != 'coco':
        print(f'{c} blast.')
    else:
        print(f'{c} rica.')
        
        
        
x = range(1,101)
k = ['aba','uku','ele']
for ce in k:
    if 'uku' == ce:
        print(f"j {ce}")
    elif 'aba' == ce:
        print(f"euy {ce}")
    else:
        for z in x:
            if z % 3 and z % 5 and z > 5:
                print(f'{z} tidak habis dibagi tiga atau lima.')
            else:
                print("test", z)
                
    
    
    
cloud = [45, 55, 33]
forest = [2, 4, 5]
k = [x + z for x in cloud for z in forest]
print(k)

test = [(x,y) for x in (1, 2, 3) for y in(4, 5, 6)]
print(test)

cloud = [45, 55, 33]
forest = [(d,v) for d in (1, 2, 3) for v in(4, 5, 6)]
k = [x + d - v for x in cloud for d, v in forest]
print(k)
