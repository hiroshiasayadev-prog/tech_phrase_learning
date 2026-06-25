# Learning path selection prompt v2: phrase evidence

- **prompt_id**: `conversation-learning-path-selection-v2-phrase-evidence`
- **status**: preserved experiment prompt
- **model_role**: learning-path selector

## User prompt template

Choose one path through the supplied coarse conversation tree for an English phrase-learning session.

The tree is an approximate traversal structure. It is not a claim that every projected edge is an explicit source reply.
Each post summary is generated from the authentic source and may omit technical detail.

Choose a path that:

- starts at the opening post;
- follows parent-to-child edges in the supplied coarse tree;
- contains between 2 and 6 posts;
- has a broadly understandable conversational flow;
- contains useful disagreement, clarification, qualification, evaluation, or collaboration language;
- prefers posts with strong source-verified reusable phrase candidates;
- avoids unnecessary code-heavy or detail-heavy branches;
- is light enough for phrase learning rather than deep technical reading.

Do not choose a path merely because it is longest.
Do not invent relationships that are not present in the supplied tree.
Do not list a selected post in `rejected_alternatives`.
Every rejected alternative must be an unselected post from the supplied tree.
Use the exact phrase candidates as evidence when comparing learning value.
Return one JSON object matching the supplied JSON schema.

## Input

{{TREE_INPUT_JSON}}
