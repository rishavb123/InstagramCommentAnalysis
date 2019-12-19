from instaloader import Instaloader, Post, Profile
from textblob import TextBlob

L = Instaloader()

HASHTAG = 'compscimemes'

total = 0
count = 0

for post in L.get_hashtag_posts(HASHTAG):

    for c in post.get_comments():
        blob = TextBlob(c.text)

        if blob.sentiment.subjectivity > 0.2:
            total += blob.sentiment.polarity
            count += 1
            print("\r", count, end='')

print("\nAverage Polarity:", total / count if count != 0 else 0)

# total = 0
# count = 0

# USERNAME = "sbvikings2020"

# for post in Profile.from_username(L.context, USERNAME).get_posts():

#     for c in post.get_comments():
#         blob = TextBlob(c.text)

#         if blob.sentiment.subjectivity > 0.2:
#             total += blob.sentiment.polarity
#     count += 1
#     print("\r", count, end='')

# print("\nAverage Polarity:", total / count if count != 0 else 0)