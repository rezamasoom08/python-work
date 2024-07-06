import pandas as pd 

scraper = pd.read_html("https://en.wikipedia.org/wiki/Premier_League_records_and_statistics")

'''for i, table in enumerate(scraper):
    print("------")
    print(i)
    print(table)'''

df = scraper[0]

df.to_csv('premier_league.csv', index = False)

df_scraped_file = pd.read_csv('premier_league.csv')
print(df_scraped_file)