import itertools
from .util import *
from collections import defaultdict

def optimal_phrases(tweets, objective='pwr', iso_code='nl'):
    """
    Indexes all tweets to their search phrases
    and find optimal search phrases.
    """
    lang_phrase_dict, all_phrase_dict = index_tweets(tweets, iso_code)

    # remove phrases that map to only one tweet as a heuristic
    for phrase, ids in lang_phrase_dict.items():
        if len(ids) == 1:
            del all_phrase_dict[phrase]

    optimal = generate_from_dicts(all_phrase_dict, lang_phrase_dict, objective)
    return optimal

def powerset(iterable):
    """
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    Taken from https://docs.python.org/3/library/itertools.html
    """
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s)+1))

def index_tweets(tweets, iso_code='nl'):
    """
    Generate keyword sets for tweets tagged as being of iso_code,
    and assign other language tweets to those phrases.
    """
    first = tweets
    second = itertools.tee(first_pass)

    lang_phrase_dict = first_pass(first, iso_code)
    all_phrase_dict = second_pass(second, lang_phrase_dict)
    return lang_phrase_dict, all_phrase_dict

def first_pass(tweets, isocode):
    """
    Generate keyword sets for tweets tagged as being of iso_code.
    """
    lang_phrase_dict = defaultdict(set)
    label = '__label__' + isocode
    for tweet in tweets:
        if tweet['fasttext_lang_id'] == label:
            text = tweet['text'] if not 'extended_tweet' in tweet else tweet['extended_tweet']['full_text']
            tokens = [token for token in tokenize(text) if len(token) > 1]
            if len(tokens) < 16: # heuristic for limiting the powersets to 2^16 per tweet
                for ps in powerset(tokens):
                    if ps and get_utf8_bytesize(ps) <= 60:
                        lang_phrase_dict[frozenset(ps)].add(tweet['id_str'])
    return lang_phrase_dict

def second_pass(tweets, lang_phrase_dict):
    """
    Assign all language tweets to generated keyword sets.
    """
    for tweet in tweets:
        text = tweet['text'] if not 'extended_tweet' in tweet else tweet['extended_tweet']['full_text']
        tokens = [token for token in tokenize(text) if len(token) > 1]
        if len(tokens) < 16:  # heuristic for limiting the powersets to 2^16 per tweet
            for ps in powerset(tokens):
                fps = frozenset(ps)
                if ps and fps in lang_phrase_dict:
                    lang_phrase_dict[fps].add(tweet['id_str'])
    return lang_phrase_dict

def generate_from_dicts(all_phrase_dict, lang_phrase_dict, objective='pwr', top=400):
    """
    Greedy solution for maximum coverage of tweets in lang_phrase_dict.
    """
    phrases = []

    true_positives = set()
    false_positives = set()

    recall_threshold = 100
    precision_threshold = 0.9

    for i in range(top):
        best_phrase = None
        best_result, best_ranker = 0, 0
        best_new_true_positives = set()
        best_new_false_positives = set()
        for phrase, ids in all_phrase_dict.items():
            new_true_positives = lang_phrase_dict[phrase].difference(true_positives)
            if not new_true_positives:
                continue
            new_false_positives = ids.difference(new_true_positives).difference(false_positives)

            additional_recall = len(new_true_positives)
            additional_precision = len(new_true_positives) / (len(new_false_positives) + len(new_true_positives))

            # optimize recall, precision or precision-weighted recall
            if objective == 'r' or objective == 'p' or objective == 'pwr':
                if objective == 'r':
                    result = additional_recall
                    ranker = additional_precision
                elif objective == 'p':
                    result = additional_precision
                    ranker = additional_recall
                else:
                    result = additional_recall * additional_precision
                    ranker = additional_recall

                if result > best_result or (result == best_result and ranker > best_ranker):
                    best_phrase = phrase
                    best_result = result
                    best_ranker = ranker
                    best_new_true_positives = new_true_positives
                    best_new_false_positives = new_false_positives

            # optimize recall threshold or precision threshold
            elif objective == 'rt' or objective == 'pt':
                if objective == 'rt':
                    result = additional_precision
                    ranker = additional_recall
                    threshold = recall_threshold
                else:
                    result = additional_recall
                    ranker = additional_precision
                    threshold = precision_threshold

                if result > best_result and ranker > threshold:
                    best_phrase = phrase
                    best_result = result
                    best_ranker = ranker
                    best_new_true_positives = new_true_positives
                    best_new_false_positives = new_false_positives

        phrases.append(best_phrase)
        true_positives = true_positives.union(best_new_true_positives)
        false_positives = false_positives.union(best_new_false_positives)
    return phrases
