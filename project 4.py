#MCS 260 Project 4 by Veronica Kalicki
class Movie:
    def __init__(self, name):
        self.name = name
        self.pop = 0


class Customer:
    def __init__(self, username):
        m_hist = []
        self.username = username
        self.m_hist = m_hist

    def Watch(self, movie):
        self.m_hist.append(Movie)
        Movie.pop += 1
        return 0

    def Rec(self,avail):
        avail = []
        self.avail = [x for x in avail if x.name != m.name for m in m_hist]
        self.avail.sort(key=lambda x: x.pop, reverse=True)
        return avail[0]


class MovieList:
    def __init__(self):
        m_list = []
        self.m_list = m_list

    def ShowList(self):
        print(self.m_list)

    def Add(self,name):
        self.name = name
        self.m_list.append(name)
        self.name = Movie('name')

    def FindByName(self,name):
        self.name = name
        if name in self.m_list:
            return name
        else:
            return 0


class CustomerList:
    def __init__(self):
        c_list = []
        self.c_list = c_list

    def ShowList(self):
        print(self.c_list)

    def Add(self,username):
        self.name = username
        self.c_list.append(username)
        self.username = Customer('username')

    def FindByName(self,username):
        self.name = username
        if username in self.c_list:
            return username
        else:
            return 0

if __name__ == '__main__':
    cust_list = CustomerList()
    movie_list = MovieList()

    while True:
        print("|||||||||||||||||||||||||||||||")
        print("Welcome to .NETflix")
        print("Please choose a number below: ")
        print("1) Create a new customer account")
        print("2) Login to as an existing customer")
        print("3) Login as an administrator")
        print("4) Quit")
        choice_1 = input("Choice: ")
        if choice_1 == '1':
            while True:
                username = input("Type in the username you'd like to use: ")
                cust = cust_list.FindByName(username)
                if cust == 0:
                    cust_list.Add(username)
                    cust = cust_list.FindByName(username)
                    print("Account created successfully!  Logging in...")
                    break
                print("That username is taken...")
        if choice_1 == '2':
            while True:
                username = input("Type in your username: ")
                cust = cust_list.FindByName(username)
                if cust != 0:
                    break
                print("That username is not on file...")
        if choice_1 == '1' or choice_1 == '2':
            while True:
                print("******************************")
                print("Hello ", username, "!")
                print("Please choose a number below: ")
                print("1) Show the list of available movies")
                print("2) Watch a movie")
                print("3) Request a recommendation")
                print("4) Logout")
                choice_2 = input("Choice: ")
                if choice_2 == '1':
                    movie_list.ShowList()
                if choice_2 == '2':
                    print("Please input the name of the movie to be watched")
                    choice_3 = input("Name: ")
                    movie = movie_list.FindByName(choice_3)
                    if movie != 0:
                        Customer.Watch(movie)
                        print("Watching movie........done!")
                    else:
                        print("That movie is not on file...")
                if choice_2 == '3':
                    cust.Rec(movie_list.m_list)
                if choice_2 == '4':
                    break

        if choice_1 == '3':
            while True:
                print("-------------------------------")
                print("Hello administrator")
                print("Please choose a number below: ")
                print("1) Show the list of available movies")
                print("2) Add new movies to the list")
                print("3) Show the list of customers")
                print("4) Logout")
                choice_2 = input("Choice: ")
                if choice_2 == '1':
                    movie_list.ShowList()
                if choice_2 == '2':
                    print("Please input the names of the movies to be added (or leave blank to quit):")
                    while True:
                        choice_3 = input("Name: ")
                        if choice_3 == '':
                            break
                        movie_list.Add(choice_3)
                if choice_2 == '3':
                    cust_list.ShowList()
                if choice_2 == '4':
                    break
        if choice_1 == '4':
            break