import random
import json

import torch

from model import NeuralNet
from nltk_utils import bag_of_words, tokenize

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

with open('hasil.json', 'r') as dataku:
    intents = json.load(dataku)

FILE = "dokumen.pth"
dokumen = torch.load(FILE)

input_size = dokumen["input_size"]
hidden_size = dokumen["hidden_size"]
output_size = dokumen["output_size"]
all_words = dokumen['all_words']
tags = dokumen['tags']
model_state = dokumen["model_state"]

model = NeuralNet(input_size, hidden_size, output_size).to('cpu')
model.load_state_dict(model_state)
model.eval()

bot_name = "Nico"

def get_response(msg):
    sentence = tokenize(msg)
    X = bag_of_words(sentence, all_words)
    X = X.reshape(1, X.shape[0])
    X = torch.from_numpy(X).to('cpu')

    output = model(X)
    _, predicted = torch.max(output, dim=1)

    tag = tags[predicted.item()]

    probs = torch.softmax(output, dim=1)
    prob = probs[0][predicted.item()]
    if prob.item() > 0.89:
        for intent in intents['intents']:
            if tag == intent["tag"]:
                return random.choice(intent['responses'])
    return "Silahkan Bertanya Di Kolom Komentar..."



if __name__ == "__main__":
    print("Mari berbincang! (ketik 'keluar' untuk keluar)")
    while True:
        sentence = input("Kamu: ")
        if sentence == "keluar":
            break

        resp = get_response(sentence)
        print(resp)



