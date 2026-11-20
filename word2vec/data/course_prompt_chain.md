# Linewise: Complete NLP Course Prompt Chain

> A class exercise for an intro NLP course: a chain of prompts, each building on the last. "Linewise" is a made-up product, a free daily practice for reading, reviewing and debugging flawed AI-generated code. The business name, gradient and product details were invented for this exercise. The only real data is the cited Stack Overflow survey figures.

## Contents

1. Part 1: Problem Aware Customer Avatar
2. Part 2: Diary Entries (Before, During, After)
3. Part 3: Brand Identity & Design System
4. Part 4: Landing Page PRD (adapted from template)
5. Part 5: Landing Page (built from the PRD)
6. Part 6: Critique of the Original PRD Template

---

# Part 1: Problem Aware Customer Avatar

## Prompt used

> Research five customer avatars for an offer about [practicing with reading, reviewing, editing, or debugging poorly AI generated/prompted code]. The avatars will be based off of the Stages of Market Awareness as taught by Eugene Schwartz in his book Breakthrough Advertising. Even though you are researching 5 stages, I only want the Problem Aware Avatar.
>
> Stages: Unaware, Problem Aware, Solution Aware, Product Aware, Most Aware.
>
> The audience is [Students or Professional Programmers] [that have an interest in improving their AI assistant's code quality]. It's a [Free service] [you will be practicing a minimum once a day with] that helps [primarily students] [in code reading comprehension].
>
> Format: sections A (Who Are They) through H (Empathy Map). At least 1000 words.

## Research grounding

Based on the Stack Overflow 2025 Developer Survey (via InfoWorld and other reports):

- 84% of developers use or plan to use AI in their workflow (up from 76% in 2024), but only 33% trust the accuracy of AI output.
- 66% say their top AI frustration is "AI solutions that are almost right, but not quite."
- 45% say debugging AI-generated code takes more time than expected.

Source: https://www.infoworld.com/article/4031673/

## Stage of Awareness: Problem Aware

*She knows something is wrong. She can't confidently read, review or debug the code her AI assistant gives her. She doesn't yet know that daily practice exists to fix this. She thinks the answer is "better prompts" or "just grinding harder."*

### A → Who Are They

- **Name:** Maya Rodriguez
- **Gender:** Female
- **Job:** Junior-year Computer Science student; part-time IT help desk assistant at her university
- **Household Income:** About $28,000/year (her part-time wages plus some family support)
- **Marital Status:** Single, in a long-distance relationship
- **Education Level:** Working on a BS in Computer Science, with an expected graduation in 18 months

### B → What They Do & Like

- **Top 3 Brands They Wear:** Uniqlo, Nike, Champion
- **1–2 Hobbies:** Indie video games (especially Stardew Valley and Hades) and short-form tech content on YouTube
- **Top 5 Favorite Movies:** *The Social Network*, *Hidden Figures*, *Spider-Man: Into the Spider-Verse*, *The Imitation Game*, *Interstellar*
- **Top 5 Favorite Books:** *Atomic Habits* (James Clear), *Cracking the Coding Interview* (Gayle Laakmann McDowell), *Clean Code* (Robert C. Martin, which she bought but never finished), *Project Hail Mary* (Andy Weir), *The Pragmatic Programmer* (Hunt & Thomas)
- **Top 5 Visited Websites:** ChatGPT or Claude, GitHub, Stack Overflow, Reddit (r/cscareerquestions, r/learnprogramming), LeetCode
- **Top 5 Relevant Social Media Influencers:** Fireship, ThePrimeagen, NeetCode, Theo (t3.gg), Tech With Tim

### C → Why Are They

- **Main Personality Traits:** Conscientious, anxious overachiever, curious, a little perfectionist, quietly competitive, slow to ask for help in public
- **5 Major Values They Hold:** Competence, honesty (she hates feeling like a fraud), financial independence, making her family proud, continuous learning
- **2 Major Life Victories:**
  1. First in her family to attend a four-year university, on a partial scholarship
  2. Built and deployed a full-stack class project (a study-group scheduler) that her professor praised in front of the class
- **2 Major Life Failures:**
  1. Froze during a live technical interview for a summer internship when asked to explain code she had "written" with AI help, and didn't get the offer
  2. Failed a data structures midterm after relying on AI for homework all semester, then had to retake the course

### D → Smart Market Questions

- **What keeps them awake at night:** "If someone asked me to walk through my own GitHub projects line by line, could I actually do it?" She replays the frozen interview and wonders whether she's learning to program or learning to copy and paste.
- **What are they secretly afraid of:** That she's an impostor who will be "found out" on her first job, and that AI will replace entry-level developers like her before she ever gets real experience.
- **What are they angry about, and who at:** She's angry at the AI tools for confidently giving her broken code. She's angry at her school for teaching 2015-style assignments while everyone uses AI in 2026. She's angry at hiring managers who ask for "2 years of experience" for junior roles. Underneath it all, she's angry at herself for taking shortcuts.
- **Top 3 Daily Frustrations:**
  1. AI code that runs but gives subtly wrong results, and she can't figure out why
  2. Spending an hour debugging something the AI wrote in 10 seconds
  3. Reading other people's code (or AI code) feels like reading a foreign language at half speed
- **Biggest Secret Desire:** To be the person on the team others come to when something breaks, the one who "just sees it."
- **Built-in Decision Bias:** Social proof and peer validation. If a respected YouTuber or a classmate she admires uses something, she'll try it. She's also strongly drawn to anything free and low-commitment, because she has little money and little time.
- **Common Words or Language:** "vibe coding," "it works on my machine," "AI slop," "hallucinated," "skill issue," "I'm cooked," "imposter syndrome," "grind LeetCode," "cracked engineer," "fundamentals"
- **Top 3 Complaints About Existing Solutions:**
  1. LeetCode trains her to *write* clever algorithms, but her real problem is *reading* and *judging* code
  2. Tutorials and courses are long and passive, so she watches 3 hours and retains nothing
  3. Asking the AI to explain its own code just produces more confident text she can't verify

### E → Going Deep

- **Top 3 Dominant Negative Emotions:** Anxiety, shame, overwhelm
- **Top 3 Dominant Positive Emotions From Solving This Problem:** Confidence, pride, relief
- **Top 3 Beliefs About the World:**
  1. "The job market is brutal and only the best juniors get hired."
  2. "AI is here to stay, so I have to learn to work with it, not against it."
  3. "Hard work beats talent, but only if you work on the right things."
- **Biggest Lifestyle Desire:** A stable, well-paid remote or hybrid software job that lets her support her family, pay off loans, and stop feeling like she's always behind.

### F → Purchasing Habits

- **Top 3 Decision Triggers:**
  1. A peer or influencer she trusts recommends it
  2. It's free, or has a generous free tier
  3. It promises quick, visible progress (a streak, a score, a "level up")
- **Prior Purchases For This Pain:** A discounted Udemy course on "Clean Code in Python" (never finished), a ChatGPT Plus subscription she pays for some months, a LeetCode Premium trial she cancelled, a used copy of *Clean Code*
- **Price Tolerance For Offer:** $0 to start. She'd pay $5–10/month for a premium tier only after seeing clear improvement. Since this offer is free, the cost she's weighing is time, not money.
- **Time Horizon of Solution:** She wants to *feel* progress within 2 weeks and be "interview-ready" within 3–6 months, before internship and new-grad recruiting season.

### G → Primary Wants

- **Wants to gain:** The ability to read unfamiliar code quickly, spot bugs in AI output, and explain code clearly in interviews
- **Wants to be:** A "real" developer who's competent and trusted, not someone who just prompts AI
- **Wants to do:** Pass technical interviews, land an internship or first job, and contribute confidently to team code reviews
- **Wants to save:** Time (hours lost to debugging), money (no expensive bootcamps), and face (no more freezing in front of interviewers)
- **Wants to avoid:** Being exposed as a fraud, failing another class, shipping AI-generated bugs at her first job, and being left behind by AI

### H → Empathy Map

- **Seeing:** Classmates bragging about shipping apps "in a weekend with Cursor," LinkedIn posts about layoffs and "AI replacing juniors," job listings requiring experience she doesn't have, and her own repos full of code she half-understands.
- **Thinking:** "Everyone else seems to get this. Why can't I read code as fast as they do? Am I actually learning anything? Maybe I'm just not cut out for this."
- **Hearing:** Professors saying "understand the fundamentals," influencers saying "AI makes you 10x," senior devs online saying "juniors can't debug anymore," and her parents asking when she'll get a job.
- **Feeling:** Stressed, behind, and secretly ashamed, but still motivated and hopeful that there's a way to fix this if she can find it.
- **Saying:** "I'm cooked for this exam." "The AI wrote it, I just tweaked it." "I need to get better at debugging." "I don't even know where to start."
- **Doing:** Pasting error messages back into ChatGPT in loops, rewatching YouTube tutorials late at night, doing occasional LeetCode problems, and avoiding group code reviews so nobody sees her uncertainty.

*Why she's Problem Aware:* Maya can name her pain ("I can't really read or debug AI code"), but she hasn't heard of structured daily code-reading practice as a solution. Messaging for her should open by naming that pain and validating it. It shouldn't lead with the product.

---

# Part 2: Diary Entries

## Prompt used

> You are highly introspective and love to journal. Take all of the output from the problem aware avatar above, and write me a diary entry from the perspective of that avatar. Focus on their dominant negative emotions. Use visual words & writing, be visceral, be emotional, and be creative. I want one entry for each scenario: Before Using the Product, During Their First Use of Product, After Using The Product.

## Maya's Journal

### Entry 1: Before Using the Product

**Tuesday, 1:47 a.m.**

The ceiling fan is doing that wobble again, *tick, tick, tick*, like a clock counting down to something I can't see.

I can't sleep. My laptop is still open on the desk, and the screen throws this pale blue light across the room, so everything looks like it's underwater. My data structures assignment is technically done. It runs. The tests pass. Green checkmarks all the way down.

And I feel sick.

I don't know why it works. I asked the AI to "fix the linked list traversal," and it gave me forty lines back. I pasted them in and they worked, and I sat there staring at them like they were written in Russian. There's a `while` loop with a condition I'd never write. There's a variable called `prev_ptr_tmp` that comes out of nowhere. I traced it with my finger on the screen and lost my place twice.

I keep thinking about the interview. That's the real reason I'm awake. I can still feel the heat crawling up my neck when he said, *"Walk me through this function you wrote."* I can still see my own face reflected in the Zoom window, mouth slightly open, eyes darting like a trapped animal. Fourteen seconds of silence. I counted them afterward. Fourteen seconds is forever.

*"I wrote it."* I didn't, though. Not really.

The shame isn't a thought. It's physical. It sits in my stomach like a cold, wet stone, and it gets heavier every time someone in the group chat says something like *"lol just shipped my app in 6 hours with Cursor."* Everyone else seems to be sprinting, and I'm standing still with my shoes glued to the floor.

My mom texted today asking how school's going. I sent a thumbs up. A thumbs up! I couldn't figure out how to type *"I think I might be a fraud"* to the woman who worked double shifts so I could be here.

I opened LeetCode for twenty minutes tonight. Solved one easy problem. Felt nothing. Because that's not my problem, is it? I can sort of *write* code. What I can't do is *read* it. I can't look at a block of someone else's logic and *see* what it's doing, the way the seniors on Reddit seem to. They glance at code and the bug just jumps out at them, like a red thread in a white sweater.

When I look at code, it's all white sweater.

I don't even know what to Google. "How to read code better"? It feels like asking how to have better eyesight.

Tick, tick, tick.

I'm cooked.

---

### Entry 2: During Their First Use of the Product

**Thursday, 7:12 a.m.**

Okay. Writing this on the bus because my hands are still a little shaky and I want to remember exactly how this felt.

Priya from my algorithms class sent me a link last night. It's a free site where you get one snippet of AI-generated code a day, and your job is to *find what's wrong with it.* No writing. Just reading. She said, *"it's humbling but it helps."* I almost didn't open it. I was scared it'd be one more thing that proves I'm bad at this.

I opened it at 6:40 this morning with cold coffee and my hair still wet.

The first snippet was twenty-two lines of Python. A function that's supposed to remove duplicate emails from a list. It looked *fine.* It looked like something I'd paste in without blinking. That alone made my chest tighten, because if it looked fine to me, and there was a bug in it, then how many bugs have I already shipped without seeing them?

I read it once. Nothing.

I read it again. My eyes slid right off it like it was oiled glass. I felt that familiar heat creeping up my neck, the interview heat, and for a second I wanted to close the tab and go back to pretending.

But there's no one watching. That's the thing. No Zoom window. No interviewer. No classmates. Just me and twenty-two lines.

So I did something I've never actually done. I read it *slowly.* Line by line. Out loud, whispering, like a weirdo on the 7 a.m. bus. *"For each email in the list... lowercase it... check if it's in seen..."*

And then I saw it.

The function lowercased the email for the *check,* but appended the *original* one to the result. So `Maya@gmail.com` and `maya@gmail.com` would both survive. It was right there. It had been right there the whole time, hiding in plain sight like a splinter you can only find when the light hits it just right.

I didn't feel triumphant, exactly. I felt *stunned.* Like I'd been squinting at the world for two years and someone handed me glasses.

I got the explanation wrong on the second part (I didn't catch that it also broke the original order), and the site showed me why. It didn't sting the way I expected it to. It felt like a coach, not a judge.

It took eleven minutes. Eleven minutes, and the cold stone in my stomach feels a little lighter. Not gone. Lighter.

The streak counter says **1.**

I want to see it say 2.

---

### Entry 3: After Using the Product

**Sunday, 10:30 p.m., six weeks later**

Streak: **41.** (I missed one day during finals and I'm still bitter about it.)

I've been putting off writing this because I'm scared that if I say it out loud, I'll jinx it. But I have to get it down.

Friday was my second-round interview for the summer internship. The same kind of interview that broke me last spring.

He shared his screen and pasted in a function. *"Our junior dev used AI to write this. Something's off in production. Can you take a look?"*

And my body did the thing. The heat in my neck. The tight chest. The old animal panic, ready to bolt.

But then something else kicked in, something that wasn't there six months ago. My eyes just *started reading.* Top to bottom. Slowly. The way I've done it forty-one mornings in a row on the bus with cold coffee. Inputs. Loop. State. What changes? What doesn't?

There. A mutable default argument. `def add_item(item, cart=[])`. Every call shares the same list. Carts bleeding into each other across users. It was the exact kind of bug I'd missed a hundred times before, and now it lit up on the screen like a road flare.

I *explained* it. Out loud. In full sentences. I even said, *"That's a classic AI mistake, it pattern-matches to code that looks clean but carries hidden state."* He actually smiled. He said, *"Yeah. That's exactly it."*

When the call ended, I sat in my dark room and cried. Not sad crying. That ugly, shaky, full-body release you get after holding your breath for way too long. Two years of shame, just draining out of me.

I'm not magically fixed. I still get anxious. I still sometimes stare at a block of code and feel the white-sweater blur coming back. But the overwhelm doesn't swallow me whole anymore. I know what to *do* now. Slow down. Read line by line. Trust what I see.

The stone in my stomach is gone. In its place there's something warmer, quieter. I think it's what confidence feels like when you earned it, instead of borrowing it from a chatbot.

I texted my mom tonight. Not a thumbs up this time.

*"I think I'm actually good at this."*

She sent back eleven heart emojis.

The fan's still wobbling. *Tick, tick, tick.* But it doesn't sound like a countdown anymore.

It just sounds like a fan.

---

# Part 3: Brand Identity & Design System

## Prompt used

> A "Brand & Design Syndicate" prompt (Brand Strategist, Lead UI/UX Designer, Lead Front-End Developer) that turns a Research Summary into a Brand Identity & Design System in a fixed markdown structure, ending with a design-tokens JSON object. No Research Summary was available, so the avatar and diary entries above were used instead, and the business name and gradient were invented.

## Linewise Brand Identity & Design System

> **Source note:** No formal Research Summary was provided. This document uses the Problem Aware avatar (Maya Rodriguez) and her three diary entries as the research input. The business name **"Linewise"** and the brand gradient are **placeholders invented for this exercise**. They were not extracted from a research summary.

### Brand Identity

#### Brand Essence

- **Clarity:** Turning "white sweater" blur into code you can actually see and understand.
- **Confidence:** Real competence earned through practice, not borrowed from a chatbot.
- **Encouragement:** A coach, not a judge. Mistakes are explained, never punished.
- **Consistency:** Small daily reps (one snippet, about 10 minutes) that compound into mastery.
- **Honesty:** No hype, no "10x" promises. Just real skills that hold up in an interview.
- **Accessibility:** Free, low-commitment, and built for students with little time or money.
- **Craft:** Respect for fundamentals: reading slowly, line by line, and trusting what you see.

#### Brand Voice

- **Tone:** Warm, calm, and reassuring, like a patient senior developer sitting next to you. Confident without being smug. We never mock a mistake.
- **Language:** Clear, plain, and jargon-light. Technical terms are explained the first time they appear. We speak the audience's language ("AI slop," "skill issue," "vibe coding") sparingly and with empathy, never to sound cool.
- **Communication Style:** Pain-first and progress-focused. We name the problem honestly ("You can write code, but reading it feels like a foreign language"), then show the next small step. We celebrate streaks and breakthroughs, and we frame errors as discoveries ("You almost had it. Here's what was hiding").

#### Brand Narrative

Every day, thousands of computer science students paste AI-generated code into their projects, watch the tests turn green, and feel a cold stone settle in their stomach, because they don't actually know why it works. They can write code, but they can't *read* it. Then an interviewer says "walk me through this," and the silence lasts forever. Linewise exists for that moment. It's a free daily practice where you get one snippet of flawed, AI-generated code and a single job: find what's wrong. There's no audience and no judgment. It's just you, twenty lines, and a coach who explains what you missed. Ten minutes a day, line by line, the blur sharpens until bugs light up like road flares. Linewise helps students stop feeling like impostors and start becoming the developer everyone turns to when something breaks.

### Design System

#### Color Palette

##### Primary Colors

- **Gradient Base:** The brand gradient is the core of the Linewise identity. It moves from the deep midnight of a 1:47 a.m. study session, through the cool blues of focused reading, to the warm flare of a bug finally spotted.

```css
background: linear-gradient(135deg, #0F172A 0%, #1E3A8A 18%, #2563EB 34%, #06B6D4 50%, #10B981 66%, #F59E0B 84%, #F97316 100%);
```

- **Primary Colors (Extracted from gradient):**
  - `#0F172A`: **Midnight** (Focus)
  - `#1E3A8A`: **Indigo** (Depth)
  - `#2563EB`: **Cobalt** (Trust)
  - `#06B6D4`: **Cyan** (Clarity)
  - `#10B981`: **Emerald** (Growth)
  - `#F59E0B`: **Amber** (Insight)
  - `#F97316`: **Flare** (Discovery)

##### Secondary Colors

- **Dark Blue (primary text):** `#1E293B`
- **Medium Gray (secondary text):** `#64748B`
- **Light Gray (backgrounds):** `#F1F5F9`
- **White:** `#FFFFFF`
- **Black:** `#000000`

##### Functional Colors

- **Success:** `#16A34A` (bug found, streak extended)
- **Warning:** `#D97706` (partial answer, streak at risk)
- **Error:** `#DC2626` (incorrect answer, failed submission)
- **Info:** `#0284C7` (hints, explanations, tips)

#### Typography

##### Font Family

- **Primary Font: Inter.** Inter was designed for screens. Its tall x-height, open letterforms, and clear distinction between similar glyphs (l, I, 1) make it ideal for a product built around careful reading. It stays legible at small sizes on mobile, where many students practice on the bus, and it works well next to monospaced code blocks. *(Code snippets use **JetBrains Mono** as a utility font for distinct characters and ligature-free clarity.)*
- **Secondary Font: DM Serif Display.** Used only for major headlines and milestone moments (streak celebrations, landing page heroes). Its high-contrast, editorial feel adds warmth and gravitas, so earned confidence feels like a real achievement and not just another app notification. The contrast with Inter separates emotional moments from functional UI.

##### Font Sizes

| Style | rem | px | Line-Height |
|---|---|---|---|
| **Display** | 4.5rem | 72px | 1.1 |
| **H1** | 3rem | 48px | 1.2 |
| **H2** | 2.25rem | 36px | 1.25 |
| **H3** | 1.875rem | 30px | 1.3 |
| **H4** | 1.5rem | 24px | 1.35 |
| **H5** | 1.25rem | 20px | 1.4 |
| **H6** | 1.125rem | 18px | 1.45 |
| **Body Regular** | 1rem | 16px | 1.6 |
| **Body Small** | 0.875rem | 14px | 1.55 |
| **Body XSmall** | 0.75rem | 12px | 1.5 |
| **Caption** | 0.6875rem | 11px | 1.45 |

##### Font Weights

- **Light (300):** Large display text and subtle supporting copy
- **Regular (400):** Body text and code explanations
- **Medium (500):** Labels, navigation, and button text
- **Semibold (600):** Subheadings, card titles, and emphasis
- **Bold (700):** Primary headings, streak counters, and key metrics

#### UI Components

##### 21st.dev Components

- **Navigation:** Top navbar, mobile bottom tab bar, breadcrumbs
- **Layout:** Containers, split-pane layouts (code panel and answer panel), cards, grids
- **Forms:** Text areas for bug explanations, line-selection inputs, sign-up and login forms
- **Feedback:** Toasts, alerts, progress bars, skeleton loaders
- **Data Display:** Stat cards, streak calendars, tables, badges
- **Disclosure:** Accordions for hints, tabs for explanation views, modals

##### MagicUI Components

- **Animated Number Ticker:** Counts up the streak (1 → 41) and stat totals
- **Shimmer Button:** Primary "Start Today's Snippet" call to action
- **Confetti:** Plays when a bug is found correctly or a streak milestone is reached
- **Animated Beam / Border Beam:** Highlights the buggy line when the answer is revealed (the "road flare" moment)
- **Marquee (Testimonial Carousel):** Scrolling student success stories on the landing page
- **Blur Fade / Scroll Animations:** Sections fade in from blur to focus on scroll, echoing the brand's "blur to clarity" story

##### reactbits.dev Components

- **Navigation:** Animated menus and dock-style mobile navigation
- **Layout:** Animated grids and masonry for practice history
- **Text Animations:** Split text and blur-text reveals for headlines
- **Feedback:** Animated counters and click-spark effects on submissions
- **Data Display:** Animated cards and tilted cards for achievements
- **Backgrounds:** Subtle animated gradient backgrounds using the brand palette

##### Custom Components

- **Daily Snippet Viewer:** A syntax-highlighted, line-numbered code panel where users click or tap to flag suspected bug lines, with a "read aloud" line-by-line focus mode.
- **Bug Reveal & Coach Explanation Panel:** After submission, highlights the actual bug, compares it with the user's answer, and explains *why* in plain language, including any partial credit.
- **Streak & Progress Dashboard:** Streak counter, calendar heatmap, accuracy over time, and a breakdown of bug categories mastered (off-by-one, mutable defaults, state leaks, and so on).
- **Interview Mode Simulator:** A timed "walk me through this" mode where users explain code in writing or by voice, preparing them for live technical interviews.

#### Micro-Interactions

- **Button Hover:** A slight lift (`translateY(-2px)`), a soft shadow, and a gradient shift on primary buttons over 150ms ease-out.
- **Form Focus:** Inputs get a 2px Cobalt (`#2563EB`) ring that eases in over 120ms, with the label shifting to Cobalt.
- **Line Selection:** Tapping a code line fades in an Amber highlight and a small check icon. Tapping again removes it.
- **Loading States:** Skeleton shimmer in Light Gray while snippets load. Submission shows a pulsing Cyan dot animation.
- **Success Actions:** A correct answer triggers an Emerald pulse on the bug line, a brief confetti burst, and the streak counter ticking up by one.
- **Scrolling & Navigation:** Sections blur-fade into focus on scroll. Page transitions use a 200ms opacity and slide.

#### Responsive Design

- **Mobile-First Approach:** Every layout starts from the smallest screen. Many users practice on their phones during commutes, so the mobile experience is the primary one.
- **Breakpoints:**
  - `sm`: 640px
  - `md`: 768px
  - `lg`: 1024px
  - `xl`: 1280px
  - `2xl`: 1536px
- **Mobile Adaptations:**
  - Simplified navigation using a hamburger menu or bottom tab bar
  - Stacked layouts: the code panel sits above the answer panel instead of side by side
  - Larger touch targets (minimum 44×44px), especially for selecting code lines
  - Horizontally scrollable code blocks with no forced wrapping, plus pinch-to-zoom support
  - Sticky "Submit" button at the bottom of the viewport

#### Accessibility

- **Color Contrast (WCAG AA):** All text meets a 4.5:1 minimum ratio (3:1 for large text). Gradient colors are never used for body text.
- **Keyboard Navigation:** Full keyboard support, including arrow-key navigation between code lines and Enter or Space to flag a line.
- **Screen Reader Support (ARIA):** Code lines expose line numbers and content to screen readers. Live regions announce results, streak changes, and hints.
- **Visible Focus Indicators:** High-visibility 2px focus rings on all interactive elements, never removed.
- **Respect for Reduced Motion:** `prefers-reduced-motion` turns off confetti, beams, and blur-fades, replacing them with instant state changes.
- **Color-Independent Feedback:** Correct and incorrect states always pair color with an icon and text, never color alone.

#### Dark/Light Mode

Both modes are fully supported and implemented with **DaisyUI themes** (`linewise-light` and `linewise-dark`). The app detects the user's system preference automatically via `prefers-color-scheme`, and a toggle in the navbar lets users override it, with the choice saved locally. Dark mode is expected to be popular with late-night studiers and uses Midnight (`#0F172A`) as the base surface.

### Implementation Guidelines

#### CSS Framework

- **Tailwind CSS:** Utility-first styling and responsive variants
- **DaisyUI:** Component classes and theme management (light and dark)
- **Custom Utilities:** `[placeholder]`, such as `.bg-linewise-gradient`, `.code-line-highlight`, and `.text-balance`

#### Animation Library

- **Framer Motion:** Complex animations, including bug-reveal sequences, page transitions, streak celebrations, and layout animations
- **Tailwind Animations:** Simple effects such as `animate-pulse`, `animate-spin`, hover transitions, and fades

#### Icon System

- **Heroicons:** Primary icon set (outline for UI, solid for active and selected states)
- **Custom SVGs:** Brand-specific icons such as the Linewise logo mark, bug-category icons, and streak flame

#### Asset Management

- **Icons:** SVG
- **Images:** WebP (with PNG fallback where needed)
- **Video:** MP4 / WebM

#### Code Structure

- **Component-Based Architecture:** Small, reusable React components (`SnippetViewer`, `CodeLine`, `StreakCounter`, `CoachPanel`) organized by feature
- **Utility-First CSS:** Tailwind utilities first, with extraction into components or `@apply` only for repeated patterns
- **Responsive Variants:** Mobile-first base styles, with `sm:`, `md:`, `lg:` variants layered on top
- **Design Tokens as Source of Truth:** All colors, spacing, and radii come from the token file below, wired into `tailwind.config`

### Design Tokens

```json
{
  "colors": {
    "primary": {
      "midnight": "#0F172A",
      "indigo": "#1E3A8A",
      "cobalt": "#2563EB",
      "cyan": "#06B6D4",
      "emerald": "#10B981",
      "amber": "#F59E0B",
      "flare": "#F97316"
    },
    "neutral": {
      "darkBlue": "#1E293B",
      "mediumGray": "#64748B",
      "lightGray": "#F1F5F9",
      "white": "#FFFFFF",
      "black": "#000000"
    },
    "functional": {
      "success": "#16A34A",
      "warning": "#D97706",
      "error": "#DC2626",
      "info": "#0284C7"
    }
  },
  "typography": {
    "fontFamily": {
      "primary": "Inter, sans-serif",
      "secondary": "DM Serif Display, serif"
    }
  },
  "spacing": {
    "xs": "0.25rem",
    "sm": "0.5rem",
    "md": "1rem",
    "lg": "1.5rem",
    "xl": "2rem",
    "2xl": "3rem",
    "3xl": "4rem"
  },
  "borderRadius": {
    "sm": "0.125rem",
    "md": "0.25rem",
    "lg": "0.5rem",
    "xl": "1rem",
    "full": "9999px"
  }
}
```

---

# Part 4: Landing Page PRD

## Prompt used

> A detailed B2B SaaS landing page PRD template (for an "AI-Powered Sales Intelligence Platform") was provided, and the request was to adapt it for Linewise.

## Product Requirements Document: Linewise Landing Page

> **Source note:** This PRD adapts a B2B SaaS landing page template for **Linewise**, a free daily code-reading practice product. Inputs: the Problem Aware avatar (Maya Rodriguez), her three diary entries, and the *Linewise Brand Identity & Design System*. "Linewise," its gradient and all product details are **placeholders from a class exercise**, not a real business. Sections marked **[ADAPTED]** were changed significantly from the template; **[REMOVED]** marks template content that does not fit a free student product.

### Executive Overview

**Product:** Linewise: free daily practice in reading, reviewing and debugging flawed AI-generated code
**Audience:** Primarily CS students (secondary: early-career developers) who use AI assistants and are **Problem Aware**. They know they can't confidently read or debug AI code, but don't know structured practice exists.
**Purpose:** Turn a stressed, skeptical student into a daily practicer. Name their pain honestly, show the fix in under a minute, and get them to finish their first snippet.
**Primary conversion:** Start today's snippet (account creation optional until the first snippet is done)
**Secondary conversion:** Sign up to save a streak

#### Messaging Strategy (Problem Aware) [ADAPTED]

Because the visitor is Problem Aware, the page **leads with the pain, not the product**. Order of persuasion:

1. Name the pain in their words ("It runs. The tests pass. And you have no idea why.")
2. Validate it with real data (they are not alone, and it isn't a "skill issue")
3. Reframe the cause: the missing skill is *reading*, not writing or prompting
4. Introduce the fix: one snippet, about 10 minutes, every day
5. Let them try it immediately, with no signup wall

---

### Page Architecture & UI Components

#### 1. Navigation Bar

**Requirements:**
- **Position:** Fixed/sticky header, visible on scroll
- **Components:**
  - Logo (left, links to top)
  - Links: How It Works, Try a Snippet, What You'll Learn, FAQ
  - Actions: "Start Today's Snippet" (primary CTA), "Sign In" (text link)
- **Behavior:**
  - Desktop: horizontal navigation
  - Mobile: hamburger menu with slide-out drawer
  - Transparent over hero, solid Midnight (`#0F172A`) with blur after 40px of scroll
- **Specifications:**
  - Height: 72px desktop, 60px mobile
  - Max-width: 1200px content, centered
  - Z-index: 1000

#### 2. Hero Section [ADAPTED]

**Layout:** Two-column split (55/45): copy left, animated code card right. Stacks below 1024px.

**Copy Structure:**
- **Pre-headline badge (pill):** "Free • One snippet a day • ~10 minutes"
  - *Replaces "Trusted by 500+ teams." Linewise has no users yet, so it cannot claim social proof.*
- **Headline (H1, DM Serif Display, 50–80 characters):**
  - Primary: "You can write code. Can you read what your AI wrote?"
  - Alternates for A/B testing: "It runs. The tests pass. And you have no idea why." / "Stop shipping AI bugs you can't see."
- **Subheadline (150–200 characters):** "Linewise gives you one flawed, AI-generated snippet a day. Your only job: find the bug. Ten minutes of slow, careful reading that turns blur into clarity."
- **CTAs:**
  - Primary: "Start Today's Snippet" (scrolls to the live demo)
  - Secondary: "See How It Works" (ghost button, scrolls to How It Works)
  - Micro-copy: "Free forever • No signup to try • No credit card"
- **Trust indicators:** [REMOVED: client logo bar.] Replaced with a row of supported languages (Python, JavaScript, Java, C++) as plain text chips. No third-party trademarks or logos.

**Visual Component:**
- A code card showing a short buggy Python function with line numbers
- Animation (15–20s loop): the lines blur, then sharpen one by one as a cursor "reads" them; the buggy line gets an Amber/Flare highlight ("road flare" moment)
- Respects `prefers-reduced-motion` (shows the final highlighted state only)

**Technical Specifications:**
- Section height: 90vh minimum
- Background: Midnight with a faint brand gradient glow
- CTA touch targets: 48px minimum

#### 3. Problem / Pain Point Section [ADAPTED]

**Purpose:** Make Maya feel seen. This is the most important section for a Problem Aware visitor.

**Section headline (question format):** "Pasting AI code you can't actually explain?"

**3-column problem grid:**

| Pain | Copy | Statistic (real, cited) |
|---|---|---|
| **"Almost right" code** | It runs. It looks clean. It's quietly wrong, and you can't see where. | **66%** of developers say their top AI frustration is solutions that are "almost right, but not quite." (Stack Overflow Developer Survey 2025) |
| **Debugging loops** | You paste the error back into the chatbot. It's confidently wrong again. An hour disappears. | **45%** say debugging AI-generated code takes more time than expected. (Stack Overflow Developer Survey 2025) |
| **The interview freeze** | "Walk me through this function." Fourteen seconds of silence. | Only **33%** of developers trust the accuracy of AI output. (Stack Overflow Developer Survey 2025) |

- **Rule:** Every statistic must link to its source. No invented numbers.
- **Icons:** Line icons, 2px stroke, Flare accent
- **Closing line (reframe):** "The problem isn't your prompts. It's that nobody ever taught you to *read* code."

**Technical Specifications:**
- Background: Light Gray (`#F1F5F9`) in light mode, contrasting the dark hero
- Padding: 120px desktop, 80px mobile
- Grid: 3 columns desktop, 1 column mobile
- Stats: 48px bold, Flare color

#### 4. Solution Positioning Section

**Headline:** "Read slowly. Line by line. Until the bug lights up."

**Solution Narrative:**
- **P1 (bridge):** Writing code and reading code are different skills. LeetCode trains the first. AI made the second the one that matters.
- **P2 (method):** Linewise uses deliberate practice: one short, realistic AI-generated snippet with one hidden bug. You read it, flag the line, explain what's wrong. A coach explains what you missed.
- **P3 (outcome):** In a few weeks, the "white sweater" blur turns into a red thread you can spot at a glance.

**Visual Proof (Before → After):**
- Before: a code block rendered blurred and gray, label "Week 1: everything looks fine"
- After: the same block sharp, with the bug line highlighted, label "Week 6: the bug jumps out"

**Unique Value Callout:** "Unlike LeetCode, you never write a line. Linewise trains the skill AI didn't replace: reading and judging code."

**Technical Specifications:** Max-width 1200px; visual 60% width desktop; blur-fade on scroll.

#### 5. How It Works & Features Section [ADAPTED]

**Part A: How It Works (3 numbered steps):**
1. **Read** today's snippet (≈20 lines, AI-generated, one hidden bug)
2. **Flag** the line(s) you think are wrong and explain why in one sentence
3. **Learn** from the coach's explanation, including what you missed

**Part B: Features (alternating image/text, 4 blocks):**

| Feature | Benefit copy | Visual |
|---|---|---|
| **Daily Snippet** | One realistic snippet a day. Small enough for a bus ride, hard enough to sharpen you. | Snippet viewer with line numbers |
| **Coach, Not Judge** | Every answer gets a plain-language explanation, with partial credit. Mistakes become discoveries. | Explanation panel |
| **Streaks & Bug Patterns** | Track your streak and which bug types you've mastered: off-by-one, mutable defaults, shared state and more. | Streak calendar + category bars |
| **Interview Mode** | Practice "walk me through this" under a timer, so the freeze never happens again. | Timer + explanation box |

- **Rule:** No outcome metrics (e.g. "40% higher win rate") until real user data exists. Use descriptive benefits only.

**Technical Specifications:** 100px between blocks; images 600×450; stack at 768px; fade + slide on scroll.

#### 6. Live Demo: "Try a Snippet" [ADAPTED, replaces ROI Calculator and Demo Video]

**Purpose:** For a free product, the most convincing proof is doing it. The visitor completes one real snippet on the landing page, with no signup.

**Functional Components:**
- Syntax-highlighted snippet (Python, ~10–15 lines) with clickable line numbers
- User selects one or more lines, then presses "Check My Answer"
- **Result states:**
  - **Correct:** Emerald highlight on the bug line, explanation revealed, confetti (respecting reduced motion), CTA "Save your streak — it's free"
  - **Partially correct / incorrect:** Amber highlight on the real bug, encouraging copy ("Almost. Here's what was hiding"), explanation revealed
- "Show a hint" disclosure before answering
- "Reset" to try again

**Sample snippet (launch demo):** Duplicate-email remover that lowercases emails for the membership check but appends the original casing, so `Maya@x.com` and `maya@x.com` both survive. (The same bug Maya found on her first day.)

**Technical Specifications:**
- React component with state for selected lines and result
- Keyboard: arrow keys move between lines, Space toggles selection, Enter submits
- Screen reader: each line is a toggle button with `aria-pressed`; results announced via `aria-live="polite"`
- Mobile: horizontally scrollable code, 44px minimum line height for tap targets

#### 7. Social Proof Section [ADAPTED]

**Rule:** **Never publish invented testimonials, names, ratings or usage numbers.** Linewise is pre-launch.

**At launch, show instead:**
- **"Built on what developers are saying"**: the cited survey data from Section 3
- **Product facts bar:** "$0 forever • ~10 min a day • 1 snippet daily • 4 languages at launch"

**After beta (Phase 2):**
- Real, consented student quotes with first name, school year and streak length
- Real aggregate stats (snippets completed, median streak)

#### 8. Pricing Section [ADAPTED]

[REMOVED: 3-tier pricing table and feature comparison.]

**Replace with a single "It's free. Really." card:**
- Price: **$0**, permanently, for daily practice
- Included: daily snippet, coach explanations, streaks, bug-pattern tracking, interview mode
- CTA: "Start Today's Snippet"
- Honest note: "If we ever add paid extras, daily practice stays free."

**FAQ micro-section:**
- "Is it actually free?"
- "Do I need to know a specific language?"
- "How long does it take each day?"
- "Will this help with technical interviews?"
- "What happens if I miss a day?"
- "Is my data private?"

#### 9. Languages & Privacy Section [ADAPTED, replaces Integration & Security]

**Languages (left):** "Practice in the language you're learning." Chips: Python, JavaScript, Java, C++ (more planned).

**Privacy (right):** "Your practice stays yours."
- No code from your own projects is ever uploaded
- Minimal data: email (or GitHub sign-in) and practice history
- No selling data, no ads
- Delete your account and history anytime
- If Linewise partners with universities, student-record rules (e.g. FERPA in the US) must be reviewed before launch

[REMOVED: SOC 2, ISO 27001 and compliance badges. Never display badges for certifications not actually held.]

#### 10. Final CTA Section

- **Headline:** "Your first snippet takes ten minutes."
- **Supporting text:** "No signup to try. No credit card. Just you, twenty lines and one hidden bug."
- **Primary CTA:** "Start Today's Snippet" (60px height)
- **Trust elements:** "Free forever" • "No signup to try" • "~10 min a day" • "Coach, not judge"
- **Background:** full brand gradient, with text contrast checked

#### 11. Footer [ADAPTED]

- **Column 1:** Logo, tagline ("Read code like you mean it."), copyright
- **Column 2 (Product):** How It Works, Try a Snippet, FAQ
- **Column 3 (Learn):** Bug Pattern Library (planned), Blog (planned)
- **Column 4 (Legal):** Privacy, Terms
- Footer note: "Linewise is a concept created for a class exercise."
- Background: Midnight; 14px text; 3 columns desktop, 1 mobile

---

### Visual Style Guide

All values come from *Linewise Brand Identity & Design System*.

#### Color Palette
- **Brand gradient:** `linear-gradient(135deg, #0F172A 0%, #1E3A8A 18%, #2563EB 34%, #06B6D4 50%, #10B981 66%, #F59E0B 84%, #F97316 100%)`
- **Primary:** Cobalt `#2563EB` (buttons, links, focus rings)
- **Secondary:** Cyan `#06B6D4` (highlights, clarity moments)
- **Accent:** Flare `#F97316` / Amber `#F59E0B` (bug highlights, stats). Never used for body text on white.
- **Neutrals:** Midnight `#0F172A` (dark surfaces), Dark Blue `#1E293B` (text), Medium Gray `#64748B`, Light Gray `#F1F5F9`, White `#FFFFFF`
- **Functional:** Success `#16A34A`, Warning `#D97706`, Error `#DC2626`, Info `#0284C7`

#### Typography
- **Headings:** DM Serif Display (H1, H2 and milestone moments only)
- **Body/UI:** Inter
- **Code:** JetBrains Mono, with `ui-monospace, monospace` fallback
- **Scale:** Per the design system (H1 48px / Body 16px / Caption 11px; Display 72px used only in the final CTA)

#### Spacing, Radius, Motion
- Spacing tokens: 0.25rem → 4rem (xs → 3xl); section padding 120px desktop / 80px tablet / 60px mobile
- Radius: buttons `lg` (0.5rem), cards `xl` (1rem), chips `full`
- Motion: 150ms micro / 300ms standard / 500ms reveal; easing `cubic-bezier(0.4, 0, 0.2, 1)`; all motion disabled under `prefers-reduced-motion`

#### Responsive Breakpoints (Tailwind)
`sm` 640 • `md` 768 • `lg` 1024 • `xl` 1280 • `2xl` 1536. Mobile-first.

---

### Technical Requirements

#### Performance
- LCP < 2.5s on mid-range mobile; Lighthouse > 90 in all categories
- No hero video; the hero animation is CSS only (lighter for students on mobile data)

#### Code Architecture
```
/components
  /Hero
  /ProblemGrid
  /Solution
  /HowItWorks
  /Features
  /SnippetDemo     ← most complex component, build first after Hero
  /FreeCard
  /FAQ
  /Footer
  /shared (Button, Card, Chip, CodeBlock)
```
- React functional components + hooks; Tailwind CSS + DaisyUI themes (`linewise-light`, `linewise-dark`); Framer Motion for reveals

#### Accessibility (WCAG 2.1 AA)
- Semantic HTML, single H1, no skipped heading levels
- 4.5:1 contrast for body text; gradient never behind small text without an overlay
- Full keyboard support, including the snippet demo
- Visible 2px focus rings; color is never the only signal (icons + text on results)

#### SEO
- Title (50–60 chars): "Linewise — Daily Practice Reading & Debugging AI Code"
- Meta description (150–160 chars) focused on the pain: AI code you can't explain
- JSON-LD: Organization, FAQPage

#### Analytics (privacy-respecting) [ADAPTED]
- Use a cookie-light tool (e.g. Plausible) instead of heavy tracking, since the audience is students
- Events: CTA clicks, demo line selected, demo submitted, demo correct/incorrect, signup started/completed, FAQ opened, scroll depth

#### Signup [ADAPTED, replaces Demo Request Form]
- Shown **after** the first snippet is done: "Save your streak"
- Fields: email *or* "Continue with GitHub"; nothing else
- Privacy policy link; no marketing opt-in by default

---

### Content Guidelines

#### Voice & Tone
- **Warm, calm, honest:** a patient senior dev, not a hype machine
- **Pain-first:** name the feeling before offering the fix
- **Coach, not judge:** mistakes are "discoveries," never failures
- **No fake urgency:** no countdowns, no "only 3 spots left"

#### Copywriting Principles
1. Use the audience's own words ("It works on my machine," "I'm cooked") sparingly and with empathy
2. Every number is real and cited, or it isn't on the page
3. Benefits are concrete but not inflated ("ten minutes a day," not "10x developer")
4. Avoid shaming AI users; the message is "use AI *and* be able to check it"

---

### Development Priority
1. Nav + Hero
2. Problem section
3. Snippet Demo (core conversion)
4. How It Works + Features
5. Free card + FAQ
6. Languages & Privacy, Final CTA, Footer
7. Polish: animations, dark mode, reduced motion

### Success Metrics [ADAPTED]

#### Primary KPIs
- **Demo start rate:** % of visitors who select at least one line
- **Demo completion rate:** % who submit an answer
- **Signup rate after demo:** % who save a streak
- **Day-7 return rate:** % of signups who do a second snippet within 7 days (the real measure of product fit)

#### Secondary Metrics
- Scroll depth to the Problem section (does the pain resonate?)
- FAQ open rates (which objections matter most)
- Hero headline A/B test results

---

# Part 5: Landing Page

The PRD and design system above were used to build a working landing page on a Claude design canvas:

**Link:** https://claude.ai/artifact/4CBFY2jJ7SnSY4KbN1gDUE

What's on the page, top to bottom:

1. **Sticky navigation:** logo, How It Works / Try a Snippet / What You'll Learn / FAQ, Sign In, and a "Start Today's Snippet" button
2. **Hero:** "You can write code. Can you read what your AI wrote?" with an animated code card where the lines sharpen from blur and a mutable-default bug lights up (turns off under reduced motion)
3. **Problem section:** three pain cards with real, cited Stack Overflow 2025 stats (66%, 45%, 33%) and the line "The problem isn't your prompts. It's that nobody ever taught you to *read* code."
4. **Solution:** a before/after visual (blurred code in Week 1, the off-by-one bug highlighted in Week 6) and the callout "Unlike LeetCode, you never write a line"
5. **How it works:** Read → Flag → Learn
6. **Features:** Daily Snippet, Coach Not Judge, Streaks & Bug Patterns, Interview Mode (alternating layout)
7. **Live demo:** "Try today's snippet." A clickable Python duplicate-email checker with the bug on line 8 (`seen.add(email)` should be `seen.add(key)`). Different results for a correct, partly correct or wrong answer, plus a hint button and a reset. Works with the keyboard and screen readers.
8. **Free card + FAQ:** "It's free. Really. $0" and six expandable questions
9. **Languages & privacy**
10. **Final call to action** on the brand gradient: "Your first snippet takes ten minutes."
11. **Footer**, with a note that Linewise is a class-exercise concept

---

# Part 6: Critique of the Original PRD Template

## What it does well

- **It's specific.** It gives exact pixel sizes, breakpoints and button heights. An AI coding tool can follow it without guessing, which is the template's stated goal.
- **Every section has a stated purpose.** That makes it easy to tell what to cut or change for a different product.
- **It has a strong technical checklist.** Accessibility, SEO, performance targets, analytics events, a build order and a testing checklist are things a lot of PRDs skip.
- **Its placeholders work well for chaining prompts.** Slots like `[Specify from brand identity]` are where the design system output plugs in.

## Bugs and errors

- **The ROI code crashes.** It declares `revenuGain` but returns `revenueGain`, which throws a `ReferenceError`.
- **The ROI math is shaky.** The text says the calculation uses an hourly rate, but there's no input for it; the code hardcodes `75`. The formula `(timeSavingsHours / 5) * (dealsPerMonth / 20)` mixes units in a way that doesn't mean anything. Also, "Annual ROI" never subtracts the product's cost, so it's really "value created," not ROI.
- **The breakpoints disagree.** The hero stacks at 1024px, the features stack at 768px, the global breakpoints are 768/1024/1440, and the design system uses Tailwind's 640/768/1024/1280/1536. The type sizes also clash: body text is 18px in one section and 16px in the style guide.
- **The trial offers contradict each other.** It says "30-day trial," "Free consultation" and "30-day money-back guarantee" in different places, with no single offer.
- **Some details are out of date.** Google Optimize, listed for A/B testing, was shut down in 2023. "iOS 13+" also clashes with "last 2 versions" in the same list.

## Design problems

- **It invites made-up proof.** Example stats ("67%… Gartner"), "Trusted by 500+," aggregate numbers and compliance badges are written as if they were real. An AI tool will happily ship them. For a real company, displaying certification badges you don't hold is a legal risk. The template should tell the tool never to invent these.
- **It doesn't account for the visitor's awareness stage.** It hardcodes one persuasion order for every product and has no slot for the avatar, so it had to be reworked for a Problem Aware visitor like Maya.
- **There are too many competing calls to action.** Request Demo, Schedule a Demo, Start Free Trial, Get Your ROI Report and an exit-intent offer all compete for the same click. A PRD should name one main conversion.
- **Some requirements work against each other.** A looping video in the hero conflicts with the "under 3 seconds on 3G" load target. The exit-intent modal conflicts with the "create urgency authentically" rule.

## Takeaway for the course

The template is a good example of a prompt that is very specific about format but has no guardrails on facts. It tells the model exactly how things should look, but never says which content must be true.
