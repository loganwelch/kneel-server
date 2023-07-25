import sqlite3
import json
from models import Metal

METALS = [
    {
        "id": 1,
        "metal": "Sterling Silver",
        "price": 12.42
    },
    {
        "id": 2,
        "metal": "14K Gold",
        "price": 736.4
    },
    {
        "id": 3,
        "metal": "24K Gold",
        "price": 1258.9
    },
    {
        "id": 4,
        "metal": "Platinum",
        "price": 795.45
    },
    {
        "id": 5,
        "metal": "Palladium",
        "price": 1241
    }
]


def get_all_metals():
    # Open a connection to the database
    with sqlite3.connect("./kneel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM metals m
        """)

        # Initialize an empty list to hold all animal representations
        metals = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row
            metal = Metal(row['id'], row['metal'], row['price'])

            # Add the dictionary representation of the animal to the list
            metals.append(metal.__dict__)

    return metals

# Function with a single parameter


def get_single_metal(id):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Use a ? parameter to inject a variable's value
        # into the SQL statement.
        db_cursor.execute("""
        SELECT
            m.id,
            m.metal,
            m.price
        FROM metals m
        WHERE m.id = ?
        """, (id, ))

        #animals = []

        # Load the single result into memory
        data = db_cursor.fetchone()
        if data:
        # Create an animal instance from the current row
            metal = Metal(data['id'], data['metal'], data['price'])

            return metal.__dict__
        else:
            return None


def create_metal(metal):
    # Get the id value of the last animal in the list
    max_id = METALS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    metal["id"] = new_id

    # Add the animal dictionary to the list
    METALS.append(metal)

    # Return the dictionary with `id` property added
    return metal


def delete_metal(id):
    # Initial -1 value for animal index, in case one isn't found
    metal_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, metal in enumerate(METALS):
        if metal["id"] == id:
            # Found the metal. Store the current index.
            metal_index = index

    # If the metal was found, use pop(int) to remove it from list
    if metal_index >= 0:
        METALS.pop(metal_index)


def update_metal(id, new_metal):
    with sqlite3.connect("./kneel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Metals
            SET
                metal = ?,
                price = ?
        WHERE id = ?
        """, (new_metal['metal'], new_metal['price'], id, ))

        # Were any rows affected?
        # Did the client send an `id` that exists?
        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        # Forces 404 response by main module
        return False
    else:
        # Forces 204 response by main module
        return True
