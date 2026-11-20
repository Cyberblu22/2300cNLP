"""
Build the training corpus for the Linewise Word2Vec model.

The subject of the course project is Linewise: daily practice in reading,
reviewing and debugging flawed AI-generated code. The corpus has two parts:

1. data/course_prompt_chain.md
   The real course document (avatar, diary entries, brand system, PRD).
   About 8,000 words. On its own it's too small to train stable vectors.

2. Generated domain sentences
   Sentences made from templates about the same subject: bug types, code
   constructs, review actions, programming languages, AI assistants,
   learning habits and the emotions in the avatar research. Each template
   puts words from a topic into realistic contexts, so words that are used
   the same way end up with similar vectors. That is the distributional
   hypothesis Word2Vec is built on.

The generated text is synthetic. It exists to give the model enough
examples; it is not real user data.

Output: data/corpus.txt with one tokenized sentence per line.
"""

import random
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE / "data"
SEED = 42

# Multi-word terms are joined with underscores so the model treats each one
# as a single token (e.g. "off by one" -> "off_by_one").
PHRASES = {
    "off by one": "off_by_one",
    "off-by-one": "off_by_one",
    "mutable default": "mutable_default",
    "null pointer": "null_pointer",
    "race condition": "race_condition",
    "memory leak": "memory_leak",
    "infinite loop": "infinite_loop",
    "type error": "type_error",
    "stack overflow": "stack_overflow",
    "code review": "code_review",
    "pull request": "pull_request",
    "unit test": "unit_test",
    "edge case": "edge_case",
    "c++": "cpp",
    "impostor syndrome": "impostor_syndrome",
    "imposter syndrome": "impostor_syndrome",
}

# ---------------------------------------------------------------------------
# Vocabulary groups. These are also the clusters the graphs color by.
# ---------------------------------------------------------------------------
GROUPS = {
    "Bug types": [
        "off_by_one", "mutable_default", "null_pointer", "race_condition",
        "memory_leak", "infinite_loop", "type_error", "deadlock", "overflow",
        "normalization",
    ],
    "Code constructs": [
        "loop", "function", "variable", "list", "index", "argument",
        "parameter", "array", "dictionary", "condition", "return", "class",
    ],
    "Review actions": [
        "read", "review", "trace", "flag", "inspect", "explain", "debug",
        "spot", "catch", "verify",
    ],
    "Languages": ["python", "javascript", "java", "cpp", "typescript", "rust"],
    "AI tools": [
        "ai", "assistant", "chatbot", "copilot", "llm", "prompt", "generated",
        "hallucinated", "autocomplete",
    ],
    "Practice & learning": [
        "practice", "streak", "daily", "snippet", "coach", "feedback",
        "hint", "lesson", "habit", "progress",
    ],
    "Negative feelings": [
        "anxiety", "shame", "overwhelm", "fear", "panic", "frustration",
        "doubt", "stress",
    ],
    "Positive feelings": [
        "confidence", "pride", "relief", "clarity", "calm", "focus",
        "trust", "joy",
    ],
    "Career": [
        "interview", "internship", "job", "recruiter", "resume", "offer",
        "hiring", "career",
    ],
}

# Short descriptions that give each bug type its own neighbors.
BUG_DETAILS = {
    "off_by_one": ["range", "index", "boundary", "first", "last", "element"],
    "mutable_default": ["argument", "shared", "list", "default", "call", "state"],
    "null_pointer": ["missing", "none", "reference", "object", "crash", "empty"],
    "race_condition": ["thread", "concurrent", "timing", "shared", "lock", "async"],
    "memory_leak": ["allocation", "free", "heap", "resource", "growing", "cleanup"],
    "infinite_loop": ["loop", "condition", "never", "exit", "counter", "hang"],
    "type_error": ["string", "integer", "cast", "type", "convert", "mismatch"],
    "deadlock": ["lock", "thread", "waiting", "mutex", "blocked", "concurrent"],
    "overflow": ["integer", "limit", "large", "boundary", "wrap", "number"],
    "normalization": ["lowercase", "case", "email", "strip", "compare", "key"],
}

