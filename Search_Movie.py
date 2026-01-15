import argparse
import requests
from dotenv import load_dotenv
import os
def movie_fetch(movie_name, api_key):
    Web_URL = "https://api.themoviedb.org/3/search/movie"
    params = {
        "api_key": api_key,
        "query": movie_name
    } 
    response = requests.get(Web_URL, params=params)
    if response.status_code != 200:
        print("Error fetching movie")
        return

    data = response.json()

    if not data["results"]:
        print("Movie not found")
        return
    movie=data["results"][0]
    #movie_id=movie["id"]
    Mname=movie["title"]
    rating=movie["vote_average"]
    overall=movie["overview"]
    RelDate=movie["release_date"]
    print(f"Title: {Mname}")
    print(f"Released: {RelDate}")
    print(f"Ratings: {rating}")
    print(f"Synopsis: {overall}")
def main():
    load_dotenv("Api.env")
    API_KEY = os.getenv("tmdbAPI")
    parser = argparse.ArgumentParser(description="Search For a movie")
    parser.add_argument("movie", help="Movie Name")
    args = parser.parse_args()
    movie_fetch(args.movie, API_KEY)
if __name__=="__main__":
    main()