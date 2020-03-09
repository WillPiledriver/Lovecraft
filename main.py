from Lovecraft import Lovecraft
from dotenv import load_dotenv
import os
import time
import random
import facebook


load_dotenv()
graph = facebook.GraphAPI(access_token=os.getenv("ACCESS_TOKEN"), version="6.0")
test = False
minutes = 30
authors = {"books": "H.P. Lovecraft",
           "suess": "Dr. Suess",
           "tolkien": "J.R.R. Tolkien",
           "stoker": "Bram Stoker",
           "austen": "Jane Austen",
           "london": "Jack London",
           "carroll": "Lewis Carroll"}

classes = dict()
t = time.time()
for k in list(authors.keys()):
    classes[k] = Lovecraft(k)
t2 = time.time()
print("Time to compile all books:", t2 - t)


def main():
    author = random.choice(list(authors.keys()))
    books = list()
    books.append(classes[author])
    mixer = random.randint(0, 2) == 0
    if mixer:
        _authors = list(authors.keys())
        _authors.remove(author)
        author = random.choice(_authors)
        books.append(classes[author])

    t = time.time()
    if mixer:
        word_map = books[1].generate_word_map(False)
    else:
        word_map = books[0].generate_word_map(False)
    t2 = time.time()
    title = random.choice(list(books[0].books.keys()))
    print("Generating word map:", t2 - t)

    token = books[0].rand_chunk(title)
    new = books[0].shuffle_chunk(word_map, token)
    while len(token) < 3:
        token = books[0].rand_chunk(title)
        new = books[0].shuffle_chunk(word_map, token)

    print(f'An Excerpt from "{title}" by {authors[author]}:\n\n{new}')
    if not test:
        graph.put_object(
            parent_object=str(os.getenv("USER_ID")),
            connection_name="feed",
            message=f'An Excerpt from "{title}" by {authors[author]}:\n\n{new}',
        )


if __name__ == "__main__":
    while True:
        main()
        time.sleep(minutes * 60)
