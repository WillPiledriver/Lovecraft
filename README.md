# Lovecraft
Experimental natural language program that takes an author's work and breaks it down to parts of speech through a long process (NLTK pos tagging.) After generating a word map, you can mix words using that author's wordspace. Results are similar to a markov chain. Sentence structure and punctuation is preserved, but some words can be shuffled around.

## Facebook integration
main.py has unnecessary code that integrates with Facebook as an example of how this software can be used by publishing results to an arbitrary Facebook page.

## How to use
Using the package is quite simple. You must first have NLTK and gutenberg which can both be installed using pip. For versions above 2.7 you must install bsddb3 for gutenberg as it has been deprecated. You can find the .whl for your version of python from [this unofficial windows binary page](https://www.lfd.uci.edu/~gohlke/pythonlibs/#bsddb3).

### Using your own library
You must first create a directory containing your books in this format:
* Directory
  * Name of book, no extension

Example:
* Lovecraft
  * At the Mountains of Madness

```python
from Lovecraft import Lovecraft
bibliography = Lovecraft(directory="Lovecraft")
```

Simple as that. After a minute it will have broken down every book in the directory into a list of paragraphs, and then each paragraph gets broken down into tuples of (word, part_of_speech).

So, now what?

### The Gutenberg shuffle
For this example, I'll be using the Gutenberg project but it's the samee as the last example for POS tagging. First, choose an author. Check [the Gutenberg project](http://www.gutenberg.org/ebooks/) to find exactly how the author is spelled on the website. In this case we will be using Lovecraft again (Lovecraft, H. P. (Howard Phillips)).

```python
from Lovecraft import Lovecraft

author = "Lovecraft, H. P. (Howard Phillips)"
bilbiography = Lovecraft(author=author)
```

Now this could take a while depending on how many works the author has. Lovecraft only has three, so for testing purposes this is fine. It's now time to shuffle it. First, you must generate a word map for the author. The word map is just a dictionary that categorizes all words by their part of speech.

```python
word_map = bibliography.generate_word_map()
```

Now take a random chunk from a book, and then shuffle it. In this case, we will just use the first book as a sample.
```python
chunk = bibliography.rand_chunk(list(bibliography.books.keys())[0])
print(bibliography.shuffle_chunk(word_map, chunk))
print("That's all, folks")
```

## Tips and tricks
* You can pass a word map from a different author when you shuffle.
* Use multi-threading to speed the tagging process.
* You can choose which parts of speech to skip replacement by changing the ignore list in Lovecraft.shuffle_chunk().
* Gutenberg language by default is English.
* Build the Gutenberg cache before doing anything (process takes a while).
```python
from gutenberg.acquire import get_metadata_cache
cache = get_metadata_cache()
cache.populate()
```
