---
name: generate-obsidian-index
description: >-
  Generates or updates the root index.md as a comprehensive, interconnected DSA study guide
  using Obsidian wikilinks. Categorizes solved problems by topic, links to question descriptions
  and solution files, and creates a navigable knowledge vault. Use when: update index, generate
  study guide, create obsidian index, rebuild index, refresh notes, update knowledge base,
  show my progress, link my notes.
argument-hint: 'Optional: specify a topic to regenerate just that section, e.g. "Arrays" or "Dynamic Programming"'
user-invocable: true
---

# Generate Obsidian Index

Create or update `index.md` at the workspace root — a **comprehensive, interconnected DSA study guide** formatted for the Obsidian note-taking app. Every problem in `1.questions/`, every solution in `2.answers/`, every progressive explanation in `3.understand/`, and every concept lesson in `study/` is surfaced here through Obsidian-native wikilinks, organized by topic, and enriched with metadata for quick navigation.

## When to Use

- After saving new problems via `document_session_files`
- When the user asks to see their progress or study guide
- When the user wants to open their notes in Obsidian
- Periodically to keep the index in sync with saved files

---

## Procedure

### Step 1 — Scan All Saved Files

Read the workspace to build a complete inventory:

1. **List `1.questions/`** — collect all `{number}.{source}.md` files
2. **List `2.answers/`** — collect all `{number}.{source}.{method}.py` files
3. **List `3.understand/`** — collect all `{number}.{source}.md` explanation files; read `primary_concept` from each frontmatter
4. **List `study/`** — collect all `{concept_slug}.md` course module files; read `concept`, `module`, and `problems_referenced` from each frontmatter
5. **Read each `1.questions/*.md` frontmatter** — extract title, difficulty, tags, date solved, and source URL
6. **Group answers by problem** — match each `.py` file to its parent question by number and source
7. **Match understand files to problems** — link `3.understand/{number}.{source}.md` to its corresponding `1.questions/` entry
8. **Match study files to concepts** — link `study/{concept_slug}.md` to all problems that use that concept

Build an internal data structure before writing anything:

```
problems = [
  {
    number: 1,
    source: "leetcode",
    title: "Two Sum",
    difficulty: "Easy",
    tags: ["Array", "Hash Map"],
    url: "https://leetcode.com/problems/two-sum/",
    date_solved: "2025-01-15",
    question_file: "1.questions/1.leetcode.md",
    solution_files: [
      "2.answers/1.leetcode.brute_force.py",
      "2.answers/1.leetcode.hash_map.py"
    ],
    understand_file: "3.understand/1.leetcode.md",   // null if not yet explained
    primary_concept: "Hash Map"
  },
  ...
]

concepts = [
  {
    slug: "hash_maps",
    title: "Hash Maps",
    module: 2,
    study_file: "study/hash_maps.md",
    problems: [1, 49, 128]   // problem numbers
  },
  ...
]
```

---

### Step 2 — Derive Topics from Tags

Group all problems by their `tags` from frontmatter. Use the canonical topic list below. If a tag doesn't fit, add it as a new section.

**Canonical DSA Topics (in learning order):**

1. Arrays & Strings
2. Hash Maps & Sets
3. Two Pointers
4. Sliding Window
5. Stack & Queue
6. Linked Lists
7. Binary Search
8. Trees & Binary Trees
9. Graphs (BFS / DFS)
10. Backtracking
11. Heap / Priority Queue
12. Greedy Algorithms
13. Dynamic Programming
14. Tries
15. Bit Manipulation

A problem may appear under **multiple topics** if it uses multiple concepts. This is intentional — cross-referencing is one of Obsidian's strengths.

---

### Step 3 — Write `index.md`

Generate the full `index.md` file at the workspace root. Use the template below.

**Wikilink format:**
- Problem descriptions: `[[1.questions/1.leetcode|Two Sum]]`
- Solution files: `[[2.answers/1.leetcode.hash_map.py|Hash Map]]`
- Progressive explanations: `[[3.understand/1.leetcode|Two Sum — Explained]]`
- Concept lessons: `[[study/hash_maps|Hash Maps]]`
- Note: Obsidian strips the `.md` extension automatically; include it for `.py` links to ensure they resolve

---

## Output Template

