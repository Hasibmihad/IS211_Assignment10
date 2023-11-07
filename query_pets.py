import sqlite3 as lite
import sys
def display_person(person):
    print(f"{person[1]} {person[2]}, {person[3]} years old")

def display_pet(person_name,pet):
    #print(pet)
    print(f"{person_name} owned {pet[0]}, a {pet[1]}, that was {pet[2]} years old")
conn = lite.connect('pets.db')
with conn:
    cursor = conn.cursor()
    
    while True:
        try:
            person_id = int(input("Enter person's ID number (or -1 to exit): "))
            if person_id == -1:
                break

            
            cursor.execute("SELECT * FROM person WHERE id=?", (person_id,))
            person = cursor.fetchone()

            if person:
                display_person(person)

                cursor.execute("SELECT pet.name, pet.breed, pet.age FROM pet "
                            "JOIN person_pet ON pet.id = person_pet.pet_id "
                            "WHERE person_pet.person_id=?", (person_id,))
                pets = cursor.fetchall()

                if pets:
                    person_name=person[1]+" "+person[2]
                    for pet in pets:
                        
                        display_pet(person_name,pet)
                else:
                    print("This person does not own any pet !!!! :( ")
            else:
                print("Person with the given ID does not exist.")
        except ValueError:
            print("Invalid input. Please enter a valid person ID.")


conn.close()