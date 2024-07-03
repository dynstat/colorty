# Example usage of the library
from colorty import Clt
from colorty import set_color, reset_color


set_color('red')  # Set text color to red
print("This text is red")
set_color('31')  # Set text color to red
print("This text is still red")
set_color('green')  # Set text color to green
print("This text is green")
set_color(32)  # Set text color to green
print("This text is still green")
reset_color()    # Reset text color to default
print("This text is default color")
# format partial string with color
print(f"This is {Clt.RED}partial red{Clt.RESET} and {Clt.BLUE}partial blue{Clt.RESET} text.")