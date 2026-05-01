# Claude Configuration for DSA Learning

Welcome to the Claude-specific configuration for your Data Structures and Algorithms learning repository.

## Overview
This configuration optimizes your DSA repository for use with **Claude Code** and **Claude Desktop**, providing agents and skills tailored to Claude's deep code understanding and interactive capabilities.

## Available Agents

### 1. Claude-DSA-Agent
Comprehensive agent for structured learning:
- Progressive explanations from brute force to optimal
- Multiple solution approaches for each problem
- Deep code analysis and understanding
- Knowledge base building and linking

**When to use:** Learning algorithms from first principles, understanding complex problems step-by-step

### 2. Claude-Code-Helper
Implementation-focused agent:
- Rapid problem-solving
- Code debugging and optimization
- Implementation guidance
- Test case generation

**When to use:** Implementing algorithms quickly, debugging code, optimizing solutions

## Available Skills

### Claude-Progressive-Teaching
Break down any DSA problem from brute force to optimal:
- Step-by-step explanations
- Time/space complexity analysis
- Real execution traces
- Cross-problem references

### Claude-Documentation
Keep your repository organized:
- Automatic file naming
- Problem documentation
- Solution organization
- Knowledge base updates

## Quick Start

1. **Learning a new algorithm:**
   ```
   "Explain the two-pointer technique step by step"
   ```
   Claude-DSA-Agent will provide a comprehensive guide.

2. **Implementing a solution:**
   ```
   "Implement a solution for the sliding window problem"
   ```
   Claude-Code-Helper will generate clean, working code.

3. **Understanding execution:**
   ```
   "Show me how the KMP algorithm executes on this string"
   ```
   Get detailed step-by-step explanation with complexity analysis.

## Directory Structure
- `claude.instructions.md` - Detailed repository conventions
- `agents/` - Claude-specific agents
- `skills/` - Claude-specific skills

## Next Steps
- Start with `claude.instructions.md` for detailed conventions
- Choose an agent based on your current task
- Use skills to automate documentation and learning

---
For platform-specific configurations, see `.github/`, `.antigravity/`, and `.gemini/`
