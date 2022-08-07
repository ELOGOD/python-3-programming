import requests_with_caching
import json
def get_movies_from_tastedive(movie_name):
    d={"q":movie_name,"type":"movies","limit":5}
    res=requests_with_caching.get("https://tastedive.com/api/similar",params=d)
    return json.loads(res.text)

def extract_movie_titles(resp):
    m_list = resp['Similar']['Results']
    movies = [movie['Name'] for movie in m_list]
    return movies

def get_related_titles(lst):
    lst2=[]
    x=[]
    for i in lst:
        x.append(extract_movie_titles(get_movies_from_tastedive(i)))
    for i in x:
        for j in i:
            if j not in lst2:
                lst2.append(j)
    return lst2 

def get_movie_data(m_name):
    m_query = {}
    m_query['t'] = m_name
    m_query['r'] = 'json'
    base_url = 'http://www.omdbapi.com/'
    res = requests_with_caching.get(base_url, params=m_query)
    resp = res.json()
    return resp

def get_movie_rating(resp):
    m_ratings = resp['Ratings']
    for rate in m_ratings:
        if rate['Source'] == 'Rotten Tomatoes':
            value = int(rate['Value'][:-1])
            return value
        else: return 0
        
def get_sorted_recommendations(mtitles_lst):
    rel_titles = get_related_titles(mtitles_lst)
    d = {}
    for title in rel_titles:
        d[title] = get_movie_rating(get_movie_data(title))
    rel_movies = list(sorted(d.keys(), key = lambda key: d[key], reverse = True))
    return rel_movies
    
# some invocations that we use in the automated tests; uncomment these if you are getting errors and want better error messages
get_sorted_recommendations(["Bridesmaids", "Sherlock Holmes"])