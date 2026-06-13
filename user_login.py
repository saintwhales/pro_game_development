class User:
    def login(self):
        print("User logged in.")


class PremiumUser(User):
    def access_premium(self):
        print("Accessing premium features.")


user = PremiumUser()
user.login()
user.access_premium()
