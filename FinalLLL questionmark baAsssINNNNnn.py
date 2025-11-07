treasure_x = 15
treasure_y = 3
Kristina = 0
Cassandra = 0
game_running = True


print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
    move = input("Enter a move (w/s/a/d) or enter (q) to quit: ")

    if move == "w" or move == "W":
        Kristina += 1
    elif move == "s" or move == "S":
        Kristina -= 1
    elif move == "a" or move == "A":
        Cassandra -= 1
    elif move == "d" or move == "D":
        Cassandra += 1
    elif move == "q" or move == "Q":
        break
    else:
        print("Invalid move")

    if Kristina == treasure_x and Cassandra == treasure_y:
        break

    print(f"Player position: {Kristina, Cassandra}")

print(f"Player has found the treasyre!")
