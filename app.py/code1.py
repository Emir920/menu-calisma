from panda3d.core import *
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
import random
import sys

# Pokemon classes (copied from oyn_pokemon.py to avoid import issues)
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

class Pokemon3DGame(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        # Set up the camera
        self.disableMouse()
        self.camera.setPos(0, -10, 5)
        self.camera.lookAt(0, 0, 0)

        # Create player
        self.player = Player("Trainer")
        self.player.add_pokemon(Pokemon("Pikachu", 35, 55, 40, 90, ["Thunder Shock", "Quick Attack"]))

        # Create world
        self.create_world()

        # Set up controls
        self.accept('w', self.move_forward)
        self.accept('s', self.move_backward)
        self.accept('a', self.move_left)
        self.accept('d', self.move_right)

        # Battle variables
        self.in_battle = False
        self.wild_pokemon = None

        # Add task for movement and encounters
        self.taskMgr.add(self.update_task, 'update')

        # UI elements
        self.create_ui()

    def create_world(self):
        # Create a simple ground plane
        self.ground = self.loader.loadModel("models/environment")
        self.ground.setScale(10, 10, 1)
        self.ground.setPos(0, 0, 0)
        self.ground.reparentTo(self.render)

        # Create some trees or obstacles (simple cubes for now)
        for i in range(10):
            tree = self.loader.loadModel("models/box")
            tree.setScale(0.5, 0.5, 2)
            tree.setPos(random.randint(-20, 20), random.randint(-20, 20), 1)
            tree.reparentTo(self.render)

    def create_ui(self):
        # Player info display
        self.player_text = OnscreenText(text="", pos=(-1.3, 0.9), scale=0.05, fg=(1,1,1,1))

        # Battle UI (hidden initially)
        self.battle_frame = DirectFrame(frameColor=(0,0,0,0.8), frameSize=(-1,1,-1,1))
        self.battle_frame.hide()

        self.battle_text = OnscreenText(text="", pos=(0, 0.5), scale=0.08, fg=(1,1,1,1), parent=self.battle_frame)

        self.fight_button = DirectButton(text="Fight", scale=0.1, pos=(-0.5, 0, 0), parent=self.battle_frame,
                                         command=self.fight_action)
        self.catch_button = DirectButton(text="Catch", scale=0.1, pos=(0.5, 0, 0), parent=self.battle_frame,
                                         command=self.catch_action)
        self.run_button = DirectButton(text="Run", scale=0.1, pos=(0, 0, -0.5), parent=self.battle_frame,
                                       command=self.run_action)

    def update_task(self, task):
        dt = globalClock.getDt()

        # Update player info
        if self.player.pokemon:
            pokemon = self.player.pokemon[0]
            self.player_text.setText(f"{self.player.name}\n{pokemon.name} HP: {pokemon.hp}/{pokemon.max_hp}")

        # Random encounter
        if not self.in_battle and random.random() < 0.005:  # Low chance per frame
            self.start_battle()

        return Task.cont

    def move_forward(self):
        self.camera.setY(self.camera.getY() + 1)

    def move_backward(self):
        self.camera.setY(self.camera.getY() - 1)

    def move_left(self):
        self.camera.setX(self.camera.getX() - 1)

    def move_right(self):
        self.camera.setX(self.camera.getX() + 1)

    def start_battle(self):
        self.in_battle = True
        self.wild_pokemon = create_wild_pokemon()

        # Create a simple 3D representation of the wild Pokemon (a sphere for now)
        self.pokemon_model = self.loader.loadModel("models/sphere")
        self.pokemon_model.setScale(0.5)
        self.pokemon_model.setPos(0, 5, 1)
        self.pokemon_model.reparentTo(self.render)

        # Show battle UI
        self.battle_frame.show()
        self.battle_text.setText(f"A wild {self.wild_pokemon.name} appeared!\nHP: {self.wild_pokemon.hp}")

    def fight_action(self):
        if self.player.pokemon and self.wild_pokemon:
            player_pokemon = self.player.pokemon[0]
            move = random.choice(player_pokemon.moves)
            damage = random.randint(5, 15)
            self.wild_pokemon.take_damage(damage)

            self.battle_text.setText(f"{player_pokemon.name} used {move}!\nDealt {damage} damage.\n"
                                     f"Wild {self.wild_pokemon.name} HP: {self.wild_pokemon.hp}")

            if not self.wild_pokemon.is_alive():
                self.end_battle(True)
            else:
                # Wild Pokemon attacks back
                wild_move = random.choice(self.wild_pokemon.moves)
                damage = random.randint(3, 12)
                player_pokemon.take_damage(damage)
                self.battle_text.setText(self.battle_text.getText() + f"\nWild {self.wild_pokemon.name} used {wild_move}!\n"
                                         f"Dealt {damage} damage.\n{player_pokemon.name} HP: {player_pokemon.hp}")

                if not player_pokemon.is_alive():
                    self.end_battle(False)

    def catch_action(self):
        if self.player.items["Pokeball"] > 0:
            if random.random() < 0.5:
                self.player.add_pokemon(self.wild_pokemon)
                self.player.items["Pokeball"] -= 1
                self.battle_text.setText(f"Gotcha! {self.wild_pokemon.name} was caught!")
                self.end_battle(True)
            else:
                self.battle_text.setText("Oh no! The Pokemon broke free!")
        else:
            self.battle_text.setText("No Pokeballs left!")

    def run_action(self):
        if random.random() < 0.5:
            self.battle_text.setText("Got away safely!")
            self.end_battle(False)
        else:
            self.battle_text.setText("Couldn't escape!")

    def end_battle(self, player_won):
        self.in_battle = False
        self.battle_frame.hide()
        if hasattr(self, 'pokemon_model'):
            self.pokemon_model.removeNode()
        self.wild_pokemon = None

    def quit_game(self):
        self.userExit()

if __name__ == "__main__":
    game = Pokemon3DGame()
    game.run()
