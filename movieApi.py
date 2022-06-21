import requests


def getMovieTitlesByTitle(title):
    titles = []
    page = 1
    totalPages = 1

    while page <= totalPages:
        req = requests.get(
            'https://jsonmock.hackerrank.com/api/movies/search/?Title=' + str(title) + '&page=' + str(page))
        movies = req.json()['data']

        if page == 1:
            totalPages = req.json()["total_pages"]

        for movie in movies:
            titles.append(movie['Title'])

        # go to next page
        page += 1

    # sorts list by alphabetical order
    titles.sort()
    return titles


def getMovieTitlesByYear(year):
    titles = []
    years = []
    page = 1
    totalPages = 1

    while page <= totalPages:
        req = requests.get(
            'https://jsonmock.hackerrank.com/api/movies/search/?Year=' + str(year) + '&page=' + str(page))
        movies = req.json()['data']

        if page == 1:
            totalPages = req.json()["total_pages"]

        for movie in movies:
            titles.append(movie['Title'])
            years.append(movie['Year'])

        # go to next page
        page += 1

    # sorts list by alphabetical order
    titles.sort()
    years.sort()
    return titles, years
