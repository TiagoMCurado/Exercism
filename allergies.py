""" Exercise allergies from exercism.
https://exercism.org/tracks/python/exercises/allergies"""


class Allergies:
    """A class to determine allergies based on a given allergy score."""

    def __init__(self, score: int):
        """Initialize the allergies based on a binary score.

        Parameters
        --------
        score: int
        An integer representing the allergy score.
        """

        self.list_of_aliments = [
            "eggs",
            "peanuts",
            "shellfish",
            "strawberries",
            "tomatoes",
            "chocolate",
            "pollen",
            "cats",
        ]

        # Convert score to binary, remove '0b' prefix and reverse for easy index mapping
        self.score = str(bin(score))[2:][::-1]

    def allergic_to(self, item: str):
        """Check if a person is allergic to a specific item.

        Parameters
        --------
        item: str
        The food item to check.

        Returns:
        bool: True if the person is allergic to the item, False otherwise.
        """
        index = self.list_of_aliments.index(item)

        # If the index is out of range of the binary score representation, return False
        if index > (len(self.score) - 1):
            return False

        # Check if the binary digit at the given index is '1' (allergic)
        return self.score[index] == "1"

    @property
    def lst(self):
        """Return a list of all allergens the person is allergic to.

        Returns:
        list[str]
        A list of allergens the person is allergic to.
        """
        l = []
        for idx, i in enumerate(self.score):
            if idx > 7:  # Ensure we only consider the first 8 allergens
                break
            if i == "1":  # If binary digit is '1', add corresponding allergen
                l.append(self.list_of_aliments[idx])

        return l