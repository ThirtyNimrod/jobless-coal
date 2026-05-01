---
name: explain-problem-progressively
description: >-
  Breaks down any LeetCode or GeeksforGeeks problem from brute force to the optimal solution
  for a complete beginner. Never skips steps. Explains time/space complexity in plain English
  at every stage. Saves the full progressive explanation to 3.understand/{number}.{source}.md.
  Use when: explain this problem, walk me through this, how do I solve this,
  break this down, what is brute force, show me optimal solution, teach me step by step.
argument-hint: 'Required: problem number and source, e.g. "1 leetcode" or paste the problem statement'
user-invocable: true
---

# Explain Problem Progressively

Walk through any DSA problem **from brute force to optimal** in a structured, beginner-friendly manner. This skill never jumps straight to the clever solution — it builds understanding by showing *why* each improvement matters and *what limitation* it overcomes.

## When to Use

- A user presents a new problem and asks how to solve it
- A user is stuck and needs the thought process, not just the answer
- A user wants to understand *why* a hash map is better than a nested loop
- Introducing any problem for the first time

---

## Procedure

### Step 0 — Understand the Problem First

Before any solution, restate the problem in the simplest possible terms:

> "In plain English: given {input}, find {output}. The trick is {key constraint}."

Then walk through the given examples manually:
- Show exactly what happens with Example 1 using the input values
- Point out any edge cases visible in the constraints (empty input, single element, negatives, duplicates)

---

### Step 1 — Approach 1: Brute Force

**Always start here, even if it's obviously inefficient.**

Structure:

#### 1.1 The Idea (Before Any Code)

Explain the approach in plain English first. Use a concrete analogy if helpful.

> "The simplest idea is to check every possible {thing} and see if it {satisfies the condition}. Think of it like trying every key on a keyring until one opens the lock."

#### 1.2 Visual Walkthrough

Manually trace through Example 1 step by step using the brute force approach. Show the state at each step using a table, list, or annotated trace — not just the final result.

```
nums = [2, 7, 11, 15], target = 9

Step 1: Pick nums[0] = 2. Try pairing with nums[1] = 7. 2 + 7 = 9 ✓ Found!
```

#### 1.3 The Code

Present the full brute force implementation with line-by-line comments.

```python
def two_sum_brute(nums: list[int], target: int) -> list[int]:
    """
    Approach: Brute Force (Nested Loops)
    Time Complexity : O(n²) — check every pair
    Space Complexity: O(1)  — no extra storage used
    """
    # Outer loop: pick the first number of the pair
    for i in range(len(nums)):
        # Inner loop: try every number after position i as the second number
        for j in range(i + 1, len(nums)):
            # If the two numbers add up to the target, we found the answer
            if nums[i] + nums[j] == target:
                return [i, j]
```

#### 1.4 Complexity Analysis (Plain English)

Explain complexity without assuming the learner knows Big O notation:

> **Time: O(n²)** — For a list of 10 numbers, we might check up to 10 × 10 = 100 pairs. For 1,000 numbers, up to 1,000,000 pairs. It gets slow very fast.
>
> **Space: O(1)** — We're not creating any extra lists or dictionaries — just two loop counters. This is great.

#### 1.5 The Flaw

Clearly explain why this approach is not good enough:

> "This works, but it's too slow for large inputs. LeetCode would accept this for small test cases, but on 10,000 numbers it would time out. We need a smarter approach."

---

### Step 2 — Approach 2: [Intermediate Improvement, if applicable]

Not every problem has a middle step. Include this section only if there is a meaningful intermediate optimization (e.g., sorting before two pointers, using a set before a map).

Follow the same structure as Approach 1:
1. The Idea (plain English + analogy)
2. Visual Walkthrough
3. The Code (fully commented)
4. Complexity Analysis (plain English)
5. The Remaining Flaw (why we can still do better)

---

### Step 3 — Approach N: Optimal Solution

Present the most efficient known solution.

Follow the same structure as Approach 1, but replace "The Flaw" with:

#### The Win

Summarize *exactly* what improved and why:

