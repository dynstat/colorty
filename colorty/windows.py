import ctypes
import sys


def handle_windows_terminal():
    """
    Handle specific settings for Windows CMD and PowerShell.
    This function enables ANSI escape sequence processing in Windows terminals.
    """
    # Check if the current platform is Windows
    if sys.platform.startswith("win"):
        try:
            # Load the Windows kernel32 library
            kernel32 = ctypes.windll.kernel32

            # Get the handle to the standard output device (console)
            # -11 is the constant for STD_OUTPUT_HANDLE
            handle = kernel32.GetStdHandle(-11)

            # Create a c_uint32 object to store the console mode
            mode = ctypes.c_uint32()

            # Get the current console mode and store it in the 'mode' object
            kernel32.GetConsoleMode(handle, ctypes.byref(mode))

            # Enable ENABLE_VIRTUAL_TERMINAL_PROCESSING (0x0004)
            # This flag allows the use of ANSI escape sequences
            mode.value |= 0x0004

            # Set the new console mode with ANSI escape sequence processing enabled
            kernel32.SetConsoleMode(handle, mode)

        except Exception as e:
            # If an error occurs during the process, print a warning message
            print(
                f"Warning: Unable to set Windows console mode. ANSI colors may not work correctly. Error: {e}",
                file=sys.stderr,
            )
            # The error message is directed to stderr for better error handling
