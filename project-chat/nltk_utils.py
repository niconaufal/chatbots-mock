import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()


def tokenize(sentence):
    """
   pisahkan kalimat menjadi larik kata/token
   token dapat berupa kata atau karakter tanda baca, atau angka
    """
    return nltk.word_tokenize(sentence)


def stem(word):
    """
  stemming = mencari bentuk akar kata
    contoh:
    kata = ["mengatur", "mengatur", "mengatur"]
    kata = [batang (w) untuk w dalam kata-kata]
    -> ["organ", "organ", "organ"]
    """
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """
    mengembalikan tas array kata:
    1 untuk setiap kata yang diketahui yang ada dalam kalimat, 0 sebaliknya
    contoh:
    kalimat = ["halo", "bagaimana", "apakah", "kamu"]
    kata = ["hai", "halo", "aku", "kamu", "sampai jumpa", "terima kasih", "keren"]
    bag   = [  0 ,    1 ,    0 ,   1 ,    0 ,    0 ,      0]
    """
    sentence_words = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words: 
            bag[idx] = 1

    return bag
