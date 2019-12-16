from instaloader import Instaloader, Post
from textblob import TextBlob
import sys

L = Instaloader()

url = input("Paste the url: ")

code = url.split("/")[len(url.split("/")) - 2]

post = None

try:
    post = Post.from_shortcode(L.context, code)
except:
    L.interactive_login(input("Enter Instagram username: ")) 
    try:
        post = Post.from_shortcode(L.context, code)
    except:
        print("Post Not Found")
        sys.exit()

total = 0
count = 0

for c in post.get_comments():
    c = c.text
    blob = TextBlob(c)

    if blob.sentiment.subjectivity > 0.2:
        total += blob.sentiment.polarity
        count += 1

print("Average Polarity:", total / count if count != 0 else 0)