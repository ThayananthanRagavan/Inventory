inventory = {}


def add_item():
    item_id = input("Geben Sie bitte die Artikel-ID ein: ")
    if item_id in inventory:
        print("Artikel-ID existiert bereits. ")
        return
    insert_data(item_id)
    print("Artikel wurde erfolgreich hinzugefügt")


def insert_data(item_id):
    quantity = int(input("Geben Sie die Menge des Artikels ein: "))
    price = float(input("Geben Sie bitte den Preis des Artikels ein: "))
    inventory[item_id] = {'name': item_id, 'quantity': quantity, 'price': price}


def remove_item():
    item_id = input("Geben Sie bitte die Artikel-ID ein: ")
    if item_id in inventory:
        item = inventory.pop(item_id, None)
        if item:
            print(f"Artikel {item_id}wurde erfolgreich gelöscht")
        else:
            print("Artikel-ID nicht vorhanden")


def update_item():
    item_id = input("Geben Sie die Artikel-ID ein, die aktualisiert werden soll: ")
    if item_id in inventory:
        print("Geben Sie die neuen Daten ein: ")
        insert_data(item_id)
        print("Artikel-ID wurde erfolgreich aktualisiert. ")


def display_inventory():
    if not inventory:
        print("Das Inventar ist leer. ")
        return
    for item_id, details in inventory.items():
        print(f"Artikel_ID: {item_id}")
        print(f"Name: {details['name']}")
        print(f"Menge: {details['quantity']}")
        print(f"Preis: {details['price']:.2}CHF")
        print("-" * 20)


def main():
    while True:
        print("\nInventarverwaltungssystem")
        print("1. Artikel hinzufügen")
        print("2. Artikel entfernen")
        print("3. Artikel aktualisieren")
        print("4. Inventar anzeigen")
        print("5. Beenden")

        choice = input("Wählen Sie eine Option: ")

        if choice == '1':
            add_item()
        elif choice == '2':
            remove_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            display_inventory()
        elif choice == '5':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")


if __name__ == "__main__":
    main()