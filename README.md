# 2300cNLP
This is for my Intro for NLP course in coolege

## Word2Vec model

A trained Word2Vec model on the project's subject (reading and debugging AI-generated code), with 2D and 3D graphs of how the words relate. See [`word2vec/`](word2vec/README.md): a results page, a notebook walkthrough, the training scripts and the saved model. On the deployed site it's at `/word2vec/`.

## Linewise landing page

A landing page for **Linewise**, a made-up product from a class exercise: free daily practice reading, reviewing and debugging flawed AI-generated code. It's built from the Part 4 landing page PRD and the Part 3 brand and design system in the course prompt chain.

### Files

| File | What it is |
|---|---|
| `index.html` | The page: nav, hero, problem, solution, how it works, features, live demo, pricing + FAQ, languages and privacy, final CTA, footer |
| `styles.css` | Design tokens (colors, type, radius, motion), light and dark themes, responsive layout |
| `script.js` | Theme toggle, mobile menu, scroll reveals, and the interactive "Try today's snippet" demo |
| `favicon.svg` | Logo mark |
| `netlify.toml` | Netlify config (static site, no build step) |

No framework and no build step: plain HTML, CSS and JavaScript, so it deploys straight to Netlify.

### Run locally

Open `index.html` in a browser, or serve the folder:

```bash
python3 -m http.server 8000
```

### Deploy to Netlify

1. In Netlify, choose **Add new site → Import an existing project** and pick this GitHub repo.
2. Branch: `main`. Build command: leave empty. Publish directory: `.` (the `netlify.toml` already sets this).
3. Deploy.

### Notes

- The statistics (66%, 45%, 33%) are real, from the Stack Overflow 2025 Developer Survey, and link to their source.
- There are no invented testimonials, user counts or ratings. The streak and heatmap visuals are labeled as illustrations.
- It respects `prefers-reduced-motion` and `prefers-color-scheme`. The demo works with the keyboard (arrow keys, Space, Enter) and screen readers.
