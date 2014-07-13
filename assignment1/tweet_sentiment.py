import sys
import json

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
    return 0

def add(x, y):
  return x + y

def calculate_tweet_score( tweet, scores ):
  if not ("text" in tweet) or (not tweet["text"]):
    return 0
  else:
    result = [calculate_score(text, scores) for text in tweet["text"].split(" ")]
    return reduce(add, result)

def main():
  sentiments = load_sentiments(sys.argv[1])
  tweet_file = open(sys.argv[2])
  for tweet in tweet_file:
    print calculate_tweet_score(json.loads(tweet), sentiments)

if __name__ == '__main__':
  main()
