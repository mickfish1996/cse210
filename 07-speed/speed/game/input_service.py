import sys
import raylibpy

class InputService:
    """Detects player input. The responsibility of the class of objects is to detect player keypresses and translate them into a point representing a direction (or velocity).

    Stereotype: 
        Service Provider

    Attributes:
        _screen (Screen): An Asciimatics screen.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (InputService): An instance of InputService.
        """
        pass
        
    def get_letter(self):
        """Gets the letter that was typed. If the enter key was pressed returns an asterisk.

        Args:
            self (InputService): An instance of InputService.

        Returns:
            string: The letter that was typed.
        """
        result = ""
        event = raylibpy.get_key_pressed()
        assert type(event) is int
        
        if not event is None:
            if event == 27 or event == 96:
                sys.exit()
            elif event == 92 or event == 10: 
                result = "*"
            elif event >= 97 and event <= 122: 
                result = chr(event)
                assert type(result) is str
        return result