> **What changed:** Instead of searching backward through the whole array, we pre-stored every number in a hash map. Lookup is now instant (O(1)) instead of linear (O(n)).
>
> **Net result:** We went from O(n²) to O(n) time — exponentially faster for large inputs.

---

### Step 4 — Side-by-Side Comparison

After all approaches, present a clean summary table:

| Approach       | Time     | Space | When to Use |
|----------------|----------|-------|-------------|
| Brute Force    | O(n²)    | O(1)  | Never in production; good for understanding |
| [Intermediate] | O(n log n)| O(1) | When extra space is constrained |
| Hash Map       | O(n)     | O(n)  | Default choice for most lookup problems |

---

### Step 5 — Save to `3.understand/`

**Always save the full progressive explanation to disk** at `3.understand/{number}.{source}.md` after completing Steps 0–4.

This file is the permanent, structured record of how this problem was taught. It is referenced by the `teach-dsa-from-history` skill and linked from `index.md`.

**File template for `3.understand/{number}.{source}.md`:**

````markdown
---
title: "{Problem Title} — Progressive Explanation"
number: {question_number}
source: {source}
difficulty: {Easy|Medium|Hard}
tags: [{tag1}, {tag2}]
primary_concept: {main DSA concept taught, e.g. "Two Pointers"}
date_explained: {YYYY-MM-DD}
---

# {question_number}. {Problem Title} — Progressive Explanation

## Plain English Summary

> In plain English: given {input}, find {output}. The trick is {key constraint}.

## Example Walkthrough

{Manually trace through Example 1 step by step}

---

## Approach 1: Brute Force

### The Idea
{Plain-English description + analogy}

### Visual Trace
{Step-by-step manual walkthrough table or annotated trace}

### Code
```python
{Full brute force implementation with line-by-line comments}
```

### Complexity
- **Time:** O({?}) — {plain-language explanation}
- **Space:** O({?}) — {plain-language explanation}

### The Flaw
{Why this approach is not good enough for large inputs}

---

## Approach {N}: {Intermediate or Optimal Name}

{Repeat structure above for each additional approach}

---

## Side-by-Side Comparison

| Approach | Time | Space | When to Use |
|----------|------|-------|-------------|
| Brute Force | O(?) | O(?) | Understanding only |
| {Intermediate} | O(?) | O(?) | Space-constrained |
| {Optimal} | O(?) | O(?) | Default choice |

## Key Insight

> {The single "aha moment" that makes the optimal solution click}

## Related Files

- Problem: [[1.questions/{number}.{source}|{Problem Title}]]
- Solutions: {comma-separated wikilinks to 2.answers/ files}
- Concept Lesson: [[study/{concept_slug}|{Concept Name} — Study Note]]
````

---

### Step 6 — Concept Hook

After completing the explanation, identify the *primary concept* demonstrated by the optimal solution and offer to teach it:

> "This problem teaches a technique called **hash map lookup**. It comes up in dozens of problems. Want me to explain hash maps in depth and show you other problems where this pattern applies?"

If the user says yes, hand off to the `teach_dsa_from_history` skill.

---

## Explanation Quality Standards

- **Never paste code without explaining it first** — always describe the idea before showing implementation
- **Never assume the learner knows Big O** — always translate complexity into plain English ("10 operations vs 10,000 operations")
- **Always show at least one manual trace** — abstract explanations don't stick; walking through an example does
- **Keep each approach self-contained** — the learner should be able to understand Approach 1 without reading Approach 2
- **Use consistent variable names** across all approaches for a given problem — don't rename `nums` to `arr` halfway through
- **Highlight the "aha moment"** — the single insight that makes the optimal solution click (e.g., "the key insight is that we're searching for a complement, not just any pair")
- **Always save to `3.understand/`** — every explanation session must produce a file on disk; never only explain in chat

---

## Tone

- Acknowledge that the brute force is a valid starting point: "This is how most people think about it first — and that's exactly right."
- Frame optimizations as natural evolution: "Now that we see the bottleneck, let's ask: is there a faster way to do this one step?"
- Never say "obviously" or "trivially" — nothing is obvious to a beginner.
