class Student:

    def __init__(self, name, cohort):
        self.name = name
        self.cohort = cohort
        # self.fav_lang = fav_lang
        # self.talk = talk

    current_students = {}

    def student_has_name(self, student_name, student_cohort):
        self.current_students.append(student_name, student_cohort)

    # def student_can_talk(self, talk):
    #     talk == "I can talk"
    #     if self.name:
    #         return talk
    def talk(self):

        return "I can talk!"

    def say_favourite_language(self, lang):
        # return "I love " + lang
        return f"I love {lang}"
        # both options work - second can be easier for a long sentence

    


