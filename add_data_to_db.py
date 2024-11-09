from get_data_from_web import vaistai
import sqlite3

print(vaistai[0])
# print(vaistai[0]["vodka"])
print(vaistai[0].get("vodka", "suka bleat is not detected"))

for v in vaistai[:5]:
    name = v.get("name", "")
    print(f"Name: {name[:10]} || Price: {v.get('price')} || Discount: {v.get('discount')}")

conn = sqlite3.connect("duombaze.db") # (automatically creates if not exist)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS nereceptiniai_vaistai (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL,
    discount BOOLEAN NOT NULL             
)
""")

for v in vaistai[:5]:
    cursor.execute(
        "INSERT INTO nereceptiniai_vaistai (name, price, discount) VALUES (?, ?, ?)",
        (v.get("name"), v.get("price"), v.get("discount"))
    )

conn.commit()

# cursor.execute("DELETE FROM nereceptiniai_vaistai")
# conn.commit()