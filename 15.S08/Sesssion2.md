# Outlines
Text Processing
RE
NLP Basics

# Notations
Corpus: collections of documents
document: unit 
Sentence
Word/Token
character


# String Operations
.upper .lower .count()
'--'.join(list)

## encodings:
ASCII, Unicode (UTF-8, default in Python 3, 95% of websites)

# Read/Write Local Files
```python
with open('sample_text.txt', 'w') as f:
    f.write("Sally sells sea shells on the sea shore.\nTom does not.\n\nThe new iPhone has 6 cameras.\nAnalysts are ecstatic.")
    
with open('sample_text.txt', 'r') as f:
    corpus = f.read()
print(corpus)

all_items = []
for doc in corpus.split('\n\n'):
    sentences = doc.split('\n')
    all_items.append(sentences)
all_items

import json
with open('sample_text.json') as f:
    doc = json.load(f)
print(doc['text'])
```

# Pandas in NLP: text + metadata (csv)
.str.split() #list of words


# Remote files: requests
res = requests.get(url)
res.text
pd.read_html
sklearn.datasets

# Regex
.match to match full pattern, where something is
```py
for m in re.finditer(r'iphone .', 'apple produces the iphone 8 and the iphone x.'):
    print('found match starting at:', m.start())
```
re split for splitting text based on rules

.+\-.+   two words connected by dash
{a-zA-Z}+\-{a-zA-Z}+       +at least once

```py
regex_ptn = r'was acquired by|purchased'
for _, row in wiki_df.iterrows():
    m = re.search(regex_ptn, row['intro_text'])
    if m:
        print(row['intro_text'][m.start()-20:m.end()+20])
```

# NLP Basics
word counts re find all wordss [a-z]+

## stemming - truncate to root
```py
from nltk.stem.porter import PorterStemmer
stemmer = PorterStemmer()
print(stemmer.stem('doing'))
# fails for does and went
# simple rules, need to find actual word root
```
wordnet: dictionary of basic word information, stuctured information (hyponyms, similarity... )
limited in size...frozen in time...
nltk.stem.WordNetLemmatizer()

## Concept: n-grams
chaining multiple tokens together: explode vocabulary size
'New York' & 'in New'?
## Bag of words
unordered, structured representation of ngrams per documents

## Sparse matrix (count of words)
scipy.sparse.csr
.todense()

# from sklearn.feature_extraction.text import CountVectorizer

# How we improve apple > the? TF-IDF
probability distribution?
Term Frequency-Inverse document frequency

the importance of a word in a document relative to the overall ubiquity of the word across the corpus

downweight common words
