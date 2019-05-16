from omdb import OMDBClient
import matplotlib.pyplot as plt

DEBUG_INFO = False

class OMDBGrapher:

    def __init__(self, api_key):
        self.api_key = api_key
        self.omdb_client = OMDBClient(apikey=api_key)
        # TODO: Check if the key is valid. If not, raise an error.

    def get_ratings(self, title):
        # TODO: Check if valid response
        series_info = self.omdb_client.get(title=title)
        try:
            total_seasons = int(series_info['total_seasons'])
        except:
            total_seasons = 0

        ratings = []
        for i in range(1, total_seasons + 1):
            season_info = self.omdb_client.get(title=title, season=i)
            season_ratings = []
            for episode in season_info['episodes']:
                try:
                    season_ratings.append(float(episode['imdb_rating']))
                except:
                    if DEBUG_INFO:
                        print(f'No rating for episode {episode["title"]}')
                    season_ratings.append(None)

            #season_ratings = [float(episode['imdb_rating']) for episode in season_info['episodes']]
            if any(season_ratings): # Do not append empty seasons
                ratings.append((i, season_ratings))

        return ratings

    def draw_graph(self, title):
        draw_graph(title, self.get_ratings(title))

not_none = lambda x: x is not None
def get_min_rating(ratings):
    min_rating = 10
    min_w_filter = lambda y: min(filter(not_none, y[1]))
    min_rating = min(map(min_w_filter, ratings))
    return min_rating

def draw_graph(title, ratings):
    if len(ratings) == 0:
        raise Exception('Received empty ratings')
    min_rating = get_min_rating(ratings)

    plt.title(title)
    last = 0
    seasons_text_locations = []
    for season_num, season_ratings in ratings:
        # TODO handle None with hatches.
        season = list(filter(not_none, season_ratings))
        plt.bar(range(last, last + len(season)), season)
        mid = last + (len(season)/2)
        seasons_text_locations.append(mid)
        last += len(season)

    plt.ylim((min_rating - 0.5, 10))
    plt.xlim((-1, last))

    plt.box(False)
    plt.ylabel('OMDB Ratings')
    plt.xticks(seasons_text_locations, [f'Season {rating[0]}' for rating in ratings])

    plt.savefig(f'{title}.png')
    plt.figure()

if __name__ == '__main__':
    pass

