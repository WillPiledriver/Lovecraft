from Lovecraft import Lovecraft
import time
import random
import facebook

access_token = ""
graph = facebook.GraphAPI(access_token=access_token, version="6.0")
test = False
authors = {"books": "H.P. Lovecraft",
             "suess": "Dr. Suess",
             "tolkien": "J.R.R. Tolkien"}

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
    mixer = random.randint(0, 4) == 0
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
    while len(token) == 0:
        token = books[0].rand_chunk(title)
    new = books[0].shuffle_chunk(word_map, token)

    print(f'An Excerpt from "{title}" by {authors[author]}:\n\n{new}')
    if not test:
        graph.put_object(
            parent_object="",
            connection_name="feed",
            message=f'An Excerpt from "{title}" by {authors[author]}:\n\n{new}',
        )


if __name__ == "__main__":
    while True:
        main()
        time.sleep(1800)
