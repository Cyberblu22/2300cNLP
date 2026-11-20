"""
Train a Word2Vec model on the Linewise corpus and draw 2D and 3D graphs of
how the words relate.

Run:
    pip install -r requirements.txt
    python build_corpus.py
    python train_word2vec.py

Outputs (in outputs/):
    pca_2d.png               2D PCA projection of the topic words
    tsne_2d.png              2D t-SNE projection (keeps local neighborhoods)
    pca_3d.png               3D PCA projection (static image)
    embedding_3d.html        interactive 3D PCA plot (rotate / zoom / hover)
    similarity_heatmap.png   cosine similarity between selected words
    results.json             training settings, nearest neighbors, analogies,
                             cluster quality numbers
Model (in model/):
    linewise_word2vec.model  the trained gensim model
    linewise_vectors.kv      just the word vectors (KeyedVectors)
"""

import json
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.patheffects as pe
import matplotlib.pyplot as plt
import numpy as np
import plotly.graph_objects as go
from adjustText import adjust_text
from mpl_toolkits.mplot3d import proj3d
from gensim.models import Word2Vec
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
from sklearn.metrics import silhouette_score

from build_corpus import GROUPS, SEED, build

HERE = Path(__file__).resolve().parent
OUT = HERE / "outputs"
MODEL_DIR = HERE / "model"
OUT.mkdir(exist_ok=True)
MODEL_DIR.mkdir(exist_ok=True)

# Brand-adjacent, colorblind-friendly categorical palette (one color per group).
COLORS = {
    "Bug types": "#E8590C",
    "Code constructs": "#2563EB",
    "Review actions": "#0CA678",
    "Languages": "#7048E8",
    "AI tools": "#C2255C",
    "Practice & learning": "#0891B2",
    "Negative feelings": "#868E96",
    "Positive feelings": "#E6A700",
    "Career": "#1E3A8A",
}

PARAMS = dict(
    vector_size=100,   # dimensions per word vector
    window=5,          # words of context on each side
    min_count=3,       # ignore words seen fewer than 3 times
    sg=1,              # 1 = skip-gram (better for small corpora), 0 = CBOW
    negative=10,       # negative samples per positive example
    epochs=40,         # passes over the corpus
    seed=SEED,
    workers=1,         # one worker so results are reproducible
)


def train():
    corpus, n_course, n_gen = build()
    model = Word2Vec(sentences=corpus, **PARAMS)
    model.save(str(MODEL_DIR / "linewise_word2vec.model"))
    model.wv.save(str(MODEL_DIR / "linewise_vectors.kv"))
    stats = {
        "course_sentences": n_course,
        "generated_sentences": n_gen,
        "total_sentences": len(corpus),
        "total_tokens": int(sum(len(s) for s in corpus)),
        "vocabulary_size": len(model.wv),
    }
    return model, stats


def topic_words(wv):
    words, labels = [], []
    for group, ws in GROUPS.items():
        for w in ws:
            if w in wv:
                words.append(w)
                labels.append(group)
    return words, labels


def pretty(w):
    return {"cpp": "c++", "ai": "AI", "llm": "LLM"}.get(w, w.replace("_", " "))


# ---------------------------------------------------------------------------
# Graphs
# ---------------------------------------------------------------------------
def style_axes(ax):
    for side in ("top", "right"):
        ax.spines[side].set_visible(False)
    ax.spines["left"].set_color("#CBD5E1")
    ax.spines["bottom"].set_color("#CBD5E1")
    ax.tick_params(colors="#64748B", labelsize=8)
    ax.grid(True, color="#E2E8F0", linewidth=0.6)
    ax.set_axisbelow(True)


# White outline around labels so they stay readable over grid lines and dots.
HALO = [pe.withStroke(linewidth=2.5, foreground="white")]
LEADER = dict(arrowstyle="-", color="#94A3B8", lw=0.6, shrinkA=0, shrinkB=3)


