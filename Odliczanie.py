"""
	Do zrobienia:
	Odliczanie czasu DONE
	Input tylko wartosci liczbowe, zmieniac liczby ujemne na naturalne DONE
	Edycja pliku DONE
	GUI
	Tekst do podania	DONE
"""
import time
import datetime

 #Time input
class Podaj_czas:
	
	@staticmethod
	def min_input():
		while True:
			try:
				minuty = input("Minut: ")
				if len(minuty)==0:
					minuty = 0
					return minuty
				else:
					return abs(int(minuty))
			except:
				print ("Wpisz wartość w cyfrach arabskich (0,1,2,3,4,5,6,7,8,9)")


	@staticmethod
	def sec_input():
		while True:
			try:
				sekundy = input("Sekund: ")
				if len(sekundy)==0:
					sekundy = 0
					return sekundy
				else:
					return abs(int(sekundy))
			except:
				print ("Wpisz wartość w cyfrach arabskich (0,1,2,3,4,5,6,7,8,9)")


def TimeChanger(minuty, sekundy):
    Sek = int(minuty)*60
    Sek = Sek + int(sekundy)
    return  int(Sek)

    #Counting down, editing TXT file
def odliczanie(odliczacz):
	a=0
	czas_pozostaly = odliczacz
	czas_pozostaly2 = odliczacz
	#print(f"Czas pozostały: {czas_pozostaly} Sekund ||Czas systemowy {str(datetime.datetime.now().time())}")
	while(a<czas_pozostaly):
		a+=1
		czas_pozostaly2-=1
		time.sleep(1)
		czas_txt=open(nazwa_pliku, "w")
		czas_txt.write(f"{wiadomosc} {czas_pozostaly2} Sekund")
		print(f"{czas_pozostaly2} Sekund || Czas systemowy {str(datetime.datetime.now().time())}")

nazwa_pliku = str(input("Podaj nazwe pliku z końcówką .txt "))
czas_txt=open(nazwa_pliku, "w")
wiadomosc = str(input("Podaj wiadomosc: "))
print("Podaj czas do odliczenia ")


minuty = Podaj_czas.min_input()
sekundy = Podaj_czas.sec_input()

odliczacz=TimeChanger(minuty,sekundy)
print(odliczanie(odliczacz))
