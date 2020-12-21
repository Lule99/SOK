
class Fakultet(object):

    def __init__(self,*args,**kwargs):
        self.__oznaka = kwargs.get('oznaka', None)
        self.__naziv=kwargs.get('naziv',None)
        self.__adresa=kwargs.get('adresa',None)

    @property
    def oznaka(self):
        return self.__oznaka

    @oznaka.setter
    def oznaka(self, vrednost):
        if isinstance(vrednost, str):
            self.__oznaka = vrednost
        else:
            raise TypeError('Mora biti tipa string')
    @property
    def naziv(self):
        return self.__naziv
    @naziv.setter
    def naziv(self,vrednost):
        if isinstance(vrednost,str):
            self.__naziv=vrednost
        else:
            raise TypeError('Mora biti tipa string')

    @property
    def adresa(self):
        return self.__adresa

    @adresa.setter
    def adresa(self, vrednost):
        if isinstance(vrednost, str):
            self.__adresa = vrednost
        else:
            raise TypeError('Mora biti tipa string')



class Student(object):

    def __init__(self,*args,**kwargs):
        self.__indeks = kwargs.get('indeks', None)
        self.__ime=kwargs.get('ime',None)
        self.__prezime = kwargs.get('prezime', None)
        self.__email = kwargs.get('email', None)
        self.__fakultet = kwargs.get('fakultet',None)


    @property
    def indeks(self):
        return self.__indeks

    @indeks.setter
    def indeks(self, vrednost):
        if isinstance(vrednost, str):
            self.__indeks = vrednost
        else:
            raise TypeError('Mora biti tipa string')

    @property
    def ime(self):
        return self.__ime

    @ime.setter
    def ime(self, vrednost):
        if isinstance(vrednost, str):
            self.__ime = vrednost
        else:
            raise TypeError('Mora biti tipa string')

    @property
    def prezime(self):
        return self.__prezime

    @prezime.setter
    def prezime(self, vrednost):
        if isinstance(vrednost, str):
            self.__prezime = vrednost
        else:
            raise TypeError('Mora biti tipa string')


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, vrednost):
        if isinstance(vrednost, str):
            self.__email = vrednost
        else:
            raise TypeError('Mora biti tipa string')

    @property
    def fakultet(self):
        return self.__fakultet

    @fakultet.setter
    def fakultet(self, vrednost):
        if isinstance(vrednost, Fakultet):
            self.__fakultet = vrednost
        else:
            raise TypeError('Mora biti tipa Fakultet')
