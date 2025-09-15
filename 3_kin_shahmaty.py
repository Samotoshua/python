k,l = 4, 4 
n,m = map(int,input(" ").split())

top_right = m-l==2 and n-k==1
top_left = m-l==2 and k-n==1
bottom_right = l-m==2 and n-k==1
bottom_left = l-m==2 and k-n==1

right_top = n-k==2 and m-l==1
left_top = k-n==2 and m-l==1
right_bottom = n-k==2 and l-m==1
left_bottom = k-n==2 and l-m==1

# if(top_right):
#     print("Вверх вправо")
# elif(top_left):
#     print("Вверх вліво")
# elif(bottom_right):
#     print("Вниз вправо")
# elif(bottom_left):
#     print("Вниз вліво")
# else:print("no")
if(top_right or top_left or bottom_right or bottom_left
or right_top or left_top or right_bottom or left_bottom):
    print("Кінь може потрапити в дану клітинку")
else:print("Кінь НЕ може потрапити в дану клітинку")