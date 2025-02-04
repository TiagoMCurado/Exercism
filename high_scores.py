"""Exercise high-scores from exercism.
https://exercism.org/tracks/python/exercises/high-scores/edit"""

import copy


class HighScores:
    """A class to manage and analyze a player's high scores."""

    def __init__(self, scores: list[int]):
        """Initialize the HighScores object with a list of scores.

        Parameters
        --------
        scores: list[int]
        A list of recorded scores.
        """
        self.scores = scores

    def latest(self):
        """Return the most recent score.

        Returns:
        int
        The last score in the list.
        """
        return self.scores[-1]

    def personal_best(self):
        """Return the highest score achieved.

        Returns:
        int
        The maximum value in the scores list.
        """
        return max(self.scores)

    def personal_top_three(self):
        """Return the top three highest scores in descending order.

        Returns:
        list[int]
        A list containing up to the top three highest scores.
        """
        list2 = copy.deepcopy(self.scores)  # Create a copy to avoid modifying the original list
        list2.sort(reverse=True)  # Sort in descending order
        return list2[:3]
