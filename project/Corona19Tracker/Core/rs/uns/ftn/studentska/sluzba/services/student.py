from abc import abstractmethod

from rs.uns.ftn.studentska.sluzba.services.fakultet import ServiceBase


class StudentUcitatiBase(ServiceBase):
    @abstractmethod
    def ucitati_studente(self, lista_fakulteta):
        pass


class StudentPrikazBase(ServiceBase):
    @abstractmethod
    def prikazati_studente(self, lista_studenata):
        pass