TEMPLATES = {
    "Bug types": [
        "the ai generated code has a subtle {w} bug",
        "she found a {w} hiding in the snippet",
        "a {w} is a common bug in generated code",
        "the coach explained why the {w} breaks the function",
        "today the hidden bug was a {w}",
        "reading slowly helps you catch a {w}",
        "the {w} made the tests pass but the output wrong",
        "this {w} bug involves the {d1} and the {d2}",
        "a {w} usually comes from the {d1} or the {d2}",
        "look at the {d1} to find the {w}",
    ],
    "Code constructs": [
        "trace each {w} line by line",
        "the {w} on line {n} looks fine at first",
        "check what the {w} returns",
        "the bug is in the {w} not the {w2}",
        "read the {w} and the {w2} together",
        "the ai renamed the {w} without telling you",
        "every {w} in the snippet has a purpose",
    ],
    "Review actions": [
        "you {w} the code before you trust it",
        "students {w} one snippet every day",
        "learn to {w} ai generated code carefully",
        "she can {w} the function line by line now",
        "the goal is to {w} the bug before it ships",
        "first {w} the snippet then {w2} the bug",
        "a good reviewer will {w} every line",
    ],
    "Languages": [
        "today the snippet is written in {w}",
        "she is learning {w} in her class",
        "the ai wrote the function in {w}",
        "practice reading {w} code every day",
        "the {w} snippet had a hidden bug",
        "{w} and {w2} are both supported languages",
        "switch the daily language from {w} to {w2}",
    ],
    "AI tools": [
        "the {w} wrote code that looks clean but is wrong",
        "do not trust the {w} output blindly",
        "she pasted the error back into the {w}",
        "{w} code is almost right but not quite",
        "the {w} gave a confident answer that was wrong",
        "use the {w} and still be able to check it",
        "most developers use an {w} but few trust it",
    ],
    "Practice & learning": [
        "the {w} takes about ten minutes",
        "keep your {w} going every morning",
        "a daily {w} builds real skill",
        "the {w} helps students improve at reading code",
        "one {w} a day compounds over weeks",
        "her {w} grew after six weeks of practice",
        "the {w} and the {w2} keep her learning",
    ],
    "Negative feelings": [
        "she felt {w} when she could not explain the code",
        "the interview filled her with {w}",
        "{w} grows when you paste code you do not understand",
        "late at night the {w} came back",
        "her {w} and {w2} made it hard to sleep",
        "debugging loops cause {w}",
        "the frozen interview left her with {w}",
    ],
    "Positive feelings": [
        "she felt {w} when she found the bug",
        "daily practice replaced fear with {w}",
        "reading line by line brings {w}",
        "her {w} grew with every snippet",
        "finding the bug gave her {w} and {w2}",
        "earned {w} lasts longer than borrowed answers",
        "the coach helped her find {w}",
    ],
    "Career": [
        "she wants to pass the technical {w}",
        "the {w} asked her to walk through the function",
        "practice reading code before the {w}",
        "a strong {w} needs real debugging skill",
        "she got the {w} after explaining the bug",
        "the {w} and the {w2} both matter to her",
        "reading code is the skill that wins the {w}",
    ],
}

# Cross-topic sentences tie the groups together the way the subject does
# (feelings change with practice, AI produces bugs, and so on).
BRIDGES = [
    "the {ai} generated a {bug} and she felt {neg}",
    "after a month of {prac} her {neg} turned into {pos}",
    "she had to {act} the {lang} snippet to find the {bug}",
    "the {ai} wrote a {con} with a {bug}",
    "in the {car} she had to {act} the {con}",
    "daily {prac} helps you {act} {ai} code with {pos}",
    "the {bug} in the {lang} {con} was easy to {act} after practice",
    "without {prac} the {car} brought {neg}",
    "with {prac} the {car} brought {pos}",
]


def tokenize(text: str) -> list[str]:
    text = text.lower()
    for phrase, token in PHRASES.items():
        text = text.replace(phrase, token)
    # Keep letters, digits, underscores and "+" (for c++ before replacement).
    return re.findall(r"[a-z][a-z0-9_]*", text)


def course_sentences() -> list[list[str]]:
    """Split the real course document into tokenized sentences."""
    raw = (DATA / "course_prompt_chain.md").read_text(encoding="utf-8")
    raw = re.sub(r"```.*?```", " ", raw, flags=re.S)       # drop code blocks
    raw = re.sub(r"https?://\S+", " ", raw)                # drop URLs
    raw = re.sub(r"[#*>|`_\-]{1,}", " ", raw)              # markdown symbols
    parts = re.split(r"(?<=[.!?])\s+|\n+", raw)
    sents = [tokenize(p) for p in parts]
    return [s for s in sents if len(s) >= 4]


def generated_sentences(rng: random.Random, per_template: int = 60) -> list[list[str]]:
    sents = []
    for group, templates in TEMPLATES.items():
        words = GROUPS[group]
        for tpl in templates:
            for _ in range(per_template):
                w, w2 = rng.sample(words, 2)
                fill = {"w": w, "w2": w2, "n": rng.randint(2, 20)}
                if group == "Bug types":
                    d1, d2 = rng.sample(BUG_DETAILS[w], 2)
                    fill.update(d1=d1, d2=d2)
                sents.append(tokenize(tpl.format(**fill)))

    pick = lambda g: rng.choice(GROUPS[g])
    for tpl in BRIDGES:
        for _ in range(per_template * 2):
            sents.append(tokenize(tpl.format(
                ai=pick("AI tools"), bug=pick("Bug types"),
                neg=pick("Negative feelings"), pos=pick("Positive feelings"),
                prac=pick("Practice & learning"), act=pick("Review actions"),
                lang=pick("Languages"), con=pick("Code constructs"),
                car=pick("Career"),
            )))
    return sents


def build() -> list[list[str]]:
    rng = random.Random(SEED)
    course = course_sentences()
    generated = generated_sentences(rng)
    # Repeat the real document a few times so its contexts carry weight
    # next to the larger generated set.
    corpus = course * 3 + generated
    rng.shuffle(corpus)
    return corpus, len(course), len(generated)


if __name__ == "__main__":
    corpus, n_course, n_gen = build()
    out = DATA / "corpus.txt"
    out.write_text("\n".join(" ".join(s) for s in corpus) + "\n", encoding="utf-8")
    n_tokens = sum(len(s) for s in corpus)
    print(f"course sentences:    {n_course}")
    print(f"generated sentences: {n_gen}")
    print(f"total sentences:     {len(corpus)} ({n_tokens:,} tokens)")
    print(f"wrote {out.relative_to(HERE)}")
