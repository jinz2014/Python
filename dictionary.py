# define canada_birds dictionary
canada_birds = {};
canada_birds['snow goose'] = 33
canada_birds['northern fulmar'] = 66
canada_birds['canada goose'] = 58

for bird in canada_birds:
  print(bird, canada_birds[bird])

# dic operations
# return a set
print(canada_birds.keys())

# return a set
print(canada_birds.values())

# return the value associated with the key
print(canada_birds.get('canada goose'))

# remove the key and return the value associated with it
print(canada_birds.pop('snow goose'))

print(canada_birds.keys())

#
asian_birds = {};
asian_birds['duck'] = 44;
asian_birds['sparrow'] = 54;
canada_birds.update(asian_birds);
print(canada_birds.items())


observation_file = open('observation.txt')
us_birds = {}
for line in observation_file:
  bird = line.strip();
  us_birds[bird] = us_birds.get(bird, 0) + 1;
observation_file.close()

# random
for bird, count in us_birds.items():
  print(bird, count)

# sorted
sorted_birds = sorted(us_birds.keys())
for bird in sorted_birds:
  print(bird, us_birds[bird])


# revert the dictionary
# each entry in the dictionary is key and a *list*
count_birds = {}
for bird, count in us_birds.items():
  if count in count_birds:
    count_birds[count].append(bird)
  else:
    count_birds[count] = [bird]; # [] is required

count_sorted = sorted(count_birds.keys())
for count in count_sorted:
  print(count, count_birds[count])

