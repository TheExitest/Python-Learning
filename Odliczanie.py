import time


def TimeChanger(minuty,sekundy):
    Sek = int(minuty)*60
    Sek = Sek + int(sekundy)
    return  int(Sek)


def odliczanie(odliczacz):
	a=0
	czas_pozostaly = odliczacz
	while(a<odliczacz):
		a=+1
		czas_pozostaly+-1
		time.sleep(1)
	return czas_pozostaly

print("Podaj czas do odliczenia ")
minuty = input("Minut: ")
sekundy = input("Sekund: ")

odliczacz=TimeChanger(minuty,sekundy)

while(odliczanie(odliczacz)>0):
	print(f"{czas_pozostaly} Sekund")

"""
print(TimeChanger(minuty,sekundy))
print(f"Czas do odliczenia: {minuty} Minut i {sekundy} Sekund")
"""