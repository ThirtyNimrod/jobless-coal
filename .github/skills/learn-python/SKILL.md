---
name: learn-python
description: >-
  Orchestrates the `document-session-files`, `explain-problem-progressively`, `teach-dsa-from-history`,
  and `generate-obsidian-index` skills to save all questions asked, answered, and discussed in the
  current chat session. Produces files in 1.questions/, 2.answers/, 3.understand/, and study/.
  Use when: /learn-python save, save all progress, persist session.
argument-hint: 'Optional: specify additional notes or a custom session title'
user-invocable: true
---

# Learn Python Skill

This skill acts as an orchestrator, invoking all four core skills (`document-session-files`, `explain-problem-progressively`, `teach-dsa-from-history`, and `generate-obsidian-index`) to save all questions and answers discussed in the current session.

## When to Use

- The user invokes `/learn-python save`
- At the end of a tutoring session to persist all progress
- When the user wants to ensure all discussed problems and solutions are saved and indexed

---

## Procedure

### Step 1 — Document All Questions and Solutions

Invoke the `document-session-files` skill to:
- Extract all problems discussed in the session
- Save problem descriptions to `1.questions/`
- Save all solution approaches to `2.answers/`

### Step 2 — Explain Problems Progressively

Invoke the `explain-problem-progressively` skill for **every problem documented in Step 1**:
- Walk through each problem from brute force to optimal
- Save a full progressive explanation to `3.understand/{number}.{source}.md`
- This step is **mandatory** — every problem must have a corresponding understand file

### Step 3 — Teach Concepts from History

Invoke the `teach-dsa-from-history` skill for **every distinct DSA concept** encountered across the session's problems:
- Reference the user's saved problems and solutions from `1.questions/`, `2.answers/`, and `3.understand/`
- Save a concept lesson to `study/{concept_slug}.md`
- If a `study/` file for a concept already exists, append the new problem examples rather than overwriting
- This step is **mandatory** — every new concept must have a corresponding study file

### Step 4 — Update the Obsidian Index

Invoke the `generate-obsidian-index` skill to:
- Regenerate the `index.md` file
- Ensure all new problems, explanations, and concept lessons are indexed
- Categorize by topic, difficulty, and approach
- Link to all four folder types: `1.questions/`, `2.answers/`, `3.understand/`, `study/`

---

## Output

After completing all steps, output a summary:

```
Session saved successfully:

1.questions/   — {N} problem descriptions saved
2.answers/     — {N} solution files saved
3.understand/  — {N} progressive explanations saved
study/         — {N} concept lesson files saved/updated

Index updated with {N} topics.

Open index.md in Obsidian to view your full progress.
```

---

## Key Rules

- **Invoke all four skills in sequence** — no step may be skipped
- **Steps 2 and 3 are mandatory** — every problem gets an understand file; every concept gets a study file
- **Handle missing directories gracefully** — create `1.questions/`, `2.answers/`, `3.understand/`, and `study/` if they do not exist
- **Preserve session context** — ensure all discussed problems and solutions are saved
- **Regenerate the full index** — do not append; overwrite `index.md` entirely
- **Output a clear summary** — confirm what was saved and indexed across all four folders

---

## Example Usage

**User Command:**
```
/learn-python save
```

**Output:**
```
Session saved successfully:

1.questions/   — 3 problem descriptions saved
2.answers/     — 6 solution files saved
3.understand/  — 3 progressive explanations saved
study/         — 2 concept lesson files saved/updated

Index updated with 5 topics.

Open index.md in Obsidian to view your full progress.
```