## Agentic Loop Architecture

The Guided Component Architect is built using an **agentic workflow**, where the system autonomously generates, evaluates, and improves code without human intervention. Instead of a single-pass generation, the system follows a controlled feedback loop to ensure governed and valid output.

### Workflow
User Prompt
   ->
LLM Generator
   ->
Linter Agent (Validation)
   ->
If errors detected -> Self-Correction Loop -> LLM Regeneration
   ->
Final Valid Angular Component


### Step-by-Step Process

1. **User Prompt**
   - The user provides a natural language description (e.g., *"Login card with glassmorphism effect"*).

2. **LLM Generator**
   - The Generator uses prompt engineering to produce **raw Angular/Tailwind code only**.
   - The predefined design system (`tokens.json`) is injected into the prompt to guide styling and structure.

3. **Linter Agent (Validator)**
   - The generated code is analyzed using rule-based validation.
   - The Linter checks:
     - Design token compliance (color, border radius, font)
     - Syntax correctness (balanced brackets)
     - HTML structure validity (no unclosed tags)

4. **Self-Correction Loop**
   - If validation fails, structured error logs are automatically passed back into the Generator.
   - The LLM regenerates the component using these error messages.
   - This creates an **autonomous self-healing loop** that improves output quality.

5. **Final Output**
   - Once validation passes, the corrected Angular component is returned as the final result.

### Key Characteristics of the Agentic Loop

- **Autonomous** — No manual correction required
- **Governed** — Enforces predefined design system
- **Reliable** — Automatically fixes invalid output
- **Structured** — Uses modular Generator + Validator architecture
- **Iterative** — Improves output through feedback

### Why This Matters

This agentic architecture moves beyond simple chat-based generation and enables **controlled, production-aligned code generation**, similar to modern AI development platforms such as Lovable and Bolt.
