from get_data_from_web import vaistai
import sqlite3

print(vaistai[0])
# print(vaistai[0]["vodka"])
print(vaistai[0].get("vodka", "suka bleat is not detected"))

for v in vaistai[:5]:
    name = v.get("name", "")
    print(f"Name: {name[:10]} || Price: {v.get('price')} || Discount: {v.get('discount')}")
