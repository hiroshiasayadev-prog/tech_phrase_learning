# Learning path selection prompt v3: authored phrase evidence

- **prompt_id**: `conversation-learning-path-selection-v3-authored-phrase-evidence`
- **status**: current investigation prompt
- **model_role**: learning-path selector

## User prompt template

Choose one path through the supplied coarse conversation tree for an English phrase-learning session.

The tree is an approximate traversal structure, not a claim that every projected edge is an explicit reply. Each summary and phrase candidate was generated from or validated against the current author's own text after quoted blocks were removed.

Choose a path that:

- starts at the opening post;
- follows parent-to-child edges in the supplied coarse tree;
- contains between 2 and 6 posts;
- has a broadly understandable conversational flow;
- contains useful disagreement, clarification, qualification, evaluation, or collaboration language;
- gives strong weight to reusable source-verified phrase candidates;
- avoids unnecessary code-heavy or detail-heavy branches;
- remains light enough for phrase learning rather than deep technical reading.

Do not choose a path merely because it is longest or most technically informative. Do not invent relationships. Do not list a selected post in `rejected_alternatives`. Every rejected alternative must be an unselected post from the supplied tree.

Return one JSON object matching the supplied JSON schema.

## Input

{{TREE_INPUT_JSON}}
