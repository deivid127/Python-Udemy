# try, except, else e finally
try:
    print('ABRIR ARQUIVO')
    8/0
except ZeroDivisionError as e:
    print(e.__class__.__name__)
    print(e)
    print('DIVIDIU ZERO')
except IndexError:
    print('IndexError')
except (NameError, ImportError):
    print('NameError + ImportError')
else:
    print('Não deu erro')
finally:
    print('FECHAR ARQUIVO')