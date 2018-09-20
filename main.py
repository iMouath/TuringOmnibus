# CSC 490 HW 3
# This program will generate a 10 by 10 wallpaper
#
# Muath Almubarrizi


# Declaring vars with default values

outputList = []  # list to hold colors in columns and rows

colors = 2  # wallpaper "colors" available options are 2 and 3

# corners for initial square
corna = 0
cornb = 0

side = 10  # length of square side


# this function will generate a wallpaper based on user input
def makeWallpaper(corna, cornb, side, colors):

    for i in range(1, 11):

        outputList.append([])  # add rows for each i in this case 10

        for j in range(1, 11):

            x = corna + (i * side / 10)
            y = cornb + (j * side / 10)
            c = int(x ** 2 + y ** 2)

            # 2 color wallpaper
            if (colors == 2):
                if (c % 2 == 0):
                    outputList[i - 1].append("X")
                else:
                    outputList[i - 1].append(" ")

            # 3 color wallpaper
            elif (colors == 3):
                if (c % 3 == 0):
                    outputList[i - 1].append("Y")
                elif (c % 2 == 0):
                    outputList[i - 1].append("X")
                else:
                    outputList[i - 1].append(" ")


# display the wallpaper by parsing our list and printing each row
def displayWallpaper():
    for l in outputList:
        buffer = ""
        for c in l:
            # build up a row in buffer until it reaches 10 columns
            buffer = buffer + c
            if len(buffer) == 10:
                print(buffer)


colors = int(input("Type 2 or 3 to pick the colors or 0 to quit, default is 2: "))

if (colors == 0):
    quit()

corna = int(input("Enter the coordinate for Corner A: "))
cornb = int(input("Enter the coordinate for Corner B: "))

side = int(input("Enter the side length: "))

makeWallpaper(corna, cornb, side, colors)
displayWallpaper()
quit()
