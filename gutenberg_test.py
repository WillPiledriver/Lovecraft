from Lovecraft import Lovecraft


authors = ["Carroll, Lewis"]

bibliography = list()
word_maps = list()
i = 0
for author in authors:
    bibliography.append(Lovecraft(author=author))
    word_maps.append(bibliography[i].generate_word_map(False))
    i += 1


chunk = bibliography[0].rand_chunk(list(bibliography[0].books.keys())[0])
print(bibliography[0].shuffle_chunk(word_maps[0], chunk))
print("Thank you")