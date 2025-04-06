from datasets import load_dataset
from gensim.utils import tokenize

data=load_dataset('imdb')

print(data)
#tokenized_data=tokenize(data)

