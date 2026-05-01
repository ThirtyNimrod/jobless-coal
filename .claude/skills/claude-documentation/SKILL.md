---
name: claude-problem-documentation
description: >
  Saves LeetCode and GeeksforGeeks problems and solutions into structured
  directories with proper naming. Use when: "save this problem", "document solution",
  "save code", "record this question", "persist my solutions".
---

# Claude Problem Documentation

## Purpose
Maintain a well-organized repository of DSA problems, solutions, and explanations across four directories.

## Directory Structure
- **1.questions/**: Problem descriptions with constraints and examples
- **2.answers/**: Python solutions with multiple approaches per problem
- **3.understand/**: Progressive explanations from brute force to optimal
- **study/**: Concept lessons and pattern documentation

## Naming Conventions
- Problems: `{problem_id}.{source}.md` (e.g., `28.leetcode.md`)
- Solutions: `{problem_id}.{source}.{approach}.py` (e.g., `28.leetcode.kmp.py`)
- Explanations: `{problem_id}.{source}.md`
- Concepts: `{concept_name}.md`

## File Contents
- **Problem files**: Complete statement, constraints, examples, edge cases
- **Solution files**: Well-commented code with approach explanation and complexity
- **Explanation files**: Progressive breakdown with multiple solution approaches
- **Concept files**: Generalized patterns and techniques

## Usage Examples
- "Save this LeetCode problem and two solutions"
- "Document the KMP algorithm approach"
- "Create a problem file for problem 28"
