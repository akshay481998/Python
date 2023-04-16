class ineuron:

    def __init__(self):
        self.students1 = "data science"

    def students(self):
        print(self.students1)

i = ineuron()
i.students()
i.students1 = "Data Analytics"
i.students()


class ineuron1:

    def __init__(self):
        self.__students1 = "data science"

    def students(self):
        print(self.__students1)

    def students_change(self,new_values):
        self.__students1 = new_values

i1 = ineuron1()
i1.students()
i1.__students1 = "big data"
i1.students()
i1.students_change("Akshay")
i1.students()