'''

'''
import json
from os import path

class Vehicle:
    def __init__(self,manufacturer,model,yearOfProduction):
        self.manufacturer=manufacturer
        self.model = model
        self.yearOfProduction = yearOfProduction
    def __repr__(self):
        return str(self.manufacturer) + " " + str(self.model) +  " ("+str(self.yearOfProduction)+")"
    def __eq__(self,other):
        if(self.manufacturer == other.manufacturer and self.model == other.model and self.yearOfProduction == other.yearOfProduction):
            return True
        else:
            return False

class Car(Vehicle):
    def __init__(self,manufacturer,model,yearOfProduction,numberOfDoors,type):
        super().__init__(manufacturer,model,yearOfProduction)
        self.numberOfDoors=numberOfDoors
        self.type = type
    def __eq__(self,other):
        if(super(Car,self).__eq__(other) and self.type==other.type and self.numberOfDoors==other.numberOfDoors):
           return True
        else:
            return False 


class Truck(Vehicle):
    def __init__(self,manufacturer,model,yearOfProduction,loadWeight):
        super().__init__(manufacturer,model,yearOfProduction)
        self.loadWeight = loadWeight


class Bus(Vehicle):
    def __init__(self,manufacturer,model,yearOfProduction,numberOfSeats):
        super().__init__(manufacturer,model,yearOfProduction)
        self.numberOfSeats=numberOfSeats

class Part:
    def __init__(self,vehicle,name,number,price):
        self.vehicle = vehicle
        self.name=name
        self.number = number
        self.price = price
    def __repr__(self):
        return str(self.name) + " (" + str(self.vehicle) + ")-"+str(self.price)

#auto = Car("Audi","A6",2016,5,"limo")
#print(type(auto)==Car)
#auto2 = Car("Audi","A",2016,5,"limo")
#print(auto==auto2)
def kreirajVozilo():

    opcija = int(input("1)Automobil\n2)Kamion\n3)Autobus:\n"))

    proizvodjac=input("Unesite proizvodjaca: ")
    model=input("Unesite model: ")
    godinaProizvodnje=input("Unesite godinu proizvodnje vozila: ")
    print("Koja kategorija vozila je u pitanju:")

    if opcija==1:
        brojVrata=int(input("Unesite broj vrata automobila: "))
        tip=input("Unesite tip automobila: ")
        vozilo=Car(proizvodjac,model,godinaProizvodnje,brojVrata,tip)
    elif opcija==2:
        maksNosivost=int(input("Unesite maksimalnu nosivost kamion u kg: "))
        vozilo = Truck(proizvodjac,model,godinaProizvodnje,maksNosivost)
    elif opcija==3:
        brojSjedista=int(input("Unesite broj sjedista autobusa: "))
        vozilo = Bus(proizvodjac,model,godinaProizvodnje,brojSjedista)
   
    return vozilo  

def dodajDio():
    print("Unesite podatke o vozilu za koji je ovaj dio!")
    vozilo = kreirajVozilo()
      
    ime = input("Unesite ime dijela: ")
    brojDijela = input("Unesite serijski broj dijela: ")
    cijena = float(input("Unesite cijenu dijeal: "))
    


    if type(vozilo)==Car:
        x={
            "ImeDijela":ime,
            "SerijskiBroj":brojDijela,
            "Cijena":cijena,
            "Vozilo":{
                "Proizvodjac":vozilo.manufacturer,
                "Model":vozilo.model,
                "GodinaProizvodnje":vozilo.yearOfProduction,
                "BrojVrata":vozilo.numberOfDoors,
                "Tip":vozilo.type
            }
        }
        if path.exists("AutoDijelovi.json"):
            with open("AutoDijelovi.json","r") as f:
                data = json.load(f)
                data.append(x)
        else:
            data=[]
            data.append(x)
        with open("AutoDijelovi.json","w") as f:
            json.dump(data,f,indent=4)
    elif type(vozilo)==Truck:
        x={
            "ImeDijela":ime,
            "SerijskiBroj":brojDijela,
            "Cijena":cijena,
            "Vozilo":{
                "Proizvodjac":vozilo.manufacturer,
                "Model":vozilo.model,
                "GodinaProizvodnje":vozilo.yearOfProduction,
                "Nosivost":vozilo.loadWeight,
            }
        }
        if path.exists("KamionDijelovi.json"):
            with open("KamionDijelovi.json","r") as f:
                data = json.load(f)
                data.append(x)
        else:
            data=[]
            data.append(x)
        with open("KamionDijelovi.json","w") as f:
            json.dump(data,f,indent=4)
        
        
    
    elif type(vozilo)==Bus:
        x={
            "ImeDijela":ime,
            "SerijskiBroj":brojDijela,
            "Cijena":cijena,
            "Vozilo":{
                "Proizvodjac":vozilo.manufacturer,
                "Model":vozilo.model,
                "GodinaProizvodnje":vozilo.yearOfProduction,
                "BrojSjedista":vozilo.numberOfSeats
            }
        }

        if path.exists("BusDijelovi.json"):
            with open("BusDijelovi.json","r") as f:
                data = json.load(f)
                data.append(x)
        else:
            data=[]
            data.append(x)
        with open("BusDijelovi.json","w") as f:
            json.dump(data,f,indent=4)

def pretraziDjelove():
    print("Za koju kategoriju trazite dijelove:\n")
    kategorija = int(input("1)Automobil\n2)Kamion\n3)Autobus\n"))
    if kategorija==1:
        putanja="AutoDijelovi.json"
    elif kategorija==2:
        putanja="KamionDijelovi.json"
    elif kategorija==3:
        putanja="BusDijelovi.json"
    

    #with open(putanja,"r") as f:
     #   podaci = json.load(f)
           

action=0
while action!=-1:
    print("Meni:\n1:Dodaj dio\n2:Pretrazi djelove\n3:Pregledaj sve djelove za vozilo!\n-1:Kraj")
    action=int(input("Unesite broj akcije koju zelite da izvrsite: "))
    if action==1:
        dodajDio()
        #print(action)
    elif action==2:
        pretraziDjelove()
       # print(action)
    elif action==3:
        #izlistajDjelove()
        print(action)
    elif action==-1:
        break
    else:
        print("Pogresan unos!!")
    provjera = int(input("Da li zelite da izvrsite jos neku akciju?\nUnesite 1 za jos akcija, a 2 za kraj rada "))
    print("Provjera: " + str(provjera))
    if provjera==1:
        action=0
    elif provjera==2:
        action=-1

print("Kraj rada!!!")
