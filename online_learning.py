class User:
    def login(self):
        print("User is now logged in.")


class Student(User):
    def watch_course(self):
        print("Now watching course.")


class Instructor(User):
    def upload_course(self):
        print("Now uploading courese.")


class TeachingAssistant(Student, Instructor):
    def display_details(self):
        self.login()
        self.watch_course()
        self.upload_course()


TeachingAssistant = TeachingAssistant()
TeachingAssistant.display_details()
