 # exercise -3
 # Treasure Map:
 row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ").split()
map[int(position[1])-1][int(position[0])-1] = "*"
print(f"{row1}\n{row2}\n{row3}")
