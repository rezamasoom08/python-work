from googlesearch import search

def GoogleSearch(Query):
    SearchResults = search(Query, num_results = 10)

    for i, results in enumerate(SearchResults, start = 1):
        print(f'Result {i}: {results}')
    
Query = input('Which term would you like to search for? ')
GoogleSearch(Query)