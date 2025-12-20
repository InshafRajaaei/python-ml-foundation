# Script 4: The Country Lookup (Nested Access)
# Concept: Complex JSON-like navigation.

# 1. Define this data:
# world = {
#     "Asia": {
#         "Japan": "Tokyo",
#         "Sri Lanka": "Colombo",
#         "India": "New Delhi"
#     },
#     "Europe": {
#         "France": "Paris",
#         "Germany": "Berlin"
#     }
# }
# 2. Ask the user: "Enter a continent:"
# 3. Ask the user: "Enter a country:"
# 4. Print the capital city by accessing world[continent][country].
# 5. Bonus: Handle errors (e.g., if the user types a continent that doesn't exist) using if/else or .get().

world = {
    "Asia" : {
        "Japan" : "Tokyo",
        "Sri Lanka" : "Colombo",
        "India" : "New Delhi"
    },
    "Europe" : {
        "France" : "Paris",
        "Germany" : "Berlin"
    }
}
input_continent = input("Enter a contienent:")
input_country = input("Enter a country:")
if input_continent in world:
    if input_country in world[input_continent]:
        print(f"The capital of {input_country} is {world[input_continent][input_country]}.")
    else:
        print(f"Country '{input_country}' not found in continent '{input_continent}'.")