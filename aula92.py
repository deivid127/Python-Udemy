# dir, hasattr e getattr em Python
string = 'Luiz'
metodo = 'upper'

if hasattr(string, 'upper'):
    print('Existe upper')
    print(getattr(string, metodo)())
else:
    print('Não existe o método', metodo)    
