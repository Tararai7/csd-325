# Student Name: Tara Rai
# Assignment: M1.3
# Description: 
#   A program that simulates the "bottles of beer on the wall" countdown.
#   Takes user input for starting number of bottles, counts down with correct
#   plural/singular phrasing, and ends with a reminder to buy more beer.

def countdown(bottles):
    """Count down from bottles to 0, printing lyrics with correct grammar."""
    while bottles > 0:
        if bottles > 1:
            print(f"{bottles} bottles of beer on the wall, {bottles} bottles of beer.")
            next_bottles = bottles - 1
            bottle_word = "bottle" if next_bottles == 1 else "bottles"
            print(f"Take one down and pass it around, {next_bottles} {bottle_word} of beer on the wall.\n")
        else:  # bottles == 1
            print("1 bottle of beer on the wall, 1 bottle of beer.")
            print("Take one down and pass it around, no more bottles of beer on the wall.\n")
        bottles -= 1

    print("No more bottles of beer on the wall, no more bottles of beer.")
    print("Go to the store and buy some more, 99 bottles of beer on the wall!")

# Main program
if __name__ == "__main__":
    try:
        bottles = int(input("How many bottles of beer on the wall? "))
        if bottles < 0:
            print("Please enter a non-negative number.")
        elif bottles == 0:
            print("No bottles? Go buy some first!")
        else:
            countdown(bottles)
    except ValueError:
        print("Please enter a valid whole number.")