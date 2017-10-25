Дешифровка решетки Кардано



#размер сетки
size = 10 
#сетка
my_list = (
  ("тСПвнперот"),
  ("ьеосФдптор"),
  ("оеевнйисст"),
  ("оттаряяевл"),
  ("лбюящ-оялд"),
  ("еуитсоочюб"),
  ("нионсызймх"),
  ("шмеянситор"),
  ("уфкртгтооо"),
  ("кудррвуоа.")
)

#решетка Кардано
grid = (
  (0, 1, 0, 0, 0, 0, 1, 0, 0, 1),
  (1, 0, 0, 0, 1, 0, 0, 0, 0, 0),
  (0, 1, 0, 0, 0, 1, 0, 0, 1, 0),
  (0, 0, 1, 0, 0, 0, 0, 1, 0, 0),
  (1, 0, 0, 1, 0, 1, 1, 0, 0, 1),
  (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
  (1, 1, 0, 0, 0, 0, 1, 0, 1, 0),
  (0, 0, 1, 0, 0, 0, 0, 0, 0, 0),
  (0, 0, 0, 0, 1, 0, 0, 0, 1, 0),
  (0, 0, 1, 0, 0, 0, 0, 1, 0, 0))

#вывод сетки
for i in range(size):
  print (my_list[i])

#вывод после поворота на 0 градусов 
print('')  
print ('0:')
for i in range(size):
  for j in range(size):
    if grid[i][j] == 1:
      print (my_list[i][j], end = '')

#вывод после поворота на 90 градусов 
print('')
print('90:')
for i in range(size):
  for j in range(size):
    if grid[size-j-1][i] == 1:
      print (my_list[i][j], end = '')
      
 #вывод после поворота на 180 градусов      
print('')
print('180:')
for i in range(size):
  for j in range(size):
    if grid[size-i-1][size-j-1] == 1:
      print (my_list[i][j], end = '')

#вывод после поворота на 270 градусов     
print('')
print('270:')
for i in range(size):
  for j in range(size):
    if grid[j][size-i-1] == 1:
      print (my_list[i][j], end = '')

########итоговый вывод

##>> тСПвнперот
##>> ьеосФдптор
##>> оеевнйисст
##>> оттаряяевл
##>> лбюящ-оялд
##>> еуитсоочюб
##>> нионсызймх
##>> шмеянситор
##>> уфкртгтооо
##>> кудррвуоа.

##>> 0:
##>> СетьФейстеля-одинизметодо
##>> 90:
##>> впостроенияблочныхшифров.
##>> 180:
##>> Представляетсобоймногокра
##>> 270:
##>> тноповторяющуюсяструктуру

