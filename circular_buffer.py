""" Exercise circular buffer from exercism.
https://exercism.org/tracks/python/exercises/circular-buffer"""


class BufferFullException(BufferError):
    """Exception raised when CircularBuffer is full.

    message: explanation of the error.
    """

    def __init__(self, message):
        # Called when an attempt is made to add data to a full buffer
        pass


class BufferEmptyException(BufferError):
    """Exception raised when CircularBuffer is empty.

    message: explanation of the error.
    """

    def __init__(self, message):
        # Called when an attempt is made to retrieve data from an empty buffer
        pass


class CircularBuffer:
    """A simple circular buffer implementation."""

    def __init__(self, capacity):
        """Initialize the circular buffer with a fixed capacity.

        Parameters:
        --------
        capacity: int
        Maximum size of the buffer.
        """

        self.capacity = capacity  # Maximum number of elements in the buffer.
        self.buffer = []  # Internal list for the buffer elements.

    def read(self):
        """Remove and return the oldest element from the buffer.

        Raises:
        BufferEmptyException: If the buffer is empty.

        Returns:
        Any
        The oldest data in the buffer.
        """

        if len(self.buffer) == 0:
            raise BufferEmptyException("Circular buffer is empty")

        return self.buffer.pop(0)

    def write(self, data: str):
        """Add a new element to the buffer if there is space.

        Parameters
        --------
        data: str
        The data to be added to the buffer.

        Raises:
        BufferFullException: If the buffer is full.
        """

        if len(self.buffer) == self.capacity:
            raise BufferFullException("Circular buffer is full")

        self.buffer.append(data)

    def overwrite(self, data: str):
        """Overwrite the oldest data if the buffer is full, otherwise add new data.

        Parameters
        --------
        data: str
        The data to be added to the buffer.
        """

        if len(self.buffer) == self.capacity:
            self.buffer.pop(0)

        self.buffer.append(data)

    def clear(self):
        """Remove all elements from the buffer, making it empty."""

        self.buffer = []
