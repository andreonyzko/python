msg= input('Digite algo: ')
qnt= int(input('Quantas vezes repetir? '))
print('{}*{}= {}\n'.format(msg,qnt,msg*qnt))
print('{:{}}'.format(msg,qnt), end='')
print('{:>20}'.format(msg))
print('{:<20}'.format(msg))
print('{:^20}'.format(msg))
print('{:=^20}'.format(msg))