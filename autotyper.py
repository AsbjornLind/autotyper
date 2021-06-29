from pynput.keyboard import Key, Controller
import time


print("--------------------------------------")
print("--------------------------------------")
print("   PRESS ENTER TO START OR Q TO QUIT")
print("--------------------------------------")
print("--------------------------------------")
decission = input("")

while decission.lower() != 'q':
    formular = input("""indtast den formular du vil have skrevet ind, uden tallet til sidst. eksempelvis: 
    jeg vil have skrevet tal ind fra 1-100 af  "=JDK!A23" 
    skriv så kun "=JDK!A" uden anførselstegn.
    """)
    print("---------------")

    start_tal = int(input("""Hvilket tal skal jeg starte fra? I eksemplet vil det være 1.
    """))
    print("---------------")

    slut_tal = int(input("""hvilket række er den sidste? I eksemplet er det 100.
    """))
    print("---------------")

    gentagelse = int(input("""Hvor mange tv stationer har hver kampagne?
    """))
    print("---------------")

    waiter = int(input("Hvor mange sekunder vil du vente før jeg starter?" ))
    print(f"""Du har nu {waiter} sekunder til at klikke i den celle jeg skal starte i! :)  
    SKYND DIG! """)

    time.sleep(waiter)
    keyboard = Controller()
    for i in range(start_tal,slut_tal+1):
        for _ in range(0,gentagelse):
            cell_value = f"{formular}{i}"

            for letters in cell_value:
                keyboard.type(letters)

            time.sleep(0.15)
            keyboard.press(Key.enter)
            keyboard.release(Key.enter)
    
    print("     Skud ud til Asbjørn")
    time.sleep(2)
    print("--------------------------------------")
    print("--------------------------------------")
    print("   PRESS ENTER TO START OR Q TO QUIT")
    print("--------------------------------------")
    print("--------------------------------------")
    decission = input("")





##pynput skal være rigtig version for det virker til pyinstaller
#https://stackoverflow.com/questions/63681770/getting-error-when-using-pynput-with-pyinstaller
