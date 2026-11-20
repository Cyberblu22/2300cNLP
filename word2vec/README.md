# Linewise Word2Vec model

A Word2Vec model trained on the subject of the class project: **reading, reviewing and debugging AI-generated code** (the Linewise concept). It includes 2D and 3D graphs that show how the words relate.

- **Results page:** `index.html` in this folder (on the Netlify site, it's served at `/word2vec/`)
- **Notebook walkthrough:** `Word2Vec_Linewise.ipynb` (GitHub shows it with its outputs)

## What's in this folder

| Path | What it is |
|---|---|
| `build_corpus.py` | Builds the training text: the real course document plus generated sentences about the same subject |
| `train_word2vec.py` | Trains the model, draws the graphs, and writes the evaluation results |
| `data/course_prompt_chain.md` | The real course document (avatar, diary entries, brand system, landing page PRD) |
| `data/corpus.txt` | The final tokenized corpus, one sentence per line |
| `model/linewise_word2vec.model` | The trained gensim model (can keep training) |
| `model/linewise_vectors.kv` | Only the word vectors (smaller, read-only) |
| `outputs/pca_2d.png` | 2D graph (PCA) |
| `outputs/tsne_2d.png` | 2D graph (t-SNE) |
| `outputs/pca_3d.png` | 3D graph (static image) |
| `outputs/embedding_3d.html` | 3D graph (interactive: drag to rotate, scroll to zoom, hover for words) |
| `outputs/similarity_heatmap.png` | Cosine similarity between selected words |
| `outputs/results.json` | Training settings, nearest neighbors, analogies, cluster quality |

## How it works

Word2Vec turns every word into a list of 100 numbers (a vector). It learns the vectors by reading the text and predicting the words that appear around each word. This model uses the **skip-gram** version. Words that show up in similar contexts end up with similar vectors, so related words sit close together in the graphs.

### Training data

1. **The real course document** (618 sentences). It is repeated 3 times so it carries weight next to the generated text.
2. **5,040 generated sentences** built from templates about the subject. They cover bug types, code constructs, review actions, programming languages, AI tools, practice habits, the feelings from the avatar research, and careers.

The generated sentences are **synthetic**. They exist because about 8,000 words of real text is too little to train stable vectors. The templates place each topic's words in similar contexts, which is a big reason the topic clusters come out so clean.

Total: 6,894 sentences, 61,623 tokens, and a vocabulary of 1,943 words.

### Settings

| Setting | Value | Meaning |
|---|---|---|
| `vector_size` | 100 | Numbers per word vector |
| `window` | 5 | Words of context on each side |
| `min_count` | 3 | Words seen fewer than 3 times are ignored |
| `sg` | 1 | Skip-gram (works better than CBOW on small corpora) |
| `negative` | 10 | Negative samples per training example |
| `epochs` | 40 | Passes over the corpus |
| `seed` / `workers` | 42 / 1 | Fixed, so results are reproducible |

## Results

**Nearest neighbors** (the most similar words by cosine similarity):

| Word | Closest words |
|---|---|
| off_by_one | race_condition, deadlock, null_pointer, mutable_default, infinite_loop |
| python | rust, javascript, cpp, java, typescript |
| copilot | autocomplete, llm, hallucinated, chatbot, prompt |
| debug | inspect, review, verify, trace, flag |
| anxiety | doubt, panic, stress, fear, shame |
| confidence | relief, pride, calm, joy, earned |
| interview | internship, resume, recruiter, summer, career |

**Analogies** (a : b :: c : ?):
- shame : pride :: anxiety : **joy** (a negative feeling maps to a positive one)
- python : javascript :: java : **cpp** (one language maps to another)
- deadlock : thread :: off_by_one : **shared** (weak; the corpus is too small for this kind of relation)

**Cluster quality:** the silhouette score is 0.512 (on a scale from -1 to 1, higher means cleaner clusters). The average similarity between words in the same topic is 0.729, against 0.377 for words in different topics.

## Run it yourself

```bash
cd word2vec
```

```bash
pip install -r requirements.txt
```

```bash
python build_corpus.py
```

```bash
python train_word2vec.py
```

Load the trained model in Python:

```python
from gensim.models import Word2Vec
model = Word2Vec.load("model/linewise_word2vec.model")
model.wv.most_similar("debug")
```

## Limitations

- The corpus is small, and most of it is template-generated, so the model learns the topic groups well but finer relations only weakly (see the third analogy).
- Small tokenizer quirk: plural phrases such as "mutable defaults" become their own token (`mutable_defaults`) instead of joining `mutable_default`, and identifiers like `add_item` in the course text are split into separate words. Fixing this moves the results by about 0.01, so it was left as-is.
- PCA keeps only part of the variance in 2 or 3 dimensions (the axis labels on each graph give the percentages). t-SNE keeps neighbors together, but the distances between clusters don't mean anything.

*Linewise is a concept created for a class exercise.*
