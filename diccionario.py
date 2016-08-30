from rae import Drae
from rae import Dpd
def diccionario(input):
    try:
        from rae import Drae
        drae = Drae()
        drae.search(u'input')
    except:
        dpd = Dpd()
        dpd.search(u'input')