class Wizyt:
    def __init__(self, name, last_name, position, firm, email):
        self.name = name
        self.last_name = last_name
        self.position = position
        self.firm = firm
        self.email = email

    def __repr__(self):
        return f"imie={self.name}, nazwisko={self.last_name}, email={self.email}"


contacts = [
    Wizyt(name="Karol", last_name="Świderski", position="Kasjer", firm="Żabka", email="kswider@wp.pl"),
    Wizyt(name="Marcin", last_name="Kozanecki", position="Kasjer", firm="Żabka", email="markoz@wp.pl"),
    Wizyt(name="Jan", last_name="Popiela", position="Kurier", firm="DHL", email="janko@wp.pl"),
    Wizyt(name="Karol", last_name="Wiśniewski", position="Influencer", firm="Ekipa", email="friz@wp.pl"),
    Wizyt(name="Weronika", last_name="Sowa", position="Influencer", firm="Ekipa", email="wera@wp.pl"),
]


sorted_by_name = sorted(contacts, key=lambda x: x.name)
sorted_by_last_name = sorted(contacts, key=lambda x: x.last_name)
sorted_by_email = sorted(contacts, key=lambda x: x.email)


print("Posortowane według imienia:")
for cont in sorted_by_name:
    print(cont)

print("\nPosortowane według nazwiska:")
for cont in sorted_by_last_name:
    print(cont)

print("\nPosortowane według e-maila:")
for cont in sorted_by_email:
    print(cont)
