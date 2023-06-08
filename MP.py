# Define the knowledge base
restaurants = {
    "Hotel Shivsagar": {
        "cuisine": "Chineese",
        "price": "Moderate",
        "atmosphere": "Romantic",
        "rating": 4.5
    },
    "Hotel Nikita": {
        "cuisine": "South-Indian",
        "price": "Low",
        "atmosphere": "Casual",
        "rating": 4.0
    },
    "Hotel Rajashree": {
        "cuisine": "Punjabi",
        "price": "High",
        "atmosphere": "Formal",
        "rating": 4.7
    }
}

# Define the rules
rules = [
    {
        "condition": lambda input: (input["cuisine"] == "Chineese") and (input["price"] == "moderate"),
        "output": "Hotel Shivsagar"
    },
    {
        "condition": lambda input: (input["cuisine"] == "South-Indian") and (input["price"] == "low"),
        "output": "Hotel Nikita"
    },
    {
        "condition": lambda input: (input["cuisine"] == "Punjabi") and (input["price"] == "high"),
        "output": "Hotel Rajashree"
    },
    {
        "condition": lambda input: (input["atmosphere"] == "romantic") and input["rating"] >= 4.0,
        "output": "Hotel Shivsagar"
    },
    {
        "condition": lambda input: (input["atmosphere"] == "casual") and input["rating"] >= 4.5,
        "output": "Hotel Nikita"
    },
    {
        "condition": lambda input: (input["atmosphere"] == "formal") and input["rating"] >= 4.7,
        "output": "Hotel Rajashree"
    }
]

# Define the user interface
print("Welcome to the Pure Veg Restaurant Recommender")
print("Please answer the following questions to receive a recommendation.")
print()

#input
cuisine = input("What type of cuisine do you prefer? \n 1.Chineese \n 2.South-Indian \n 3.Punjabi \n").lower()
price = input("What price range are you comfortable with?\n 1.High \n 2.Moderate \n 3.Low\n  ").lower()
atmosphere = input("What kind of atmosphere do you prefer?\n 1.Romantic \n 2.Casual \n 3.Formal\n ").lower()
rating = float(input("What minimum rating do you require?\n 1. 4.0 \n 2. 4.5 \n 3. 4.7\n "))

match cuisine:
    case "1":
        cuisine = "Chineese"
    case "2":
        cuisine = "South-Indian"
    case "3":
        cusine = "Punjabi"

match price:
    case "1":
        price = "high"
    case "2":
        price = "moderate"
    case "3":
        price = "low"

match atmosphere:
    case "1":
        atmosphere = "romantic"
    case "2":
        atmosphere = "casual"
    case "3":
        atmosphere = "formal"


match rating:
    case 1:
        rating = 4.0
    case 2:
        rating = 4.5
    case 3:
        rating = 4.7
    

input_data = {
    "cuisine": cuisine,
    "price": price,
    "atmosphere": atmosphere,
    "rating": rating
}

# Define the inference engine
def infer(input_data, rules):
    for rule in rules:
        if rule["condition"](input_data):
            return rule["output"]
    return "No recommendation"

# Output the recommendation

print()
print()
print("You selected the following preferrences:")
print()
print("     cuisine-->", cuisine.upper())
print("     price-->", price.upper())
print("     atmosphere-->", atmosphere.upper())
print("     rating-->", rating)
print()



recommendation = infer(input_data, rules)
if recommendation == "No recommendation":
    print("Sorry, we could not find any restaurant that matches your criteria.")
else:
    print("Based on your input, we recommend visiting:", recommendation)













