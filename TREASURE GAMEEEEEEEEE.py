treasure_x = 1
treasure_y = 0
Kristina = 0
Cassandra = 0
game_running = True


print(f"Find the treasure at ({treasure_x}, {treasure_y})!")

while game_running:
    move = input("Enter move (w/s/a/d) or (q) to quit: ")

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

    print(f"player at {Kristina, Cassandra}")

    if Kristina == treasure_x and Cassandra == treasure_y:
        break

print(f"Player position: ({Kristina}, {Cassandra})")
