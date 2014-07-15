import sys
import json

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
    if tweet.get("entities") and len(tweet["entities"]["hashtags"]) > 0:
      tweets.append(tweet)
  return tweets

def main():
  tweets = load_tweets(sys.argv[1])
  hashtags = {}
  for tweet in tweets:
    for hashtag in tweet["entities"]["hashtags"]:
      key = hashtag["text"]
      if not hashtags.get(key):
        hashtags[key] = 1
      else:
        hashtags[key] = hashtags[key] + 1

  result = sorted(hashtags.items(), key=lambda student: student[1], reverse=True)
  for index in range(10):
    print u"{0} {1}".format(result[index][0], result[index][1])

if __name__ == '__main__':
    main()
