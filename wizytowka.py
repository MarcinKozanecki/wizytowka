from faker import Faker


class Wizyt:
    def __init__(self, name, last_name, email, phone):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def label_length(self):
        return len(self.name) + len(self.last_name)


class BaseContact(Wizyt):
    def __init__(self, name, last_name, email, phone):
        super().__init__(name, last_name, email, phone)


class BusinessContact(BaseContact):
    def __init__(self, name, last_name, email, phone, position, firm, firm_phone):
        super().__init__(name, last_name, email, phone)
        self.position = position
        self.firm = firm
        self.firm_phone = firm_phone


faker = Faker("pl_PL")

def create_contacts(contact_type, quantity):
 
    contacts = []
    
    if contact_type == 'base':
        contacts = [
            BaseContact(
                name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                phone=faker.phone_number()
            ) for _ in range(quantity)
        ]
    
    elif contact_type == 'business':
        contacts = [
            BusinessContact(
                name=faker.first_name(),
                last_name=faker.last_name(),
                email=faker.email(),
                phone=faker.phone_number(),
                position=faker.job(),
                firm=faker.company(),
                firm_phone=faker.phone_number()
            ) for _ in range(quantity)
        ]
    
    return contacts





def main():
    quantity = int(input("Podaj ilość wizytówek do stworzenia: "))

    contact_type = input("Podaj typ wizytówek ('base' lub 'business'): ").lower()

    contacts = create_contacts(contact_type, quantity)

    if contact_type == "base":
        for contact in contacts:
            print(f"Wybieram numer:{contact.phone} i dzwonię do {contact.name} {contact.last_name}. Długość imienia i nazwiska: {contact.label_length()}")
            print("-" * 50)

    elif contact_type=="business":
        for contact in contacts:
            print(f"Wybieram numer:{contact.firm_phone} i dzonię do {contact.firm} na stanowisko {contact.position}. Długość imienia i nazwiska: {contact.label_length()}")
            print("-" * 50)

    else:
        print("Niepoprawny typ wizytówki. Wybierz 'base' lub 'business'.")
        return


    


main()
