# Example usage of the library
from colort import Clt
from colort import set_color, reset_color


set_color('31')  # Set text color to red
set_color('31')  # Set text color to red
print("This text is red")
print("This text is still red")
set_color('32')  # Set text color to green
print("This text is green")
reset_color()    # Reset text color to default
print("This text is default color")
# format partial string with color
print(f"This is {Clt.RED}partial red{Clt.RESET} and {Clt.BLUE}partial blue{Clt.RESET} text.")