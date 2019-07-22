'''
Final project - Exploring a CSV file using csv module

In this project will build a CSV file  which contains some specifications about some movies such as: title, country, rating,
actor, director, duration, budget, etc
Will be extracted information in the form of lists depending on some applied conditions
The CSV file will be copied in the working directory of Pycharm before start writing the code
Will import csv module csv which will help to manipulate the CSV file
Will work in construction of methods with list comprehension

'''
import csv
class Media:
    '''
    Analysing of best market places and production studios
    '''

    def __init__(self, market_dupl, production_studio_dupl):
        '''
        Defining the constructor of class Media
        :param market_dupl: duplicates of movies market countries
        :param production_studio_dupl: duplicates of production movies studios
        '''
        self.market = market_dupl
        self.production_studio_dupl = production_studio_dupl

    def market_country(self):
        '''
        :return: prints a dictionary with frequency of duplicates of market movies countries(key : value)
        '''
        with open('project.csv', 'r') as f:
            csv_file = csv.reader(f, delimiter = ',')
            next(csv_file)
            self.market_dupl = {}
            for row in csv_file:
                market = row[1]
                if market in self.market_dupl.keys():
                    self.market_dupl[market] += 1
                else:
                    self.market_dupl[market] = 1
            print('The distribution of market countries duplicates is:',self.market_dupl)
            print('=====================================================================================================')

    def production_studio(self):
        '''
        :return: prints a dictionary with frequency of duplicates of production studios(key : value)
        '''
        with open('project.csv', 'r') as f:
            csv_file = csv.reader(f, delimiter = ',')
            next(csv_file)
            self.production_studio_dupl = {}
            for row in csv_file:
                production_studio = row[2]
                if production_studio in self.production_studio_dupl.keys():
                    self.production_studio_dupl[production_studio] += 1
                else:
                    self.production_studio_dupl[production_studio] = 1
            print('The distribution of production studios duplicates is:', self.production_studio_dupl)
            print('=====================================================================================================')

class Movie:
    '''
    Analysing the specific parameters of a movie
    '''
    def __init__(self,title, year, director, actor, genre, runtime, budget, language, rating):
       '''
       Defining the constructor of super-class Movie (parent class)
       :param title: the title of movie
       :param year: the year of movie release
       :param director: the director of movie
       :param actor: main role actor of movie
       :param genre: the genre of movie
       :param runtime: the duration of movie
       :param budget: the estimated budget of movie
       :param language: the main languafe of movie
       :param rating: IMDB rating of movie
       '''
       self.title = title
       self.year = year
       self.director = director
       self.actor = actor
       self.genre = genre
       self.runtime = runtime
       self.budget = budget
       self.language = language
       self.rating = rating

    def show_movie_title(self):
       '''
       :return: prints a list with the titles of movies with estimated budgets within in interval 100000000 and 250000000 USD
       '''
       with open('project.csv', 'r') as f:
            rows = list(csv.reader(f))[1:]
            self.title = [str(row[0]) for row in rows if (float(row[11]) >= 100000000.0) and (float(row[11]) <= 250000000.0)]
            print('The movies titles with estimated budget between 100mil and 250mil USD are:', self.title)
            print('=====================================================================================================')

    def show_movie_year(self):
        '''
        :return: prints a list with release year of movies which have as main role actor Al Pacino or which are directed
        by Bradley Cooper
        '''
        with open('project.csv', 'r') as f:
            rows = list(csv.reader(f))[1:]
            self.year = [int(row[4]) for row in rows if (str(row[9]) == 'Al Pacino') or (str(row[8]) == 'Bradley Cooper')]
            print('Production years of movies which have as main role actor A. Pacino or director as B. Cooper:', self.year)
            print('=====================================================================================================')

    def show_movie_director(self):
        '''
        :return: prints a list with directors names which direct movies with lower or highest rating
        '''
        with open('project.csv', 'r') as f:
            rows = list(csv.reader(f))[1:]
            r_lower = min([float(row[10]) for row in rows])
            r_higher = max([float(row[10]) for row in rows])
            self.director = [str(row[8]) for row in rows if (float(row[10]) == r_lower) or (float(row[10]) == r_higher)]
            print('The names of directors of movies which directed the lower or the higher rated movie:',self.director)
            print('=====================================================================================================')

    def show_movie_actor(self):
        '''
        :return: prints a list with actors names which act in shortest or the longest movie
        '''
        with open('project.csv', 'r') as f:
            rows = list(csv.reader(f))[1:]
            runtime_lower = min([int(row[7]) for row in rows])
            runtime_higher = max([int(row[7]) for row in rows])
            self.actor = [str(row[9]) for row in rows if (int(row[7]) == runtime_lower) or (int(row[7]) == runtime_higher)]
            print('The names of main role actors which act in the shortest or the longest movie as the duration:',self.actor)
            print('=====================================================================================================')

    def show_movie_genre(self):
        '''
        :return: prints a list with genres of movies produced in Romania or France
        '''
        with open('project.csv', 'r') as f:
            rows = list(csv.reader(f))[1:]
            self.genre = [str(row[6]) for row in rows if (str(row[1]) == 'Romania') or (str(row[1]) == 'France')]
            print('The genres of movies produced in Romania or France are:', self.genre)
            print('=====================================================================================================')

    def show_movie_runtime(self):
        '''
        :return: prints a list with durations of movies released in only odd year after 2015
        '''
        with open('project.csv', 'r') as f:
            rows = list(csv.reader(f))[1:]
            self.runtime = [int(row[7]) for row in rows if (int(row[4]) > 2015) and (int(row[4]) % 2 != 0)]
            print('The durations of movies released after 2015 in odd years:' + ' ' + str(self.runtime) + ' ' + '(minutes)')
            print('=====================================================================================================')

    def show_movie_budget(self):
        '''
        :return: prints a list with estimated budgets of movies wich have rating > 9.5 or runtime > 200 minutes
        '''
        with open('project.csv', 'r') as f:
            rows = list(csv.reader(f))[1:]
            self.budget = [float(row[11]) for row in rows if (float(row[10]) >= 9.5) or (int(row[7]) > 200)]
            print('The budgets of movies with IMDB ratings grater than 9.5 or durations grater than 200 min:' + str(self.budget)+'(USD)')
            print('=====================================================================================================')

    def show_movie_language(self):
        '''
        :return: prints a list with languages of movies produced in Canal + or 20th Century Fox studios
        '''
        with open('project.csv', 'r') as f:
            rows = list(csv.reader(f))[1:]
            self.language = [str(row[5]) for row in rows if (str(row[2]) == 'Canal +') or (str(row[2]) == '20th Century Fox')]
            print('The language of movies produced by Canal + or 20th Century Fox:', self.language)
            print('=====================================================================================================')

    def show_movie_rating(self):
        '''
        :return: prints a list with IMDB ratings of movies The Godfather or Star Trek
        '''
        with open('project.csv', 'r') as f:
            rows = list(csv.reader(f))[1:]
            self.rating = [float(row[10]) for row in rows if (str(row[0]) == 'The Godfather') or (str(row[0]) == 'Star Trek')]
            print('The IMDB rating of THE GODFATHER or STAR TREK movie is:', self.rating)
            print('=====================================================================================================')

