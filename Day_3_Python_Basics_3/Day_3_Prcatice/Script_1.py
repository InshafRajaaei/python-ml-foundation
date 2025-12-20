# Script 1: The Inventory Manager (Dictionaries)
# Concept: Dictionary CRUD operations.

# 1. Create a dictionary called inventory with items: {"apples": 10, "bananas": 5, "oranges": 8}.

# 2. Ask the user: "What item did you buy?"

# 3. Ask the user: "How many?" (Convert to int).

# 4. Check if the item exists in the dictionary:

#     If yes: Add the quantity to the existing stock.

#     If no: Create a new key with that quantity.

# 5. Print the updated inventory.

inventory = {
    "apples": 10,
    "bananas": 5,
    "oranges": 8
    }
input_frt = input("What items dir d you buy :")
input_frt_cnt_temp = input("How many:")
input_frt_cnt = int(input_frt_cnt_temp)
for frt in inventory.keys():
    if frt == input_frt:
        inventory[frt] = inventory[frt] + input_frt_cnt
        break
    else:
        inventory[input_frt] = input_frt_cnt
        break

print("Updated Inventory:" , inventory)