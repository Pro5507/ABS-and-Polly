class India():
    def capital(self):
        print("Delhi is the capital of India")
    def language(self):
        print("Hindi is widly used language in India")
    def type(self):
        print("India is a developing country.")
class USA():
    def capital(self):
        print("Washington, D.C. is the capital of USA")
    def language(self):
        print("Englis is used in USA")
    def type(self):
        print("USA is a developed country.")
objIND= India()
objUSA= USA()
for country in (objIND,objUSA):
    country.capital()
    country.language()
    country.type()