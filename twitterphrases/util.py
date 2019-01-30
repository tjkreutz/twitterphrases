import re
import json
import string
import fastText

MODEL = fastText.load_model('lid.176.bin')
REMOVE = string.punctuation.replace("@", "").replace("#", "")

def get_utf8_bytesize(set):
    """
    Return the size in bytes of a set of utf-encoded strings.
    """
    return sum([len(s.encode('utf-8')) for s in set])

def tokenize(text):
    """
    Custom tokenization adhering to rules for Twitter keyword matching.
    """
    lowered = text.lower()
    removed = re.sub(r'[{}]'.format(REMOVE), " ", lowered)
    splitted = removed.split()
    return splitted

def output_tweets(tweets, fn):
    """
    Write tweets in jsonl format.
    """
    with open(fn, 'w') as fo:
        for tweet in tweets:
            fo.write(json.dumps(tweet))
            fo.write('\n')

def jsonl_iterator(fp):
    """
    Iterator for tweets in jsonl format.
    """
    with  open(fp) as file:
        for line in file:
            yield json.loads(line)

def remove_doubles_and_retweets(tweets):
    """
    Remove double tweets (same id) and tweets that are retweets.
    """
    newtweets = []
    ids = set()
    for tweet in tweets:
        if not 'retweeted_status' in tweet:
            if 'id_str' in tweet:
                if not tweet['id_str'] in ids:
                    ids.add(tweet['id_str'])
                    newtweets.append(tweet)
    return newtweets

def lang_id(tweets):
    """
    Identify the language of tweets using the fasttext model.
    """
    newtweets = []
    for tweet in tweets:
        if 'text' not in tweet:
            continue
        text = tweet['text'] if not 'extended_tweet' in tweet else tweet['extended_tweet']['full_text']
        text = text.replace('\n', ' ')
        lang_pred = MODEL.predict(text)
        tweet['fasttext_lang_id'] = lang_pred[0][0]
        tweet['fasttext_lang_prob'] = lang_pred[1][0]
        newtweets.append(tweet)
    return newtweets
