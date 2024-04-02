
cities = ["Addis Ababa", "Hawassa", "Bahir dar", "Gonder", "Hossana", "Adama"]
cities_with_region = {"Addis Ababa": "Addis Ababa","Hawassa": "Sidama", "Bahir dar": "Amhara", "Gonder":"Amhara", "Hossana":"South", "Adama": "Oromia"}


def iterate(iterable):
    for element in iterable:
        print(element)


def iterate_dic(dictionary):
    for k,v in dictionary.items():
        print(k + ": " + v)


iterate_dic(cities_with_region)
print("------------------------")
iterate(cities)