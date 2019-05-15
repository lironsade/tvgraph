import omdb
import matplotlib.pyplot as plt


# OMDB stuff
OMDB_API_KEY = None
if OMDB_API_KEY is None:
    OMDB_API_KEY = '65d268f9'
omdb.set_default('apikey', OMDB_API_KEY)

def get_ratings(title=None):
    SERIES_TITLE = title

    series_info = omdb.get(title=SERIES_TITLE)
    total_seasons = int(series_info['total_seasons'])

    ratings = []
    for i in range(1, total_seasons + 1):
        season_info = omdb.get(title=SERIES_TITLE, season=i)
        season_ratings = []
        for episode in season_info['episodes']:
            try:
                season_ratings.append(float(episode['imdb_rating']))
            except:
                print(f'No rating for episode {episode["title"]}')

        #season_ratings = [float(episode['imdb_rating']) for episode in season_info['episodes']]
        ratings.append(season_ratings)
    return ratings

def get_ratings_stub(title=None):
    ratings = [
            [8.9, 8.7, 8.7, 8.3, 8.3, 9.2, 8.8],
            [8.7, 9.2, 8.4, 8.1, 8.3, 8.8, 8.7, 9.0, 8.9, 8.6, 8.8, 9.1, 9.1],
            [8.6, 8.7, 8.4, 8.2, 8.7, 9.3, 9.5, 8.8, 8.4, 7.7, 8.5, 9.5, 9.6],
            [9.1, 8.3, 8.0, 8.7, 8.7, 8.5, 8.9, 9.2, 8.8, 9.6, 9.6, 9.4, 9.9],
            [9.2, 8.8, 8.8, 8.8, 9.6, 8.9, 9.5, 9.5, 9.4, 9.1, 9.5, 8.9, 9.8, 9.9, 9.6, 9.9]
    ]
    return ratings

def get_min_rating(ratings):
    min_rating = 10
    for season in ratings:
        min_rating = min(min(season), min_rating)
    return min_rating


def graph_it(title=None, ratings=None):
    min_rating = get_min_rating(ratings)

    plt.title(title)
    last = 0
    seasons_text_locations = []
    for season in ratings:
        plt.bar(range(last, last + len(season)), season)
        mid = last + (len(season)/2)
        seasons_text_locations.append(mid)
        last += len(season)

    plt.ylim((min_rating - 0.5, 10))
    plt.xlim((-1, last))
    plt.box(False)
    plt.ylabel('IMDB Ratings')

    plt.xticks(seasons_text_locations, [f'Season {i}' for i in range(1, len(ratings) + 1)])

    #plt.bar(range(len(ratings)), ratings)
    plt.show()

    


if __name__ == '__main__':
    title = 'Silicon Valley'
    graph_it(title, get_ratings(title))

