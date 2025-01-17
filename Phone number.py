"""Solution to the phone number exercise.
https://exercism.org/tracks/python/exercises/phone-number"""

import re

class PhoneNumber:
    def __init__(self, number): 
        """Phone number exercise. 
        Clean up and formatting valid phone numbers, for use in the system.

         Parameters
         -------- 
         number : str
            Differently formatted telephone numbers """

        if re.search(r'[@:!]+', number):
            raise ValueError("punctuations not permitted")
        if re.search(r'[a-zA-Z]+', number):
            raise ValueError("letters not permitted")
        number = re.sub(r'\D', "", number)
        if len(number) < 10:
            raise ValueError("must not be fewer than 10 digits")

        elif len(number) == 10:
            if int(number[0]) == 0:
                raise ValueError("area code cannot start with zero")
            if int(number[0]) == 1:
                raise ValueError("area code cannot start with one")
            if int(number[3]) == 0:
                raise ValueError("exchange code cannot start with zero")
            if int(number[3]) == 1:
                raise ValueError("exchange code cannot start with one")

        elif len(number) == 11:
            if int(number[0]) != 1:
                raise ValueError("11 digits must start with 1")
            if int(number[1]) == 1:
                raise ValueError("area code cannot start with one")
            if int(number[1]) == 0:
                raise ValueError("area code cannot start with zero")
            if int(number[4]) == 1:
                raise ValueError("exchange code cannot start with one")
            if int(number[4]) == 0:
                raise ValueError("exchange code cannot start with zero")

        else:
            raise ValueError("must not be greater than 11 digits")

        if len(number) == 10:
            self.number = number
        else:
            self.number = number[1:]
        
        self.area_code = self.number[:3]
                  
    def pretty(self):
        """Output of the phone number in a specific format. Phone number format example ("(223)-456-7890")

         Return: str
          String formatted phone number"""
        return f"({self.area_code})-{self.number[3:6]}-{self.number[6:]}"