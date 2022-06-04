from typing import List, Any

import requests
# import json
# import pandas as pd


def make_url(api, fr_, to_):
    fr = fr_ + "-01-01"
    to = to_ + "-01-01"
    url = "https://imdb-api.com/API/AdvancedSearch/{}?title_type=feature&release_date={},{}&countries=gb,us&count=250".format(
        api, fr, to)
    response = requests.get(url)
    j = response.json()
    jr = j['results']
    return jr


def lists1(self, jr):
    Title = []
    Release_Year = []
    Run_Time = []
    Director = []
    Imdb_Rating = []
    Meta_Critic = []
    Content_Rating = []
    Genres = []
    for i in range(0, len(jr)):
        title_ = jr[i]['title']
        release_year_ = jr[i]['description']
        run_time_ = jr[i]['runtimeStr']
        imdb_rating_ = jr[i]['imDbRating']
        meta_critic_ = jr[i]['metacriticRating']
        content_rating_ = jr[i]['contentRating']
        genres_ = jr[i]['genres']

        Title.append(title_)
        Release_Year.append(release_year_)
        Run_Time.append(run_time_)
        Imdb_Rating.append(imdb_rating_)
        Meta_Critic.append(meta_critic_)
        Content_Rating.append(content_rating_)
        Genres.append(genres_)

    return Title, Release_Year, Run_Time, Imdb_Rating, Meta_Critic, Content_Rating, Genres


def id_list(self, json_response):
    id = []
    for i in range(0, len(json_response)):
        id_ = json_response[i]['id']
        id.append(id_)
    return id


def lists2(self, api, ids):
    Dir = []
    Dop = []
    Mus = []
    for i in range(0, len(ids)):
        url2 = "https://imdb-api.com/en/API/FullCast/{}/{}".format(api, ids[i])
        res = requests.get(url2)
        jr2 = res.json()
        if jr2['directors'] == None:
            pass
        else:
            Director = jr2['directors']['items'][0]['name']
        if jr2['others'] == None or len(jr2['others']) == 0:
            pass
        else:
            DOP = jr2['others'][2]['items'][0]['name']
        if jr2['others'] == None or len(jr2['others']) == 0:
            pass
        else:
            Music_by = jr2['others'][1]['items'][0]['name']

        Dir.append(Director)
        Dop.append(DOP)
        Mus.append(Music_by)
    return Dir, Dop, Mus


# def make_df(self, lists):
#     imdb_dict = {"Title": Title, "Release_Year": Release_Year, "Director": Dir, "Director of Photography": Dop,
#                  "Music Director": Mus, "Imdb_Rating": Imdb_Rating, "Meta_Critic": Meta_Critic,
#                  "Content_Rating": Content_Rating, "Genres": Genres}
#     imdb = pd.DataFrame(imdb_dict)