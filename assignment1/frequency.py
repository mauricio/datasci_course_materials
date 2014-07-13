import sys
import json

def load_tweets(path):
  tweet_file = open(path)
  tweets = []
  for line in tweet_file:
    tweet = json.loads(line)
    if ("text" in tweet) and tweet["text"] and ("lang" in tweet) and tweet["lang"] == "en":
      tweets.append(tweet)
  return tweets

def calculate_frequencies( tweets ):
  frequencies = {}
  total_frequencies = 0
  for tweet in tweets:
    for base_word in tweet["text"].split(" "):
      word = unicode(base_word.strip().lower())
      if word:
        total_frequencies += 1
        if word in frequencies:
          frequencies[word] = frequencies[word] + 1
        else:
          frequencies[word] = 1
  result = {}
  for word, count in frequencies.iteritems():
    result[word] = count/total_frequencies
  return result

def main():
  tweets = load_tweets(sys.argv[1])
  frequencies = calculate_frequencies(tweets)
  for word, count in frequencies.iteritems():
    print u'{0} {1}'.format(word, count)

if __name__ == '__main__':
    main()
