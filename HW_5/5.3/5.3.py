import string

text = input("Enter a string: ")


def make_hashtag(text):
    for ch in string.punctuation:
        text = text.replace(ch, "")

    words = text.split()

    words = [word.capitalize() for word in words]

    hashtag = "#" + "".join(words)

    return hashtag[:140]


print(make_hashtag(text))