class CommercialMovie(Movie):

    def __init__(self, title, year, director, actor, genre, runtime, budget, language, rating, commercial):
        '''
        Defining the constructor of sub-class CommercialMovie (child class)
        The single inheritance is made with super() method - provides the access to those methods of parents class which
        have been overridden in child class that inherits from it
        :param commercial: the type of movie
        '''
        super().__init__(title, year, director, actor, genre, runtime, budget, language, rating)
        self.commercial = commercial

    def commercial_movie(self):
        '''
        :return: prints a list with titles of movies that are of commercial type
        '''
        with open('project.csv', 'r') as f:
            rows = list(csv.reader(f))[1:]
            self.commercial = [str(row[0]) for row in rows if str(row[3]) == 'Comercial']
            print('The titles of commercial movies are:', self.commercial)
            print('=====================================================================================================')

class ArtMovie(Movie):

    def __init__(self, title, year, director, actor, genre, runtime, budget, language, rating, art):
        '''
        Defining the constructor of sub-class ArtMovie (child class)
        The inheritance was made with super() method
        :param art: the type of movie
        '''
        super().__init__(title, year, director, actor, genre, runtime, budget, language, rating)
        self.art = art

    def art_movie(self):
        '''
        :return: prints a list with titles of movies that are of art type
        '''
        with open('project.csv', 'r') as f:
            rows = list(csv.reader(f))[1:]
            self.art = [str(row[0]) for row in rows if str(row[3]) == 'Art']
            print('The titles of art movies are:',self.art)
            print('=====================================================================================================')

'''
Initialize the instance
Prints docstrings of methods
'''
m = Media('United States of America', 'Paramount Pictures')
print(m.market_country.__doc__)
m.market_country()
print(m.production_studio.__doc__)
m.production_studio()

a = ArtMovie('Titanic', 1997, 'Quentin Tarantino', 'Al Pacino', 'Drama', 120, 100000000.0, 'English', 9.2,'The Godfather')
print(a.show_movie_title.__doc__)
a.show_movie_title()
print(a.show_movie_year.__doc__)
a.show_movie_year()
print(a.show_movie_director.__doc__)
a.show_movie_director()
print(a.show_movie_actor.__doc__)
a.show_movie_actor()
print(a.show_movie_genre.__doc__)
a.show_movie_genre()
print(a.show_movie_runtime.__doc__)
a.show_movie_runtime()
print(a.show_movie_budget.__doc__)
a.show_movie_budget()
print(a.show_movie_language.__doc__)
a.show_movie_language()
print(a.show_movie_rating.__doc__)
a.show_movie_rating()
print(a.art_movie.__doc__)
a.art_movie()

c = CommercialMovie('Titanic', 1997, 'Quentin Tarantino', 'Al Pacino', 'Drama', 120, 100000000.0, 'English', 9.2,'Invictus')
print(c.commercial_movie.__doc__)
c.commercial_movie()
