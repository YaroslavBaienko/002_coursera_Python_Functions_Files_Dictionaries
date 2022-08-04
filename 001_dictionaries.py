eng2sp = dict()
eng2sp['one'] = 'uno'
eng2sp['two'] = 'dos'
eng2sp['three'] = 'tre'
eng2sp['four'] = 'quarto'

print(eng2sp)
print(eng2sp['four'])

del eng2sp['two']
print(eng2sp)
eng2sp['two'] = 2
print(eng2sp)
eng2sp['two'] = eng2sp['two'] + 200
print(eng2sp)
numitems = len(eng2sp)
print(numitems)
eng2sp['hui'] = eng2sp['one'] + str(eng2sp['two'])
print(eng2sp['hui'])

rushka = dict()
rushka = {'putin': 'huilo', 'russian_warship': 'go_fuck_yourself', 'kadirov': 'tiktok'}
rushka['putikadr'] = rushka['putin'] + rushka['kadirov']
print(rushka)

inventory = {'apples': 430, 'bananas': 345, 'oranges': 234, 'pears': 123}
print(inventory['oranges'])
for key in inventory.keys():
    print(key, 'has the value', inventory[key])

keys = list(inventory.keys())
print(keys)

values = list(inventory.values())
print(values)

iteritems = list(inventory.items())

for item in iteritems:
    print(item)

print('apples' in inventory)
print('cherries' in inventory)

if 'bananas' in inventory:
    wehave = inventory['bananas']
    print(f'We han an {wehave} bananas')
else:
    print('We dont ha any bananas')


def purchases():
    inventory = dict()
    while True:
        waiter = input('Желаете что-то добавить в корзину? напишите да, если желаете ')
        if waiter == 'да':
            we_buy = input('Что мы хотим добавить в корзину? ')
            how_many = int(input(f'Сколько {we_buy} вы купили? '))
            inventory[we_buy] = how_many
        else:
            break
    total = 0
    for akey in inventory:
        if len(inventory) >= 3:
            total = total + inventory[akey]
        else:
            total = "We don't have enough purchases"
    return str(total)


swimmers = {'Manuel': 4, 'Lochte': 12, 'Adrian': 7, 'Ledecky': 5, 'Dirado': 4, 'Phelps': 23}
print(swimmers)

# Add the string “hockey” as a key to the dictionary sports_periods and assign it the value of 3. Do not rewrite the
# entire dictionary.
sports_periods = {'baseball': 9, 'basketball': 4, 'soccer': 4, 'cricket': 2, 'hockey': 3}
print(sports_periods)

# The dictionary golds contains information about how many gold medals each country won in the 2016 Olympics. But
# today, Spain won 2 more gold medals. Update golds to reflect this information.
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}
golds['Spain'] = golds['Spain'] + 2
print(golds)

# Create a list of the countries that are in the dictionary golds, and assign that list to the variable name
# countries. Do not hard code this.
golds = {"Italy": 12, "USA": 33, "Brazil": 15, "China": 27, "Spain": 19, "Canada": 22, "Argentina": 8, "England": 29}

countries = list(golds)
print(countries)

# Provided is the dictionary, medal_count, which lists countries and their respective medal count at the halfway
# point in the 2016 Rio Olympics. Using dictionary mechanics, assign the medal count value for "Belarus" to the
# variable belarus. Do not hardcode this.
medal_count = {'United States': 70, 'Great Britain': 38, 'China': 45, 'Russia': 30, 'Germany': 17, 'Italy': 22,
               'France': 22, 'Japan': 26, 'Australia': 22, 'South Korea': 14, 'Hungary': 12, 'Netherlands': 10,
               'Spain': 5, 'New Zealand': 8, 'Canada': 13, 'Kazakhstan': 8, 'Colombia': 4, 'Switzerland': 5,
               'Belgium': 4, 'Thailand': 4, 'Croatia': 3, 'Iran': 3, 'Jamaica': 3, 'South Africa': 7, 'Sweden': 6,
               'Denmark': 7, 'North Korea': 6, 'Kenya': 4, 'Brazil': 7, 'Belarus': 4, 'Cuba': 5, 'Poland': 4,
               'Romania': 4, 'Slovenia': 3, 'Argentina': 2, 'Bahrain': 2, 'Slovakia': 2, 'Vietnam': 2,
               'Czech Republic': 6, 'Uzbekistan': 5}
belarus = medal_count['Belarus']
print(belarus)

# The dictionary total_golds contains the total number of gold medals that countries have won over the course of
# history. Use dictionary mechanics to find the number of golds Chile has won, and assign that number to the variable
# name chile_golds. Do not hard code this!

