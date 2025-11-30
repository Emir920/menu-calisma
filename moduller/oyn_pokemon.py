
import random
import time

class Pokemon:
    def __init__(self, name, hp, attack, defense, speed, moves):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.moves = moves
        self.level = 1

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.hp = 0

    def is_alive(self):
        return self.hp > 0

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp:
            self.hp = self.max_hp

class Player:
    def __init__(self, name):
        self.name = name
        self.pokemon = []
        self.items = {"Pokeball": 5, "Potion": 3}

    def add_pokemon(self, pokemon):
        self.pokemon.append(pokemon)

    def has_pokemon(self):
        return len(self.pokemon) > 0

def create_wild_pokemon():
    pokemon_list = [
        Pokemon("Pikachu", 35, 55, 40, 90, ["Thunder Shock", "Quick Attack"]),
        Pokemon("Charmander", 39, 52, 43, 65, ["Ember", "Scratch"]),
        Pokemon("Squirtle", 44, 48, 65, 43, ["Water Gun", "Tackle"]),
        Pokemon("Bulbasaur", 45, 49, 49, 45, ["Vine Whip", "Tackle"]),
        Pokemon("Eevee", 55, 55, 50, 55, ["Tackle", "Sand Attack"])
    ]
    return random.choice(pokemon_list)

def battle(player, wild_pokemon):
    print(f"\nA wild {wild_pokemon.name} appeared!")
    time.sleep(1)

    player_pokemon = player.pokemon[0]  # For simplicity, use first Pokemon

    while player_pokemon.is_alive() and wild_pokemon.is_alive():
        print(f"\n{player_pokemon.name} HP: {player_pokemon.hp}/{player_pokemon.max_hp}")
        print(f"Wild {wild_pokemon.name} HP: {wild_pokemon.hp}/{wild_pokemon.max_hp}")

        print("\nWhat will you do?")
        print("1. Fight")
        print("2. Use Item")
        print("3. Run")

        choice = input("Choose: ")

        if choice == "1":
            # Player attacks
            move = random.choice(player_pokemon.moves)
            damage = random.randint(5, 15)
            wild_pokemon.take_damage(damage)
            print(f"{player_pokemon.name} used {move}! Dealt {damage} damage.")

            if wild_pokemon.is_alive():
                # Wild Pokemon attacks
                wild_move = random.choice(wild_pokemon.moves)
                damage = random.randint(3, 12)
                player_pokemon.take_damage(damage)
                print(f"Wild {wild_pokemon.name} used {wild_move}! Dealt {damage} damage.")

        elif choice == "2":
            if player.items["Potion"] > 0:
                player_pokemon.heal(20)
                player.items["Potion"] -= 1
                print(f"{player_pokemon.name} was healed!")
            else:
                print("No potions left!")

        elif choice == "3":
            if random.random() < 0.5:
                print("Got away safely!")
                return
            else:
                print("Couldn't escape!")

        else:
            print("Invalid choice!")

        time.sleep(1)

    if player_pokemon.is_alive():
        print(f"\nYou defeated the wild {wild_pokemon.name}!")
        # Chance to catch
        print("Throw a Pokeball?")
        if input("y/n: ").lower() == "y" and player.items["Pokeball"] > 0:
            if random.random() < 0.5:
                player.add_pokemon(wild_pokemon)
                player.items["Pokeball"] -= 1
                print(f"Gotcha! {wild_pokemon.name} was caught!")
            else:
                print("Oh no! The Pokemon broke free!")
        else:
            print("You chose not to catch it.")
    else:
        print(f"\n{player_pokemon.name} fainted!")
        # In a full game, you'd handle this better

def explore(player):
    print("\nExploring...")
    time.sleep(1)

    if random.random() < 0.3:  # 30% chance of encounter
        wild_pokemon = create_wild_pokemon()
        battle(player, wild_pokemon)
    else:
        print("Nothing happened.")

def main():
    print("Welcome to Pokemon Text Adventure!")
    player_name = input("Enter your name: ")
    player = Player(player_name)

    # Give starter Pokemon
    print("\nChoose your starter Pokemon:")
    print("1. Pikachu")
    print("2. Charmander")
    print("3. Squirtle")
    print("4. Bulbasaur")

    choice = input("Choose: ")
    starters = {
        "1": Pokemon("Pikachu", 35, 55, 40, 90, ["Thunder Shock", "Quick Attack"]),
        "2": Pokemon("Charmander", 39, 52, 43, 65, ["Ember", "Scratch"]),
        "3": Pokemon("Squirtle", 44, 48, 65, 43, ["Water Gun", "Tackle"]),
        "4": Pokemon("Bulbasaur", 45, 49, 49, 45, ["Vine Whip", "Tackle"])
    }

    if choice in starters:
        player.add_pokemon(starters[choice])
        print(f"You chose {starters[choice].name}!")
    else:
        player.add_pokemon(starters["1"])
        print("Invalid choice. You got Pikachu!")

    while True:
        print(f"\n{player.name}'s Pokemon:")
        for i, p in enumerate(player.pokemon):
            print(f"{i+1}. {p.name} (HP: {p.hp}/{p.max_hp})")

        print("\nWhat do you want to do?")
        print("1. Explore")
        print("2. Check Items")
        print("3. Quit")

        choice = input("Choose: ")

        if choice == "1":
            explore(player)
        elif choice == "2":
            print("Items:")
            for item, count in player.items.items():
                print(f"{item}: {count}")
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
