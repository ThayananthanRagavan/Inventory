class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item_id, quantity, price):
        if item_id in self.inventory:
            return "Artikel-ID existiert bereits."
        self.inventory[item_id] = {'name': item_id, 'quantity': quantity, 'price': price}
        return "Artikel wurde erfolgreich hinzugefügt"

    def insert_data(self, item_id, quantity, price):
        self.inventory[item_id] = {'name': item_id, 'quantity': quantity, 'price': price}

    def remove_item(self, item_id):
        if item_id in self.inventory:
            item = self.inventory.pop(item_id, None)
            if item:
                return f"Artikel {item_id} wurde erfolgreich gelöscht"
        return "Artikel-ID nicht vorhanden"

    def update_item(self, item_id, quantity, price):
        if item_id in self.inventory:
            self.inventory[item_id] = {'name': item_id, 'quantity': quantity, 'price': price}
            return "Artikel-ID wurde erfolgreich aktualisiert."
        return "Artikel-ID nicht vorhanden"

    def display_inventory(self):
        if not self.inventory:
            return "Das Inventar ist leer."
        result = []
        for item_id, details in self.inventory.items():
            result.append(f"Artikel_ID: {item_id}")
            result.append(f"Name: {details['name']}")
            result.append(f"Menge: {details['quantity']}")
            result.append(f"Preis: {details['price']:.2f} CHF")
            result.append("-" * 20)
        return "\n".join(result)

def main():
    inventory = Inventory()
    while True:
        print("\nInventarverwaltungssystem")
        print("1. Artikel hinzufügen")
        print("2. Artikel entfernen")
        print("3. Artikel aktualisieren")
        print("4. Inventar anzeigen")
        print("5. Beenden\n")

        choice = input("Wählen Sie eine Option: ")

        if choice == '1':
            item_id = input("Geben Sie bitte die Artikel-ID ein: ")
            quantity = int(input("Geben Sie die Menge des Artikels ein: "))
            price = float(input("Geben Sie bitte den Preis des Artikels ein: "))
            print(inventory.add_item(item_id, quantity, price))
        elif choice == '2':
            item_id = input("Geben Sie bitte die Artikel-ID ein: ")
            print(inventory.remove_item(item_id))
        elif choice == '3':
            item_id = input("Geben Sie die Artikel-ID ein, die aktualisiert werden soll: ")
            quantity = int(input("Geben Sie die Menge des Artikels ein: "))
            price = float(input("Geben Sie bitte den Preis des Artikels ein: "))
            print(inventory.update_item(item_id, quantity, price))
        elif choice == '4':
            print(inventory.display_inventory())
        elif choice == '5':
            print("Programm beendet.")
            break
        else:
            print("Ungültige Auswahl. Bitte versuchen Sie es erneut.")

if __name__ == "__main__":
    main()
