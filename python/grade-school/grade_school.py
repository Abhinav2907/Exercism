from collections import defaultdict
class School:
    def __init__(self):
        self.grades = defaultdict(list)

    def add_student(self, name, grade):
        self.grades[grade].append(name)

    def roster(self):
        ans = []
        for _, st in sorted(self.grades.items()):
            ans.extend(sorted(st))
        return ans

    def grade(self, grade_number):
        return sorted(self.grades[grade_number])