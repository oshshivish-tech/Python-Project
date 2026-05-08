import random

subjects=[
    "Shahrukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai Cat",
    "An Alien from Mars",
    "A Dog in Delhi",
    "An Engineer in Bangalore",
]


actions=[
    "backflips while yodeling at",
    "teaches yoga to",
    "photobombs",
    "challenges to a dance-off",
    "accidentally invents time travel with",
    "confuses with a samosa",
    "mistakes for pizza and bites",
    "hypnotizes with their stare at",
    "declares war on",
    "proposes marriage to",
    "roasts on national television",
    "steals the WiFi password from",
]



places_or_things=[
    "while riding a unicorn down the Ganges",
    "inside Amitabh Bachchan's Twitter account",
    "on a WhatsApp group chat",
    "during a live IPL match with commentary",
    "in a desi grocery store at 3 AM",
    "on top of the Taj Mahal wearing roller skates",
    "while live-streaming on TikTok",
    "inside a samosa factory",
    "at a wedding where nobody invited them",
    "in front of the Statue of Liberty (in India)",
    "while juggling biryani plates",
    "on a random street corner in Mumbai traffic",
    "inside a Bollywood dance sequence",
]

while True:
    subject = random.choice(subjects)
    action = random.choice(actions)
    place_or_thing = random.choice(places_or_things)

    headline = f"BREAKING NEWS:  {subject} {action} {place_or_thing}!"
    print(headline)

    another = input("Do you want another headline? (y/n): ").strip().lower()
    if another != 'y':
        break
print("Thank you for using the Fake News Headline Generator!")




