from game import constants
from game.actor import Actor
from game.point import Point

class Snake:
    """A limbless reptile. The responsibility of Snake is keep track of its segments. It contains methods for moving and growing among others.

    Stereotype:
        Structurer, Information Holder

    Attributes:
        _body (List): The snake's body (a list of Actor instances)
    """
    def __init__(self):
        """The class constructor.
        
        Args:
            self (Snake): An instance of snake.
        """
        super().__init__()
        self._collidable_index = constants.DEFAULT_SQUARE_LENGTH + 1
        self._segments = []
        self._prepare_body()
    
    def get_all(self):
        """Gets all the snake's segments.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's segments.
        """
        return self._segments

    def get_body(self):
        """Gets the snake's body.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            list: The snake's body.
        """
        return self._segments[1:]

    def get_collidable_segments(self):
        """
        Get's the part of the snake that can be collided with.
        """
        return self._segments[self._collidable_index:]

    def get_head(self):
        """Gets the snake's head.
        
        Args:
            self (Snake): An instance of snake.

        Returns:
            Actor: The snake's head.
        """
        return self._segments[0]

    def grow_tail(self, amount):
        """
        Grows the tail by the amount specified.
        """
        grow_amount = amount * 10

        for i in range(grow_amount):
            self.grow_tail_single()

    def grow_tail_single(self):
        """Grows the snake's tail by one segment.
        
        Args:
            self (Snake): An instance of snake.
        """
        tail = self._segments[-1]
        offset = tail.get_velocity().reverse()
        position = tail.get_position().add(offset)
        velocity = tail.get_velocity()
        self._add_segment(position, velocity)
    
    def turn_head(self, direction):
        """Moves the head in the given direction.

        Args:
            self (Snake): An instance of snake.
            direction (Point): The direction to move.
        """
        head = self.get_head()
        head.set_velocity(direction)


    def move(self):
        """Moves the each segment of the snake.

        Args:
            self (Snake): An instance of snake.
        """
        # First move them all forward
        for segment in self._segments:
            segment.move_next()

        # Now update the velocity of each segment to be the one before it
        count = len(self._segments) - 1
        for n in range(count, 0, -1):
            current_segment = self._segments[n]
            segment_before = self._segments[n - 1]

            velocity = segment_before.get_velocity()
            current_segment.set_velocity(velocity)

    def _add_segment(self, position, velocity):
        """Adds a new segment to the snake using the given text, position and velocity.

        Args:
            self (Snake): An instance of snake.
            text (string): The segment's text.
            position (Point): The segment's position.
            velocity (Point): The segment's velocity.
        """
        segment = Actor()
        segment.set_position(position)
        segment.set_velocity(velocity)
        segment.set_width(constants.DEFAULT_SQUARE_LENGTH)
        segment.set_height(constants.DEFAULT_SQUARE_LENGTH)
        self._segments.append(segment)

    def _prepare_body(self):
        """Prepares the snake body by adding segments.
        
        Args:
            self (Snake): an instance of Snake.
        """
        x = int(constants.MAX_X / 2)
        y = int(constants.MAX_Y / 2)
        for n in range(constants.SNAKE_LENGTH):
            position = Point(x - n, y)
            velocity = Point(1, 0)
            self._add_segment(position, velocity)