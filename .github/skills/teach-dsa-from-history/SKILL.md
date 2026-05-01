---
name: teach-dsa-from-history
description: >-
  Teaches Data Structure and Algorithm concepts in Python by referencing the user's own
  previously solved problems as concrete examples. Scans the 1.questions/, 2.answers/, and
  3.understand/ directories to ground abstract theory in familiar code. Saves the lesson to
  study/{concept_slug}.md as a reusable Python course module. Use when: teach me hash maps,
  explain recursion, what is dynamic programming, explain this concept, I want to learn about
  two pointers, teach me sliding window, what patterns have I used.
argument-hint: 'Required: the DSA concept or topic to teach, e.g. "hash maps", "recursion", "two pointers"'
user-invocable: true
---

# Teach DSA from History

Teach any Data Structures and Algorithms concept using the user's **own solved problems** as the primary teaching material. Abstract theory is anchored to real code the user has already written and understood — making every lesson personally relevant.

## When to Use

- A user asks "what is a hash map?" after solving Two Sum
- A user wants to understand a pattern they've seen across multiple problems
- Introducing a new concept that builds on something previously solved
- Reviewing a topic the user found confusing

---

## Procedure

### Step 1 — Scan Saved Work

Before teaching anything, read the workspace directories:

1. List all files in `1.questions/` — these are the problems the user has studied
2. List all files in `2.answers/` — these are their actual solutions
3. List all files in `3.understand/` — these are the progressive explanations; read `primary_concept` from each frontmatter to identify which concepts have already been taught
4. Read the relevant solution files to understand which approaches and data structures the user has already encountered

**Extract:**
- Which data structures appear (hash map, stack, queue, set, list, deque)
- Which algorithm patterns appear (two pointers, sliding window, binary search, recursion, BFS, DFS, dynamic programming)
- The specific variable names and problem contexts — use these when giving examples

If `questions/` and `answers/` are empty, note this and offer to teach from scratch using a worked example problem.

---

### Step 2 — Identify Relevant Examples

From the scanned files, select the **most relevant 1–3 examples** that demonstrate the requested concept.

**Preference order:**
1. Problems where the concept is the *primary* solution technique
2. Problems where the concept appears as a *sub-step*
3. If no saved examples exist, note this explicitly and teach using a new, simple example

---

### Step 3 — Teach the Concept

Use a consistent 4-part teaching structure:

#### 3.1 Real-World Analogy

Open with a concrete, everyday analogy. Never lead with the technical definition.

**Examples by concept:**

| Concept | Analogy |
|---------|---------|
| Hash Map | "A physical dictionary — look up a word, get the definition instantly. No need to read every page." |
| Stack | "A stack of plates — always add and remove from the top. The last plate you put on is the first one you take off." |
| Queue | "A line at a coffee shop — first person in line gets served first." |
| Two Pointers | "Two people walking toward each other from opposite ends of a hallway." |
| Sliding Window | "A magnifying glass moving across a page — you only look at a fixed-size region at a time." |
| Recursion | "Russian nesting dolls — each doll contains a smaller version of itself, until you reach the smallest one with nothing inside." |
| Binary Search | "Guessing a number between 1–100: always guess the middle. Each guess eliminates half the remaining options." |
| BFS | "Spreading ripples in water — explore everything one 'hop' away before going two hops." |
| DFS | "Exploring a maze by always going as deep as possible before backtracking." |
| Dynamic Programming | "Remembering your work — instead of solving the same subproblem twice, store the answer the first time and reuse it." |

#### 3.2 Technical Definition

After the analogy has landed, introduce the formal definition:

> "In computer science terms, a **hash map** is a data structure that stores key-value pairs and provides average O(1) — that is, near-instant — lookup, insertion, and deletion by using a hash function to compute a memory location from the key."

Keep definitions precise but not dense. Define any technical sub-terms (e.g., "hash function") immediately.

#### 3.3 Your Code, Explained

Reference the specific saved file(s) from the user's `2.answers/` directory. Quote actual lines from their code:

> "Remember when you solved **Two Sum** (`2.answers/1.leetcode.hash_map.py`)? Here's what you wrote:
>
> ```python
> seen = {}  # This IS the hash map
>
> for index, number in enumerate(nums):
>     complement = target - number
>     if complement in seen:       # O(1) lookup — instant check
>         return [seen[complement], index]
>     seen[number] = index         # Store: "I've seen this number at this index"
> ```
>
> The `seen` dictionary *is* the hash map. Every time you write `if complement in seen`, Python checks the hash map in essentially constant time — no matter how large the list is."

#### 3.4 The Pattern to Remember

