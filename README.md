# Colort

Colort is a Python library for handling colored text in various terminal environments including Windows CMD, PowerShell, and Unix-like terminals on Ubuntu and macOS.

## Installation

Install Colort using pip:



```bash
pip install colort
```
## Usage

Basic example:

```python
from colort import set_color, reset_color

set_color('31')  # Set text color to red
print("This text is red")
print("This text is still red")
set_color('32')  # Set text color to green
print("This text is green")
reset_color()    # Reset text color to default
print("This text is default color")
```

Using the `Clt` class:

```python
from colort import Clt

# format partial string with color
print(f"This is {Clt.RED}partial red{Clt.RESET} and {Clt.BLUE}partial blue{Clt.RESET} text.")
```

## API Reference

- `set_color(color)`: Sets the terminal text color.
- `reset_color()`: Resets the terminal text color to default.
- `Clt`: Class with predefined ANSI color codes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.


**Acknowledgments**: inspired from the Colorama library. 