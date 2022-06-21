import movieApi
import unittest


class TestMovieApi(unittest.TestCase):
    def test_movie_titles_list_with_positive_title(self):
        title = 'Aquaman'
        names = movieApi.getMovieTitlesByTitle(title=title)
        self.assertEqual(len(names), 14)
        self.assertIn(title, names[13])
        self.assertIn(title, names[0])
        self.assertIn(title, names[7])

    # 'Aqua boy' is not a correct title
    def test_movie_titles_list_with_negative_title(self):
        title = 'Aqua boy'
        names = movieApi.getMovieTitlesByTitle(title=title)
        self.assertEqual(len(names), 0)
        self.assertNotIn(title, names)

    def test_movie_titles_list_by_year_with_positive_data(self):
        year = 1995
        names, dates = movieApi.getMovieTitlesByYear(year=year)
        self.assertEqual(len(dates), 27)
        self.assertEqual(len(names), 27)
        self.assertFalse(len(dates) < 27)
        self.assertFalse(len(names) > 27)
        self.assertIn(year, dates)

    # Year 2022 not in the dates list that API returns
    def test_length_of_the_movie_titles_list_by_year_with_negative_data(self):
        year = 2022
        names, dates = movieApi.getMovieTitlesByYear(year=year)
        self.assertEqual(len(names), 0)
        self.assertEqual(len(dates), 0)
        self.assertNotIn(2022, dates)
