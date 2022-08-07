
punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

#function to strip punctuations
def strip_punctuation(wrd):
    new_wrd =str()
    for ch in wrd:
        if ch not in punctuation_chars:
            new_wrd = new_wrd + ch
    return new_wrd

#function to count negaative words
def get_neg(input_str):
    stripped_str = strip_punctuation(input_str)
    new_str = stripped_str.lower().split()
    neg_count = 0
    for wrd in new_str:
        if wrd in negative_words:
            neg_count += 1
    return neg_count

#function to get positive words
def get_pos(input_str):
    stripped_str = strip_punctuation(input_str)
    new_str = stripped_str.lower().split()
    pos_count = 0
    for wrd in new_str:
        if wrd in positive_words:
            pos_count += 1
    return pos_count
    
#get the tweets into a list
csv_handler = open('project_twitter_data.csv', 'r')
tweet_lst = list()
for line in csv_handler:
    tweet_lst.append(line.strip().split(","))
#print(tweet_lst)

#create and write to a new list
new_csv = open("resulting_data.csv",'w')
new_csv.write("{}, {}, {}, {}, {}".format("Number of Retweets","Number of Replies","Positive Score","Negative Score","Net Score"))
new_csv.write('\n')
for tweet in tweet_lst[1:]:
    retweet_count = tweet[1]
    reply_count = tweet[2]
    pos_score = get_pos(tweet[0])
    neg_score = get_neg(tweet[0])
    net_score = pos_score - neg_score
    new_csv.write("{}, {}, {}, {}, {}".format(retweet_count,reply_count,pos_score,neg_score,net_score))
    new_csv.write('\n')
    
csv_handler.close()
new_csv.close
