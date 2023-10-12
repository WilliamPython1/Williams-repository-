import random

class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.gold = 100
        self.inventory = {}

    def display_stats(self):
        print(f"Name: {self.name}")
        print(f"Class: {self.player_class}")
        print(f"Health: {self.health}")
        print(f"Attack: {self.attack}")
        print(f"Defense: {self.defense}")
        print(f"Gold: {self.gold}")
        print("Inventory:")
        for item, quantity in self.inventory.items():
            print(f"{item}: {quantity}")

class Shop:
    def __init__(self):
        self.items = {
            "Health Potion": 10,
            "Sword": 20,
            "Armor": 15,
        }

    def buy(self, item, player):
        if item in self.items and player.gold >= self.items[item]:
            player.gold -= self.items[item]
            if item in player.inventory:
                player.inventory[item] += 1
            else:
                player.inventory[item] = 1
            print(f"You bought a {item}.")

    def sell(self, item, player):
        if item in player.inventory:
            player.gold += self.items[item]
            player.inventory[item] -= 1
            if player.inventory[item] == 0:
                del player.inventory[item]
            print(f"You sold a {item}.")

class Enemy:
    def __init__(self, name, health, attack, defense):
        self.name = name
        self.health = health
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        self.health -= max(0, damage - self.defense)

def battle(player, enemy):
    while player.health > 0 and enemy.health > 0:
        player_damage = random.randint(1, player.attack)
        enemy_damage = random.randint(1, enemy.attack)

        print(f"{player.name} attacks {enemy.name} for {player_damage} damage.")
        enemy.take_damage(player_damage)
        print(f"{enemy.name} attacks {player.name} for {enemy_damage} damage.")
        player.health -= max(0, enemy_damage - player.defense)

    if player.health <= 0:
        print("You have been defeated.")
    else:
        print(f"You defeated {enemy.name}.")

def main():
    player_name = input("Enter your character's name: ")
    player_class = input("Choose your class (Warrior, Mage, Rogue): ")
    player = Player(player_name, player_class)
    shop = Shop()

    while player.health > 0:
        print("\n===== Main Menu =====")
        print("1. Display Stats")
        print("2. Visit Shop")
        print("3. Battle Enemy")
        print("4. Quit")
        choice = input("Enter your choice: ")

        if choice == "1":
            player.display_stats()
        elif choice == "2":
            print("\n===== Shop =====")
            print("Items for sale:")
            for item, price in shop.items.items():
                print(f"{item}: {price} gold")
            shop_choice = input("Enter item name to buy or 'exit' to leave the shop: ")
            if shop_choice == 'exit':
                continue
            shop.buy(shop_choice, player)
        elif choice == "3":
            enemy = Enemy("Goblin", 30, 8, 2)
            print(f"\nA wild {enemy.name} appears!")
            battle(player, enemy)
        elif choice == "4":
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