def place_labels(ax, xs, ys, words, objects, fontsize):
    """Write one label per point, then nudge the labels apart so none overlap.

    Labels that move away from their dot get a thin leader line back to it.
    """
    texts = [ax.text(x, y, pretty(w), fontsize=fontsize, color="#1E293B",
                     zorder=5, path_effects=HALO)
             for x, y, w in zip(xs, ys, words)]
    adjust_text(texts, x=list(xs), y=list(ys), objects=objects, ax=ax,
                expand=(1.15, 1.35), force_text=(0.3, 0.5), force_static=(0.2, 0.4),
                force_pull=(0.005, 0.005), time_lim=10, arrowprops=LEADER)
    return texts


def scatter_2d(points, words, labels, title, subtitle, path, xlabel, ylabel):
    fig, ax = plt.subplots(figsize=(13, 9), dpi=150)
    dots = []
    for group, color in COLORS.items():
        idx = [i for i, l in enumerate(labels) if l == group]
        if not idx:
            continue
        dots.append(ax.scatter(points[idx, 0], points[idx, 1], s=70, color=color,
                               edgecolor="white", linewidth=1.2, label=group, zorder=3))
    style_axes(ax)
    ax.margins(0.08)
    ax.set_xlabel(xlabel, color="#475569")
    ax.set_ylabel(ylabel, color="#475569")
    fig.suptitle(title, x=0.06, ha="left", fontsize=16, fontweight="bold", color="#0F172A")
    ax.set_title(subtitle, loc="left", fontsize=10, color="#64748B", pad=10)
    ax.legend(loc="upper left", bbox_to_anchor=(1.01, 1), frameon=False, fontsize=9,
              title="Topic group", title_fontsize=9)
    fig.tight_layout()
    place_labels(ax, points[:, 0], points[:, 1], words, dots, fontsize=8.5)
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def scatter_3d_png(points, words, labels, explained, path):
    fig = plt.figure(figsize=(13, 10), dpi=150)
    ax = fig.add_subplot(111, projection="3d")
    for group, color in COLORS.items():
        idx = [i for i, l in enumerate(labels) if l == group]
        if not idx:
            continue
        ax.scatter(points[idx, 0], points[idx, 1], points[idx, 2], s=55,
                   color=color, edgecolor="white", linewidth=0.8, label=group,
                   depthshade=True)
    ax.set_xlabel(f"PC1 ({explained[0]:.0%} of variance)", color="#475569", fontsize=9)
    ax.set_ylabel(f"PC2 ({explained[1]:.0%})", color="#475569", fontsize=9)
    ax.set_zlabel(f"PC3 ({explained[2]:.0%})", color="#475569", fontsize=9)
    ax.tick_params(colors="#94A3B8", labelsize=7)
    ax.view_init(elev=22, azim=-58)
    ax.set_title("Word2Vec embeddings in 3D (PCA)", fontsize=15, fontweight="bold",
                 color="#0F172A", loc="left")
    ax.legend(loc="upper left", bbox_to_anchor=(1.02, 0.95), frameon=False, fontsize=9,
              title="Topic group", title_fontsize=9)
    fig.tight_layout()

    # 3D text can't be de-overlapped directly, so project each point to its
    # 2D position on the rendered image and place the labels on a transparent
    # 2D layer drawn on top of the 3D axes.
    fig.canvas.draw()
    xs, ys, _ = proj3d.proj_transform(points[:, 0], points[:, 1], points[:, 2],
                                      ax.get_proj())
    disp = ax.transData.transform(np.column_stack([xs, ys]))
    overlay = fig.add_axes(ax.get_position(), facecolor="none")
    overlay.set_axis_off()
    overlay.set_xlim(0, 1)
    overlay.set_ylim(0, 1)
    xy = overlay.transAxes.inverted().transform(disp)
    dots = overlay.scatter(xy[:, 0], xy[:, 1], s=55, alpha=0)  # obstacles only
    place_labels(overlay, xy[:, 0], xy[:, 1], words, [dots], fontsize=7.5)
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)


