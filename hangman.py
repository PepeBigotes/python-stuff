#!/usr/bin/env python3
#Created by PepeBigotes

import random
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

letters = ["q","w","e","r","t","y","u","i","o","p","a","s","d","f","g","h","j","k","l","z","x","c","v","b","n","m"]

#From https://gist.github.com/borlaym/585e2e09dd6abd9b0d0a
WORDS = [
    "aardvark",
    "albatross",
    "alligator",
    "alpaca",
    "ant",
    "anteater",
    "antelope",
    "ape",
    "armadillo",
    "donkey",
    "baboon",
    "badger",
    "barracuda",
    "bat",
    "bear",
    "beaver",
    "bee",
    "bison",
    "boar",
    "buffalo",
    "butterfly",
    "camel",
    "capybara",
    "caribou",
    "cassowary",
    "cat",
    "caterpillar",
    "cattle",
    "chamois",
    "cheetah",
    "chicken",
    "chimpanzee",
    "chinchilla",
    "chough",
    "clam",
    "cobra",
    "cockroach",
    "cod",
    "cormorant",
    "coyote",
    "crab",
    "crane",
    "crocodile",
    "crow",
    "curlew",
    "deer",
    "dinosaur",
    "dog",
    "dogfish",
    "dolphin",
    "dotterel",
    "dove",
    "dragonfly",
    "duck",
    "dugong",
    "dunlin",
    "eagle",
    "echidna",
    "eel",
    "eland",
    "elephant",
    "elk",
    "emu",
    "falcon",
    "ferret",
    "finch",
    "fish",
    "flamingo",
    "fly",
    "fox",
    "frog",
    "gaur",
    "gazelle",
    "gerbil",
    "giraffe",
    "gnat",
    "gnu",
    "goat",
    "goldfinch",
    "goldfish",
    "goose",
    "gorilla",
    "goshawk",
    "grasshopper",
    "grouse",
    "guanaco",
    "gull",
    "hamster",
    "hare",
    "hawk",
    "hedgehog",
    "heron",
    "herring",
    "hippopotamus",
    "hornet",
    "horse",
    "human",
    "hummingbird",
    "hyena",
    "ibex",
    "ibis",
    "jackal",
    "jaguar",
    "jay",
    "jellyfish",
    "kangaroo",
    "kingfisher",
    "koala",
    "kookabura",
    "kouprey",
    "kudu",
    "lapwing",
    "lark",
    "lemur",
    "leopard",
    "lion",
    "llama",
    "lobster",
    "locust",
    "loris",
    "louse",
    "lyrebird",
    "magpie",
    "mallard",
    "manatee",
    "mandrill",
    "mantis",
    "marten",
    "meerkat",
    "mink",
    "mole",
    "mongoose",
    "monkey",
    "moose",
    "mosquito",
    "mouse",
    "mule",
    "narwhal",
    "newt",
    "nightingale",
    "octopus",
    "okapi",
    "opossum",
    "oryx",
    "ostrich",
    "otter",
    "owl",
    "oyster",
    "panther",
    "parrot",
    "partridge",
    "peafowl",
    "pelican",
    "penguin",
    "pheasant",
    "pig",
    "pigeon",
    "pony",
    "porcupine",
    "porpoise",
    "quail",
    "quelea",
    "quetzal",
    "rabbit",
    "raccoon",
    "rail",
    "ram",
    "rat",
    "raven",
    "red deer",
    "red panda",
    "reindeer",
    "rhinoceros",
    "rook",
    "salamander",
    "salmon",
    "sand dollar",
    "sandpiper",
    "sardine",
    "scorpion",
    "seahorse",
    "seal",
    "shark",
    "sheep",
    "shrew",
    "skunk",
    "snail",
    "snake",
    "sparrow",
    "spider",
    "spoonbill",
    "squid",
    "squirrel",
    "starling",
    "stingray",
    "stinkbug",
    "stork",
    "swallow",
    "swan",
    "tapir",
    "tarsier",
    "termite",
    "tiger",
    "toad",
    "trout",
    "turkey",
    "turtle",
    "viper",
    "vulture",
    "wallaby",
    "walrus",
    "wasp",
    "weasel",
    "whale",
    "wildcat",
    "wolf",
    "wolverine",
    "wombat",
    "woodcock",
    "woodpecker",
    "worm",
    "wren",
    "yak",
    "zebra"
]

#From https://gist.github.com/chrishorton/8510732aa9a80a03c829b09f12e20d9c
STICKMAN = ['''
  +---+
      |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


word = random.choice(WORDS)

left_letters = letters
i_letter = ""
guessed_letters = []
wasted_letters = []
lives = 7
cword = ""

while lives > 0:
    cls()
    cword = ""
    for i in word:
        if i in guessed_letters: cword += i
        else: cword += "-"
    if cword == word: break
    if lives == 0: break
    print(STICKMAN[(lives-7) * -1])
    
    print(f"Word: {cword}")
   
    for i in wasted_letters:
        print(i, end=" ")
    print()
   
    #print(f"{lives}/7 attempts left")
    print("Type a letter:")
    i_letter = input("> ")
   
    if type(i_letter) != str:
        cls()
        print("Invalid input, you need to type one lowercase letter")
        input("Press ENTER to continue")
        continue
   
    if not i_letter in letters:
        cls()
        print("Your letter is not in the list of letters, Please use lowercase")
        input("Press ENTER to continue")
        continue
   
    if len(i_letter) > 1:
        cls()
        print("You can only guess one letter at a time")
        input("Press ENTER to continue")
        continue
   
    if i_letter in guessed_letters or i_letter in wasted_letters:
        cls()
        print("You already guessed this letter, try another!")
        input("Press ENTER to continue")
        continue
   
    if i_letter in word:
        guessed_letters.append(i_letter)
    else:
        lives -= 1
        wasted_letters.append(i_letter)
       
cls()
if lives > 0:
    print(f"The stickman survived, the word was '{word}'!")
else:
    print(STICKMAN[7])
    print(f"The stickman got hanged, the word was '{word}'")