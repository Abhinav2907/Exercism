class Garden:
    STUDENTS = ['Alice','Bob','Charlie','David','Eve','Fred','Ginny','Harriet','Ileana','Joseph','Kincaid','Larry']
    FLOWERS = {'C': 'Clover', 'R': 'Radishes','G': 'Grass', 'V': 'Violets'}
    def __init__(self, diagram, students=STUDENTS):
        diagram = diagram.split()
        flowers = zip(*[iter(diagram[0])]*2 + [iter(diagram[1])]*2)
        self.pots = dict(zip(sorted(students), flowers))

    def plants(self, x):
		return map(self.FLOWERS.get, self.pots[x])
