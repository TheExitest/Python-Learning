"""
	Do zrobienia:
	Odliczanie czasu DONE
	Input tylko wartosci liczbowe, zmieniac liczby ujemne na naturalne DONE
	Edycja pliku DONE
	GUI
	Tekst do podania	
"""
import time
import datetime


class Podaj_czas:
	
	@staticmethod
	def min_input():
		while True:
			try:
				minuty = abs(int(input("Minut: ")))
				return minuty
			except:
				print ("Wpisz wartość w cyfrach arabskich (0,1,2,3,4,5,6,7,8,9)")


	@staticmethod
	def sec_input():
		while True:
			try:
				sekundy = abs(int(input("Sekund: ")))
				return sekundy
			except:
				print ("Wpisz wartość w cyfrach arabskich (0,1,2,3,4,5,6,7,8,9)")


def TimeChanger(minuty, sekundy):
    Sek = int(minuty)*60
    Sek = Sek + int(sekundy)
    return  int(Sek)


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

		#print(f"{czas_pozostaly2} Sekund || Czas systemowy {str(datetime.datetime.now().time())}")

nazwa_pliku = str(input("Podaj nazwe pliku z końcówką .txt "))
wiadomosc = str(input("Podaj wiadomosc: "))
print("Podaj czas do odliczenia ")
minuty = Podaj_czas.min_input()
sekundy = Podaj_czas.sec_input()
czas_txt=open(nazwa_pliku, "w")

odliczacz=TimeChanger(minuty,sekundy)
print(odliczanie(odliczacz))
