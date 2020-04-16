import sys
from twitterphrases import util
from twitterphrases import generate

def main():
    """
    Example of generating Dutch keyword sets for your datasets.
    """
    tweetfile = sys.argv[1]
    outfile = sys.argv[2]

    tweets = util.jsonl_iterator(tweetfile)
    tweets = util.lang_id(tweets)

    optimal_phrases = generate.optimal_phrases(tweets, iso_code='nl')
    open(outfile, 'w').write('\n'.join(optimal_phrases))

if __name__ == "__main__":
    if len(sys.argv) > 2:
        main()
    else:
        print("Missing command line arguments for input file and output file.")