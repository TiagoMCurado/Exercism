"""Exercise grade-school from exercism.
https://exercism.org/tracks/python/exercises/grade-school"""


class School:
    """Based on the names of the students and the grade level they are in,
    the class creates a roster for the school.
    Grades should be sorted by 1, 2, 3, etc., and students within a grade
    should be sorted alphabetically by name.
    Note that all of our students have only have one name and each student can only
    be added to a grade or roster once."""

    def __init__(self):
        """Method, which shows us an empty list of students and an additional empty list.
        Also show us a dictionary (self.grade_list) where the keys are
        the names of the students and the values correspond to their grades.
        """

        self.student_list = []
        self.adding_list = []
        self.grade_list = {}

    def add_student(self, name, grade):
        """Method that checks whether a name already exists in the student_list.
        If not, add it to the student_list, where a boolean True is also added
        to the adding_list and the name and the grade to the dict grade_list.
        If not, no name and grade will be added to the student_list and grade_list,
        but only a boolean False is added to the adding_list.

        Parameters
        --------
        name: string
        grade: int
        """

        if name not in self.student_list:
            self.student_list.append(name)
            self.adding_list.append(True)
            self.grade_list[name] = grade
        else:
            self.adding_list.append(False)

    def roster(self):
        """Method that provides us with the list of students, sorted by name and grade.

        Returns:
        list(dict_order.keys()): list[str]
            List of student names ordered by name and grade"""

        dict_order = dict(
            sorted(self.grade_list.items(), key=lambda item: (item[1], item[0]))
        )

        return list(dict_order.keys())

    def grade(self, grade_number: int):
        """Method that provides us the list of students in a selected grade, sorted by name.

        Parameters
        --------
        grade_number: int

        Returns:
        temporary_list: list[str]
        """
        temporary_list = []  # creation of a temporary list that will give us the list
        # of students in a selected grade

        for key, value in self.grade_list.items():
            if value == grade_number:
                temporary_list.append(key)

        temporary_list.sort()

        return temporary_list

    def added(self):
        """Method that returns a boolean list of whether or not the student
        has been added to the student_list.

        Returns:
        self.adding_list: list[bool]
        """
        return self.adding_list

"""class School:
    
    def __init__(self):

        self.student_list = []
        self.adding_list = []
        self.grade_list = {}

    def add_student(self, name, grade):
        
        if name not in self.student_list:
            self.student_list.append(name)
            self.adding_list.append(True)
            self.grade_list[name] = grade
        else:
            self.adding_list.append(False)

    def roster(self):
        
        dict_order = dict(sorted(self.grade_list.items(), key=lambda item: (item[1],item[0])))

        return list(dict_order.keys())

    def grade(self, grade_number):

        def my_filtering_function(pair):
            wanted_value = grade_number
            key, value = pair
            if value == wanted_value:
                return True  #  keep pair in the filtered dictionary
            else:
                return False  # filter pairs out of the dictionary'''
        
        filtered_grades = dict(filter(my_filtering_function,self.grade_list.items()))

        filtered_grades = dict(sorted(filtered_grades.items(), key=lambda item: (item,item[0])))

        return list(filtered_grades.keys())

        return temporary_list

    def added(self):

        return self.adding_list 
"""
