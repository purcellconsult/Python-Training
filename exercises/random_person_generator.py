# --------------------------------------
# what are some things people have?
# first name
# last name
# gender
# place of birth
# favorite music
# ---------------------------------------

from random import choice


def first_name():
    """
    names to choose from
    """
    first = ['Bob', 'Jim', 'Beth', 'Zoey', 'Mike', 'Doug', 'Sandra', 'Kobe']
    name = choice(first)
    return name


def last_name():
    """
    return a random last name
    """
    last_names = ['Johnson', 'Smith', 'Doe', 'Lennister', 'Williams', 'Simpson', 'Rogers', 'Doubtfire']
    return choice(last_names)


def city_of_birth():
    """
    randomly select a city from
    a list of options.
    """
    cities = ['nyc', 'san francisco', 'miami', 'houston', 'madison']
    i = 0
    while i < 0:
        cities[i].capitalize()
        i += 1
    return choice(cities)


def favorite_music():
    """
    randomly select music from list of options.

    """
    music = ['hip hop', 'r and b', 'rock and roll', 'electronic', 'jazz', 'classical']
    i = 0
    while i < 0:
        music[i].capitalize()
        i += 1
    return choice(music)


def create_person():
    """
    a string that combines
    all of the details together.
    """
    first = first_name()
    last = last_name()
    city = city_of_birth()
    music = favorite_music()
    person = "{} {} is from {} and likes to listen to {} music.".format(first, last, city, music)
    print(person)


for x in range(100):
    create_person()
    print('----------')