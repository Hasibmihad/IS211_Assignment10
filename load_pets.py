import sqlite3 as lite
import sys
conn = lite.connect('pets.db')
with conn:
    cursor = conn.cursor()
    person_data = [
        (1, 'James', 'Smith', 41),
        (2, 'Diana', 'Greene', 23),
        (3, 'Sara', 'White', 27),
        (4, 'William', 'Gibson', 23)
    ]

    pet_data = [
        (1, 'Rusty', 'Dalmation', 4, 1),
        (2, 'Bella', 'Alaskan Malamute', 3, 0),
        (3, 'Max', 'Cocker Spaniel', 1, 0),
        (4, 'Rocky', 'Beagle', 7, 0),
        (5, 'Rufus', 'Cocker Spaniel', 1, 0),
        (6, 'Spot', 'Bloodhound', 2, 1)
    ]

    person_pet_data = [
        (1, 1),
        (1, 2),
        (2, 3),
        (2, 4),
        (3, 5),
        (4, 6)
    ]


    cursor.executemany("INSERT INTO person VALUES (?, ?, ?, ?)", person_data)
    cursor.executemany("INSERT INTO pet VALUES (?, ?, ?, ?, ?)", pet_data)
    cursor.executemany("INSERT INTO person_pet VALUES (?, ?)", person_pet_data)


conn.close()