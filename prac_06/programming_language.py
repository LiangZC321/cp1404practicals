#10:31 start(doing these at home before class since medical issue)
class ProgrammingLanguage:
    def __init__(self, name, typing, reflection, year):
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        return self.typing == "Dynamic"

    def __str__(self):
        reflection_status = "True" if self.reflection else "False"
        return f"{self.name}, {self.typing} Typing, Reflection={reflection_status}, First appeared in {self.year}"