def scatter_3d_html(points, words, labels, explained, path):
    fig = go.Figure()
    for group, color in COLORS.items():
        idx = [i for i, l in enumerate(labels) if l == group]
        if not idx:
            continue
        fig.add_trace(go.Scatter3d(
            x=points[idx, 0], y=points[idx, 1], z=points[idx, 2],
            mode="markers+text", name=group,
            text=[pretty(words[i]) for i in idx], textposition="top center",
            textfont=dict(size=11, color="#1E293B"),
            marker=dict(size=6, color=color, line=dict(width=1, color="white")),
            hovertemplate="<b>%{text}</b><br>" + group + "<extra></extra>",
        ))
    axis = dict(backgroundcolor="#F8FAFC", gridcolor="#E2E8F0", zerolinecolor="#CBD5E1",
                showspikes=False)
    fig.update_layout(
        title=dict(text="Linewise Word2Vec: interactive 3D view (drag to rotate)",
                   font=dict(size=18, color="#0F172A")),
        scene=dict(
            xaxis=dict(title=f"PC1 ({explained[0]:.0%})", **axis),
            yaxis=dict(title=f"PC2 ({explained[1]:.0%})", **axis),
            zaxis=dict(title=f"PC3 ({explained[2]:.0%})", **axis),
        ),
        legend=dict(title="Topic group", itemsizing="constant"),
        paper_bgcolor="white", margin=dict(l=0, r=0, t=60, b=0),
        font=dict(family="Inter, system-ui, sans-serif"),
    )
    fig.write_html(path, include_plotlyjs="cdn", full_html=True)


def heatmap(wv, path):
    sample = ["off_by_one", "mutable_default", "race_condition", "deadlock",
              "python", "javascript", "copilot", "chatbot",
              "review", "debug", "anxiety", "shame", "confidence", "relief",
              "interview", "internship", "streak", "snippet"]
    sample = [w for w in sample if w in wv]
    m = np.array([[wv.similarity(a, b) for b in sample] for a in sample])
    fig, ax = plt.subplots(figsize=(11, 9.5), dpi=150)
    im = ax.imshow(m, cmap="Blues", vmin=min(0, m.min()), vmax=1)
    names = [pretty(w) for w in sample]
    ax.set_xticks(range(len(sample)), names, rotation=50, ha="right", fontsize=9)
    ax.set_yticks(range(len(sample)), names, fontsize=9)
    for i in range(len(sample)):
        for j in range(len(sample)):
            ax.text(j, i, f"{m[i, j]:.2f}", ha="center", va="center", fontsize=6.5,
                    color="white" if m[i, j] > 0.6 else "#1E293B")
    ax.set_title("Cosine similarity between word vectors", loc="left", fontsize=15,
                 fontweight="bold", color="#0F172A", pad=12)
    fig.colorbar(im, ax=ax, fraction=0.04, pad=0.02, label="cosine similarity")
    fig.tight_layout()
    fig.savefig(path, bbox_inches="tight", facecolor="white")
    plt.close(fig)


