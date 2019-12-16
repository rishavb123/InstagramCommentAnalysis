from instaloader import Instaloader, Post
from textblob import TextBlob

L = Instaloader()

# url = input("Paste the url: ")
# # Negative Post: https://www.instagram.com/p/BsbFhcHFvha/

# code = url.split("/")[len(url.split("/")) - 2]

# post = Post.from_shortcode(L.context, code)

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