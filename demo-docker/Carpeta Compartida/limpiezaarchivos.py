## Limpieza de archivos con Python y Pandas

import pandas as pd

x = pd.Series(
  [
    'Juan D. Velasquez',
    'Juan D Velasquez',
    'Velasquez, Juan D',
    'Velasquez Juan',
    'car',
    'cars',
    'run',
    'running',
  ]
)

x

## --------


def fingerprint(x):
    if x is None:
        return None
    x = x.strip().lower()
    x = re.sub("-", " ", x)
    x = re.sub("[" + string.punctuation + "]", "", x)
    x = remove_accents(x)
    x = sorted(set([s.stem(word) for word in x.split()]))
    return " ".join(x)
    
    
    
## -------

from nltk.stem import PorterStemmer
import re
import string


def stemmer_porter(x):
    if x is None:
        return None
    x = x.strip().lower()
    x = re.sub("-", " ", x)
    x = re.sub("[" + string.punctuation + "]", "", x)
    x = remove_accents(x)
    s = PorterStemmer()
    x = sorted(set([s.stem(word) for word in x.split()]))
    return " ".join(x)

stemmer_porter("  hola, mundo-MUNDOS !!! CRUEL¿¿¿.  ")



## --------

import unicodedata

def remove_accents(text):
    text = unicodedata.normalize('NFD', text)
    text = text.encode('ascii', 'ignore')
    text = text.decode('utf-8')
    return str(text)

remove_accents('áéíóúñÁÉÍÓÚN')


 #
    # x : es una serie de pandas
    #
    
    x = x.dropna()
    def text_clustering(x, name_strategy="mostfrequent", key="porter"):
    x = x.map(lambda w: w.strip())
    x = x.unique()

    x = pd.DataFrame({'col': x.tolist()})

    # if key == 'fingerprint':
    #     f = fingerprint
    # else:
    #     f = stemmer_porter

    f = {
        "fingerprint": fingerprint,
         "porter": stemmer_porter,
    }[key]

    x['key'] = x.col.map(f)

    grp = x.groupby(by='key').agg({"col": list})
    grp["listlen"] = grp.col.map(len)
    grp = grp[ grp.listlen > 1 ]

    grp['col'] = grp.col.map(lambda w: pd.Series(w))
    grp["groupname"] = None

    if name_strategy is None:
        name_strategy = "mostfrequent"

    if name_strategy == "mostfrequent":
        grp["groupname"] = grp.col.map(
            lambda w: w.value_counts()[w.value_counts() == w.value_counts().max()]
            .sort_index()
            .index[0]
        )

    if name_strategy == 'longest':
        grp["groupname"] = grp.col.map(
            lambda w: sorted(w.tolist(), key=len, reverse=True)[0]
        )

    if name_strategy == 'shortest':
        grp["groupname"] = grp.col.map(
            lambda w: sorted(w.tolist(), key=len, reverse=False)[0]
        )

    return {key: sorted(value.tolist()) for key, value in zip(grp.groupname, grp.col)}


text_clustering(x)

## ------