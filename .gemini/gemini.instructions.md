# Repository Instructions for Google Gemini

## Purpose
This repository is dedicated to documenting and teaching Data Structures and Algorithms (DSA) using Python. It follows a structured approach to organize problems, solutions, explanations, and concept lessons.

## Directory Structure
- **1.questions/**: Contains Markdown files with problem descriptions.
- **2.answers/**: Contains Python solution files for problems. Each problem can have multiple solutions, named by the approach used (e.g., `problem_name.brute_force.py`).
- **3.understand/**: Contains progressive explanations for problems in Markdown format.
- **study/**: Contains concept lessons derived from problems and solutions.
- **index.md**: Serves as a comprehensive index linking all problems, solutions, explanations, and lessons.

## Conventions
1. **File Naming**:
   - Problem descriptions: `problem_id.source.md` (e.g., `28.leetcode.md`).
   - Solutions: `problem_id.source.approach.py` (e.g., `28.leetcode.kmp.py`).
   - Explanations: `problem_id.source.md` (e.g., `28.leetcode.md`).
   - Concept lessons: `concept_name.md` (e.g., `two_pointers.md`).

2. **Content Guidelines**:
   - Problem descriptions must include the problem statement, constraints, and examples.
   - Solutions must be well-commented, explaining the approach and time/space complexity.
   - Explanations must progressively break down the problem from brute force to optimal solutions.
   - Concept lessons must generalize patterns and techniques derived from problems.

3. **Workflow**:
   - Document problems and solutions in their respective directories.
   - Create progressive explanations for each problem in `3.understand/`.
   - Derive and document concept lessons in `study/`.
   - Update `index.md` to reflect all additions.

4. **Index Maintenance**:
   - Ensure `index.md` links to all problems, solutions, explanations, and lessons.
   - Categorize entries by topic for easy navigation.

## Gemini-Specific Features
- Leverage Google Gemini's multimodal capabilities for code analysis and visualization.
- Support for Python-native integration with Google Cloud services.
- Optimized for real-time collaboration and notebook-style learning.

## Related Customizations
- Automate `index.md` updates.
- Validate file naming conventions during commits.
- Generate templates for new problems, solutions, and explanations.
