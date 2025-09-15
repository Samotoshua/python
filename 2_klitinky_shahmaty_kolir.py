#Варіант 1

ax,ay,bx,by = map(int,input(" ").split())
if(0<ax<=8 and 0<bx<=8 and 0<ay<=8 and 0<by<=8):
    if(ax==bx and ay==by):
        print("Однаковий колір")
    elif((ax%2==0 and ay%2!=0) and (bx%2==0 and by%2!=0)):
        print("Однаковий колір")
    elif((ax%2!=0 and ay%2==0) and (bx%2!=0 and by%2==0)):
        print("Однаковий колір")
    elif((ax%2!=0 and ay%2!=0) and (bx%2!=0 and by%2!=0)):
        print("Однаковий колір")
    elif((ax%2==0 and ay%2==0) and (bx%2==0 and by%2==0)):
        print("Однаковий колір")
    elif((ax%2==0 and ay%2==0) and (bx%2!=0 and by%2!=0)):
        print("Однаковий колір")
    elif((ax%2!=0 and ay%2!=0) and (bx%2==0 and by%2==0)):
        print("Однаковий колір")
    else: print("Різний колір")
else:
    print("Точка за межами шахматної доски")

#Варіант 2
ax,ay,bx,by = map(int,input(" ").split())

if(0<ax<=8 and 0<bx<=8 and 0<ay<=8 and 0<by<=8):
    if (ax + ay) % 2 == (bx + by) % 2:
        print("Однаковий колір")
    else:
        print("Різний колір")
else:
    print("Точка за межами шахматної дошки")