```markdown
---
title: DSA Study Guide
updated: {YYYY-MM-DD}
total_problems: {count}
sources: [leetcode, geeksforgeeks]
---

# DSA Study Guide

> Personal knowledge base for Data Structures and Algorithms.
> Built with [learn-python](https://github.com/ThirtyNimrod/jobless-coal).
> Last updated: {YYYY-MM-DD} · {total_problems} problems solved.

---

## Progress Overview

| Metric | Count |
|--------|-------|
| Total problems solved | {N} |
| Progressive explanations in `3.understand/` | {N} |
| Concept lessons in `study/` | {N} |
| LeetCode | {N} |
| GeeksforGeeks | {N} |
| Easy | {N} |
| Medium | {N} |
| Hard | {N} |

---

## Python DSA Course Modules

> Concept lessons organized in learning order. Each module builds on the previous one.

| Module | Concept | Problems Covered | Study Note |
|--------|---------|-----------------|------------|
| {module} | {Concept Name} | {N} problems | [[study/{concept_slug}\|Open Lesson]] |

---

## Problems by Topic

{Repeat the following block for each topic that has at least one problem}

### {Topic Name}

| # | Problem | Difficulty | Solutions | Explained | Date |
|---|---------|------------|-----------|-----------|------|
| [[1.questions/1.leetcode\|1]] | [[1.questions/1.leetcode\|Two Sum]] | 🟢 Easy | [[2.answers/1.leetcode.brute_force.py\|Brute Force]] · [[2.answers/1.leetcode.hash_map.py\|Hash Map]] | [[3.understand/1.leetcode\|📖]] | 2025-01-15 |
| [[1.questions/15.leetcode\|15]] | [[1.questions/15.leetcode\|3Sum]] | 🟡 Medium | [[2.answers/15.leetcode.two_pointers.py\|Two Pointers]] | [[3.understand/15.leetcode\|📖]] | 2025-01-20 |

> 📖 = progressive explanation available in `3.understand/`

---

## All Problems (Chronological)

> Sorted by date solved — see your learning journey unfold.

| Date | # | Source | Problem | Difficulty | Approaches | Explained |
|------|---|--------|---------|------------|------------|-----------|
{For each problem sorted by date_solved ascending}
| {date} | [[1.questions/{n}.{src}\|{n}]] | {LeetCode\|GeeksforGeeks} | [[1.questions/{n}.{src}\|{title}]] | {emoji} {difficulty} | {comma-separated solution wikilinks} | [[3.understand/{n}.{src}\|📖]] |

---

## Solutions by Approach

> Find all problems solved with a specific technique.

### Hash Map
{list wikilinks to all problems solved using hash map approach}
- [[1.questions/1.leetcode|Two Sum]] → [[2.answers/1.leetcode.hash_map.py|solution]] · [[3.understand/1.leetcode|explanation]]

### Two Pointers
- ...

### Brute Force
- ...

{Add a section for every distinct method name found in 2.answers/}

---

## Quick Reference

### Complexity Cheatsheet

| Structure / Algo | Access | Search | Insert | Delete | Space |
|-----------------|--------|--------|--------|--------|-------|
| Array           | O(1)   | O(n)   | O(n)   | O(n)   | O(n)  |
| Hash Map        | O(1)   | O(1)   | O(1)   | O(1)   | O(n)  |
| Stack / Queue   | O(n)   | O(n)   | O(1)   | O(1)   | O(n)  |
| Binary Search   | —      | O(log n)| —     | —      | O(1)  |
| Sorting         | —      | —      | O(n log n)| —  | O(n)  |

### Python DSA Snippets

```python
# Hash map with default value
from collections import defaultdict
freq = defaultdict(int)

# Deque for O(1) append/pop from both ends
from collections import deque
dq = deque()

# Min heap (Python only has min-heap natively)
import heapq
heap = []
heapq.heappush(heap, value)
smallest = heapq.heappop(heap)

# Sort by custom key
items.sort(key=lambda x: x[1])
```

---

## Navigation Tips (Obsidian)

- **Cmd/Ctrl + Click** any wikilink to open the note
- **Graph View** — see all problem connections at a glance
- **Tag search** — filter by `#easy`, `#medium`, `#hard`, or any topic tag
- **Backlinks** — every solution file links back here automatically
```

---

### Step 4 — Confirm Completion

Output a summary after writing `index.md`:

```
index.md updated

  {N} problems indexed
  {N} topics covered: Arrays, Hash Maps, Two Pointers, ...
  {N} solution files linked
  {N} progressive explanations linked (3.understand/)
  {N} concept lessons linked (study/)

Open index.md in Obsidian for the full interactive view.
```

---

## Key Rules

- **Always regenerate the full file** — do not append; overwrite `index.md` entirely on each run to ensure consistency
- **Use the exact filenames from disk** — do not invent or assume paths; always read `1.questions/`, `2.answers/`, `3.understand/`, and `study/` first
- **Difficulty emoji:** 🟢 Easy · 🟡 Medium · 🔴 Hard · ⚪ Unknown
- **Preserve existing wikilink format** — Obsidian uses `[[path/to/note|Display Text]]`; do not use Markdown-style `[text](url)` links for internal notes
- **Include problems with no tags** — place them under an `## Uncategorized` section rather than omitting them
- **Include problems with no understand file** — show the 📖 column as `—` rather than omitting the row
- **Sort topic sections** by the canonical learning order defined above, not alphabetically

## Obsidian Compatibility Notes

- File path in wikilinks must match the actual file path relative to the vault root (workspace root)
- `.md` files: use `[[1.questions/1.leetcode|Two Sum]]` (no extension needed)
- `.py` files: use `[[2.answers/1.leetcode.hash_map.py|Hash Map]]` (include extension)
- Understand files: use `[[3.understand/1.leetcode|Two Sum — Explained]]` (no extension)
- Study files: use `[[study/hash_maps|Hash Maps]]` (no extension)
- YAML frontmatter must be the very first thing in the file — no blank lines before `---`
- Avoid special characters in wikilink display text that Obsidian cannot render (e.g., `|`, `[`, `]`)
