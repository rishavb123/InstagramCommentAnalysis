from instaloader import Instaloader, Post
from textblob import TextBlob

L = Instaloader()

url = input("Paste the url: ")
# Positive Post: https://www.instagram.com/p/B2b9-yPpyev/
# Negative Post: https://www.instagram.com/p/BsbFhcHFvha/

code = url.split("/")[len(url.split("/")) - 2]

post = Post.from_shortcode(L.context, code)

total = 0
count = 0

for c in post.get_comments():
    blob = TextBlob(c.text)

    if blob.sentiment.subjectivity > 0.2:
        total += blob.sentiment.polarity
        count += 1

print("Average Polarity:", total / count if count != 0 else 0)