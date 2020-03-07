from Lovecraft import Lovecraft


def main():
    love = Lovecraft("books")
    word_map = love.generate_word_map()
    book = list(love.books.keys())[0]
    token = love.rand_chunk(book)

    new = love.shuffle_chunk(word_map[book], token)
    print(new)


if __name__ == "__main__":
    main()