Distill the concept into one memorable rule the user can apply to future problems:

> **Hash Map Pattern:** When a problem asks you to find a pair, group, or match — and doing it with nested loops feels slow — ask yourself: 'Can I store what I've already seen?' If yes, a hash map is probably the answer.

---

### Step 4 — Generalize with Multiple Examples (if available)

If the user has solved more than one problem using this concept, show the pattern appearing across problems:

> "You've now used hash maps in **three different problems**:
> - `1.leetcode.md` — Two Sum: find complement
> - `49.leetcode.md` — Group Anagrams: group by sorted key
> - `128.leetcode.md` — Longest Consecutive Sequence: fast membership check
>
> Notice the pattern: in all three, the hash map replaced a slow search with an instant lookup."

Summarize the typical time/space trade-offs for the concept in plain English:

> **Hash Map:**
> - **Time:** O(1) average for get/set/check — it doesn't matter if you have 10 items or 10 million, the lookup is equally fast
> - **Space:** O(n) — you're trading memory for speed; you store up to n items in the map
> - **Trade-off:** You spend memory to save time. Almost always worth it.

---

### Step 6 — Practice Problem (Optional)

Offer a next practice problem that uses this concept at a slightly higher difficulty:

> "Want to reinforce this? Try **LeetCode 49 — Group Anagrams**. It uses a hash map in a slightly more creative way. I can walk you through it using the same progressive approach."

---

### Step 7 — Save to `study/`

**Always save the full concept lesson to disk** at `study/{concept_slug}.md` after completing Steps 3–6.

The `study/` folder is organized as a **Python DSA course** — one file per concept, building from simple to complex. These files are standalone lesson notes the user can open in Obsidian to review any time.

**Naming convention for `study/` files:**
- Format: `study/{concept_slug}.md`
- `concept_slug`: lowercase, underscores for spaces (e.g., `two_pointers`, `bit_manipulation`, `hash_maps`)
- One file per concept — if a concept file already exists, **append** new problem examples rather than overwriting

**File template for `study/{concept_slug}.md`:**

````markdown
---
title: "{Concept Name}"
concept: {concept_slug}
module: {canonical learning order number, e.g. 1 for Arrays, 2 for Hash Maps}
problems_referenced: [{number}.{source}, ...]
date_updated: {YYYY-MM-DD}
---

# {Concept Name}

> Part of the Python DSA Course — Module {module}

## Real-World Analogy

{The everyday analogy used to introduce the concept}

## What Is It?

{Formal technical definition in plain English. Define all sub-terms immediately.}

## When to Use This Pattern

> **{Concept} Pattern:** {One-sentence memorable rule for recognising when to apply this concept}

Look for these signals in a problem:
- {Signal 1}
- {Signal 2}
- {Signal 3}

## Your Problems That Use This

{For each problem in the user's history that uses this concept:}

### {number}. {Problem Title} (`1.questions/{number}.{source}.md`)

> **The key use:** {one sentence explaining how this concept appears in this problem}

```python
# From 2.answers/{number}.{source}.{method}.py
{Quoted code excerpt with inline annotations}
```

See the full progressive explanation: [[3.understand/{number}.{source}|{Problem Title} — Progressive Explanation]]

---

## Complexity

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| {op 1} | O(?) | O(?) | {plain-language note} |
| {op 2} | O(?) | O(?) | {plain-language note} |

**Trade-off:** {One sentence summarising the time-vs-space trade-off}

## Practice Next

- **Easier:** {Problem title + LeetCode link}
- **Same level:** {Problem title + LeetCode link}
- **Harder:** {Problem title + LeetCode link}
````

---

## Teaching Quality Standards

- **Always reference real saved files** by exact filename — use paths from `1.questions/`, `2.answers/`, and `3.understand/`
- **Never teach a concept in isolation** — always connect it to a problem the user has seen or will see
- **Use exact variable names from their code** — don't replace `seen` with `hashmap` if their file uses `seen`
- **Avoid concept overload** — teach one concept per session; mention related concepts but don't dive into them unprompted
- **Use progressive complexity** — if explaining recursion, don't introduce memoization in the same breath; offer it as a natural next step
- **Always save to `study/`** — every teaching session must produce a file on disk; never only teach in chat

## Handling Missing History

If `1.questions/` and `2.answers/` are empty:

> "You haven't solved any problems yet, so I don't have your personal examples to reference. Let me teach this concept using a classic problem — and once you've solved it, future lessons will be anchored to your own work."

Then proceed with a canonical example problem for the concept (e.g., Two Sum for hash maps, Valid Parentheses for stacks).
