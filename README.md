clear
======

A cross-platform Python module that provides a clear() function which clears the terminal. That's all.

To install with pip, run:

    pip install clear

You can then clear the screen by running:

    from clear import clear
    clear()

This function runs the one-liner: `os.system('cls' if os.name == 'nt' else 'clear')`

This module exists as a simpler alternative to defining this function on your own.

Special thanks to David George for allowing me to use the Clear name on PyPI. The original Clear module ("Command-Line Extract And Rename utility. This provides a media library manager that allows extraction and renaming of media files.") can still be found in the previous releases of this project on PyPI.