total_golds = {"Italy": 114, "Germany": 782, "Pakistan": 10, "Sweden": 627, "USA": 2681, "Zimbabwe": 8, "Greece": 111,
               "Mongolia": 24, "Brazil": 108, "Croatia": 34, "Algeria": 15, "Switzerland": 323, "Yugoslavia": 87,
               "China": 526, "Egypt": 26, "Norway": 477, "Spain": 133, "Australia": 480, "Slovakia": 29, "Canada": 22,
               "New Zealand": 100, "Denmark": 180, "Chile": 13, "Argentina": 70, "Thailand": 24, "Cuba": 209,
               "Uganda": 7, "England": 806, "Denmark": 180, "Ukraine": 122, "Bahamas": 12}
chile_golds = total_golds['Chile']
print(chile_golds)

# Provided is a dictionary called US_medals which has the first 70 metals that the United States has won in 2016,
# and in which category they have won it in. Using dictionary mechanics, assign the value of the key "Fencing" to a
# variable fencing_value. Remember, do not hard code this.
US_medals = {"Swimming": 33, "Gymnastics": 6, "Track & Field": 6, "Tennis": 3, "Judo": 2, "Rowing": 2, "Shooting": 3,
             "Cycling - Road": 1, "Fencing": 4, "Diving": 2, "Archery": 2, "Cycling - Track": 1, "Equestrian": 2,
             "Golf": 1, "Weightlifting": 1}

fencing_value = US_medals['Fencing']

# f = open('voina.txt', 'r')
#
# txt = f.read()
#
# txt = txt.split()
#
# chars = dict()
# for c in txt:
#     if c not in chars:
#         chars[c] = 0
#     chars[c] = chars[c] + 1
#
# print(chars)
# f.close()


sentence = "The dog chased the rabbit into the forest but the rabbit was too quick."

words = sentence.split()
words_count = dict()

for word in words:
    if word not in words_count:
        words_count[word] = 0
    words_count[word] = words_count[word] + 1

print(words_count)

stri = "what can I do"

char_d = dict()
for c in stri:
    if c not in char_d:
        char_d[c] = 0
    char_d[c] = char_d[c] + 1

print(char_d)

place = """How do I exit all virtual environments and work on my system environment again? Right now, the only way I 
have of getting back to me@mymachine:~$ is to exit the shell and start a new one. That's kind of annoying. Is there a 
command to work on "nothing", and if so, what is it? If such a command does not exist, how would I go about creating 
it? """

d = {}

for c in place:
    if c not in d:
        d[c] = 0
    d[c] = d[c] + 1

keys = list(d.keys())
min_value = keys[0]

for key in keys:
    if d[key] < d[min_value]:
        min_value = key

max_value = keys[0]
for key in keys:
    if d[key] > d[max_value] and key != " ":
        max_value = key

print('"' + min_value + '"', 'used', d[min_value], 'times')
print('"' + max_value + '"', 'used', d[max_value], 'times')

f = open('voina.txt', 'r')

txt = f.read()
txt = txt.split()

chars = dict()
for c in txt:
    if c not in chars:
        chars[c] = 0
    chars[c] = chars[c] + 1

print(chars)
keys = list(chars.keys())

min_value_v = keys[0]
for key in keys:
    if chars[key] < chars[min_value_v]:
        min_value_v = key

max_value_v = keys[0]
for key in keys:
    if chars[key] > chars[
        max_value_v] and key != "-" and key != " " and key != "и" and key != "в" and key != "не" and key != "на" and key != "он":
        max_value_v = key
print('"' + min_value_v + '"', 'used', chars[min_value_v], 'times')
print('"' + max_value_v + '"', 'used', chars[max_value_v], 'times')

# The dictionary Junior shows a schedule for a junior year semester. The key is the course name and the value is the
# number of credits. Find the total number of credits taken this semester and assign it to the variable credits. Do
# not hardcode this – use dictionary accumulation!
Junior = {'SI 206': 4, 'SI 310': 4, 'BL 300': 3, 'TO 313': 3, 'BCOM 350': 1, 'MO 300': 3}
values = list(Junior.values())
total = 0
for c in values:
    total = total + c
print(total)

#Create a dictionary, freq, that displays each character in string str1 as the key and its frequency as the value.
str1 = "peter piper picked a peck of pickled peppers"
freq = dict()
total = 0
for c in str1:
    if c not in freq:
        freq[c] = 0
    freq[c] = freq[c] + 1

print(freq)