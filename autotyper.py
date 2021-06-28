from pynput.keyboard import Key, Controller
import time

formular = input("""
indtast den formular du vil have skrevet ind, uden tallet til sidst. eksempelvis: 
jeg vil have skrevet tal ind fra 1-100 af  "=JDK!A23" 
skriv så kun "=JDK!A" uden anførselstegn.
""")

start_tal = int(input("""Hvilket tal skal jeg starte fra? I eksemplet vil det være 1./n
"""))
print("---------------")
slut_tal = int(input("""hvilket række er den sidste? I eksemplet er det 100.
"""))

waiter = int(input("Hvor mange sekunder vil du vente før jeg starter?" ))
print(f"""Du har nu {waiter} sekunder til at klikke i den celle jeg skal starte i! :)  
SKYND DIG! """)

time.sleep(waiter)
keyboard = Controller()
for i in range(start_tal,slut_tal+1):
    cell_value = f"{formular}{i}"

    for letters in cell_value:
        keyboard.type(letters)

    time.sleep(0.15)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
