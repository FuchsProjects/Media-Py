a = int(input('Primeiro Bimeste:'))
if a > 10:
    a = int(input('Sua nota não pode ser maior que 10, Digite novamente:'))
b = int(input('Segundo Bimeste:'))
if b > 10:
    b = int(input('Sua nota não pode ser maior que 10, Digite novamente:'))
c = int(input('Terceiro Bimeste:'))
if c > 10:
    c = int(input('Sua nota não pode ser maior que 10, Digite novamente:'))
d = int(input('Quarto Bimeste:'))
if d > 10:
    d = int(input('Sua nota não pode ser maior que 10, Digite novamente:'))
media = ( a + b + c + d) /4
# if a <= 10 and b <= 10 and c <= 10 and d <= 10
#     print('')
print('Média = {}'.format(media))


