class ineuron:

    def student(self):
        print("print the details of all the students")

    def achievers(self):
        print("print the list of the all achievers")

    def hall_of_fame(self):
        print("print everyone from hall of fame")

class ineuron_vision(ineuron):
    def student(self):     # method over riding
        print("These are the filter students list")

iv = ineuron_vision()
iv.student()