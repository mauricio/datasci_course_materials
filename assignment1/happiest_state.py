import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

def load_sentiments(path):
  afinnfile = open(path)
  scores = {}
  for line in afinnfile:
    term, score  = line.split("\t")
    scores[term] = int(score)
  return scores

def calculate_score(word, scores):
  if word in scores:
    return scores[word]
  else:
    return 0.0

def add(x, y):
  return x + y

def calculate_tweet_score( tweet, scores ):
  if not ("text" in tweet) or (not tweet["text"]):
    return 0.0
  else:
    result = [calculate_score(text, scores) for text in tweet["text"].split(" ")]
    return reduce(add, result)

def score_tweets( tweets, scores ):
  result = []
  for tweet in tweets:
    value = calculate_tweet_score(tweet, scores)
    tweet["score"] = value
    result.append(tweet)
  return result

def load_tweets(path):
  tweet_file = open(path)
  tweets = []
  for line in tweet_file:
    tweet = json.loads(line)
    if tweet.get("text") and tweet.get("lang") == "en":
      tweets.append(tweet)
  return tweets

def tweets_with_states(path):
  all = load_tweets(path)
  tweets = []
  for tweet in all:
    if tweet.get("place") and tweet["place"].get("full_name") and tweet["place"].get("country") == "United States":
      city, state = tweet["place"]["full_name"].split(", ")
      for key in states:
        if state and state == key:
          tweet["state"] = key
          tweets.append(tweet)
  return tweets

def main():
  scores = load_sentiments(sys.argv[1])
  tweets = tweets_with_states(sys.argv[2])
  results = score_tweets(tweets, scores)
  groups = {}
  for tweet in results:
    if not groups.get(tweet["state"]):
      groups[tweet["state"]] = []
    groups[tweet["state"]].append(tweet["score"])
  means = {}
  for state in groups:
    values = groups[state]
    means[state] = sum(groups[state]) / len(values)

  happiest_value = -100.0
  happiest_state = "NA"

  for state, value in means.iteritems():
    if value > happiest_value:
      happiest_value = value
      happiest_state = state

  print happiest_state

if __name__ == '__main__':
    main()