# ---------------------------------------------------------------------------
# Evaluation
# ---------------------------------------------------------------------------
def evaluate(wv, vectors, labels):
    probes = ["off_by_one", "mutable_default", "race_condition", "python",
              "copilot", "debug", "anxiety", "confidence", "interview", "streak"]
    neighbors = {w: [[n, round(float(s), 3)] for n, s in wv.most_similar(w, topn=6)]
                 for w in probes if w in wv}

    analogies = []
    # a is to b as c is to ?  ->  b - a + c
    for a, b, c in [("shame", "pride", "anxiety"),
                    ("python", "javascript", "java"),
                    ("deadlock", "thread", "off_by_one")]:
        if all(x in wv for x in (a, b, c)):
            res = wv.most_similar(positive=[b, c], negative=[a], topn=3)
            analogies.append({"a": a, "b": b, "c": c,
                              "answers": [[w, round(float(s), 3)] for w, s in res]})

    pairs = [("anxiety", "shame"), ("anxiety", "confidence"), ("python", "java"),
             ("python", "anxiety"), ("off_by_one", "range"), ("deadlock", "thread"),
             ("copilot", "chatbot"), ("interview", "internship")]
    similarities = [{"pair": [a, b], "cosine": round(float(wv.similarity(a, b)), 3)}
                    for a, b in pairs if a in wv and b in wv]

    # How well do the topic groups separate? Silhouette in the full 100-d space
    # (cosine distance). Range -1..1, higher = cleaner clusters.
    sil = float(silhouette_score(vectors, labels, metric="cosine"))

    # Average cosine similarity within a group vs. across groups.
    unit = vectors / np.linalg.norm(vectors, axis=1, keepdims=True)
    sims = unit @ unit.T
    lab = np.array(labels)
    same = lab[:, None] == lab[None, :]
    off_diag = ~np.eye(len(lab), dtype=bool)
    within = float(sims[same & off_diag].mean())
    across = float(sims[~same].mean())

    return {
        "nearest_neighbors": neighbors,
        "analogies": analogies,
        "similarities": similarities,
        "cluster_quality": {
            "silhouette_cosine": round(sil, 3),
            "mean_within_group_similarity": round(within, 3),
            "mean_across_group_similarity": round(across, 3),
        },
    }


def main():
    model, stats = train()
    wv = model.wv
    words, labels = topic_words(wv)
    vectors = np.array([wv[w] for w in words])

    pca2 = PCA(n_components=2, random_state=SEED)
    p2 = pca2.fit_transform(vectors)
    ev2 = pca2.explained_variance_ratio_
    scatter_2d(p2, words, labels,
               "Word2Vec embeddings in 2D (PCA)",
               f"{len(words)} topic words from a {PARAMS['vector_size']}-dimension model, "
               f"projected onto the 2 directions of greatest variance",
               OUT / "pca_2d.png",
               f"PC1 ({ev2[0]:.0%} of variance)", f"PC2 ({ev2[1]:.0%} of variance)")

    tsne = TSNE(n_components=2, perplexity=12, metric="cosine", init="pca",
                random_state=SEED, max_iter=2000)
    t2 = tsne.fit_transform(vectors)
    scatter_2d(t2, words, labels,
               "Word2Vec embeddings in 2D (t-SNE)",
               "t-SNE keeps nearby words nearby, so topic clusters stand out. "
               "Distances between clusters are not meaningful.",
               OUT / "tsne_2d.png", "t-SNE dimension 1", "t-SNE dimension 2")

    pca3 = PCA(n_components=3, random_state=SEED)
    p3 = pca3.fit_transform(vectors)
    ev3 = pca3.explained_variance_ratio_
    scatter_3d_png(p3, words, labels, ev3, OUT / "pca_3d.png")
    scatter_3d_html(p3, words, labels, ev3, OUT / "embedding_3d.html")

    heatmap(wv, OUT / "similarity_heatmap.png")

    results = {
        "parameters": {k: v for k, v in PARAMS.items() if k != "workers"},
        "corpus": stats,
        "topic_words_plotted": len(words),
        "pca_explained_variance": {
            "2d": [round(float(x), 3) for x in ev2],
            "3d": [round(float(x), 3) for x in ev3],
        },
        **evaluate(wv, vectors, labels),
    }
    (OUT / "results.json").write_text(json.dumps(results, indent=2), encoding="utf-8")

    print(json.dumps(results["corpus"], indent=2))
    print("cluster quality:", results["cluster_quality"])
    for w, ns in results["nearest_neighbors"].items():
        print(f"  {w:16s} -> " + ", ".join(n for n, _ in ns))
    for a in results["analogies"]:
        print(f"  {a['a']} : {a['b']} :: {a['c']} : {a['answers'][0][0]}")
    print("saved graphs and results to", OUT.relative_to(HERE))


if __name__ == "__main__":
    main()
