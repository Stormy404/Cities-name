from fuzzywuzzy import process

with open('r.txt', 'r') as f:
    cities = f.read().split("\n")


    def get_matches(query, choices, limit=3):
        results = process.extract(query, choices, limit=limit)
        return results
a = get_matches((input(" ")), cities)
print(a)
