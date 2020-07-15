import nlpaug.augmenter.word as naw
import nltk
import os

def get_input():
    txt = input("Text to be augmented: ")
    num_iter  = input("data augmentation size: ")
    return txt, int(num_iter)

def print_header(text):
    print("Original:")
    print(text)
    print("Augmented Text:")

def data_generation(text):
    aug = naw.SynonymAug(aug_src='wordnet')
    augmented_text = aug.augment(text)
    return augmented_text

def check_repetition(text, samples):
    if text.replace(" ","") not in samples:
        samples[text.replace(" ","")]=0
        print(text)