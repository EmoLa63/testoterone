import os

def run_as_admin():
    print("Je suis en mode administrateur!")
    # Insérer ici les commandes souhaitées 
    os.system("notepad.exe") # ouvre le bloc note (exemple d'action simple)

if __name__ == "__main__":
    run_as_admin()
