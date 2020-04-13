import requests, json

def get_url_data(url, params): 
    # params is key word argument that contains data for GR api
    response = requests.get(url, params=params) # contacts url and gets data
    return response.json()

url = 'https://www.goodreads.com/book/isbn_to_id'

key = 'yfDBeS4CL7NKpQa0i0ccPA'

isbn = input('Input a book ISBN: ')

params = {
    'key': key,
    'isbn': isbn
}

book_id = get_url_data(url, params)

url2 = 'https://www.goodreads.com/book/show.json'
params = {
    # 'format': 'json',
    'id': book_id,
    'key': key
}

# goodreads api is poor, doesn't return much useful data in json format
# this is why reviews is not used
reviews = get_url_data(url2, params)

reviews_url = 'https://www.goodreads.com/book/review_counts.json'

params = {
    'isbns': isbn,
    'key': key,
}

reviews = get_url_data(reviews_url, params)
# print(reviews)

avg_rating = reviews['books'][0]['average_rating']

print('Average rating', avg_rating)
