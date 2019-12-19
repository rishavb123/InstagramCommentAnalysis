from instaloader import Instaloader, Post, Profile
from textblob import TextBlob

L = Instaloader()

total = 0
count = 0

USERNAME = "sbvikings2020"
# USERNAME = "google"
for post in Profile.from_username(L.context, USERNAME).get_posts():


    print(post.caption)
    # for c in post.get_comments():
    #     blob = TextBlob(c.text)

    #     if blob.sentiment.subjectivity > 0.2:
    #         total += blob.sentiment.polarity
    # count += 1
    # print("\r", count, end='')

    print('-----------------------------------------')

# print("\nAverage Polarity:", total / count if count != 0 else 0)

