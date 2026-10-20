# 📐 Visual Grammar — Stage‑1 Structural Representation

Human‑Readable Companion to visual‑grammar.json

The visual grammar provides a structural map of the Stage‑1 domestic‑remedy exhaustion project.  
It uses geometric primitives — nodes, edges, surfaces, and operators — to make complex procedural systems cognitively tractable.

This grammar is descriptive, non‑legal, and non‑interpretive.  
It is not part of the system‑agnostic AI interpretability spine.

---

🧩 1. Grammar Primitives

🔹 Node
A discrete structural unit representing a jurisdictional or procedural domain.

🔸 Edge
A directional relationship showing how duties, constraints, or flows connect nodes.

🟪 Surface
A region where multiple edges converge, revealing structural contradictions or collapse points.

⚙️ Operator
A geometric transformation applied to nodes/edges/surfaces to reveal structure.  
Operators here are procedural, not AI‑interpretive.

---

🏛️ 2. Nodes (Structural Units)

| Emoji | Node ID | Layer | Description |
|-------|---------|--------|-------------|
| 🏛️ | N01 | 01federalstatutes | Federal criminal statutes relevant to duty flows and exhaustion. |
| ⚖️ | N02 | 02judicialbranch_constraints | Judicial immunity, administrative acts, and structural constraints. |
| 🚓 | N03 | 03municipalpolicing_DC | MPD nondiscretionary duties and DC Home Rule obligations. |
| 📝 | N04 | 04mandamusDCCourtof_Appeals | Mandamus prerequisites and structural tests. |
| 🌍 | N05 | 05embassyextraterritoriality | Embassy jurisdiction and extraterritorial statute mapping. |
| ♿ | N06 | 06disabilityrights | Access‑to‑justice barriers and disability‑rights constraints. |
| 🛡️ | N07 | 07humanrights_defender | HRD protections and retaliation pattern documentation. |
| 🔍 | N08 | 08federalLEconflictassessment | Assessment of compromised federal enforcement pathways. |
| 🔒 | N09 | 99stage2contingency | Locked foreign‑jurisdiction contingency layer. |

---

🔗 3. Edges (Directional Flows)

📤 Duty & Statute Flows
- N01 → N03 — Federal statutes impose nondiscretionary enforcement duties on municipal actors.  
- N03 → N04 — Municipal failures create conditions for mandamus review.  
- N02 → N04 — Judicial constraints shape mandamus viability.

🌐 Extraterritorial Flows
- N01 → N05 — Federal statutes define extraterritorial applicability for embassy conduct.

♿ Access‑Barrier Flows
- N06 → N04 — Disability barriers affect access to mandamus and procedural remedies.

🛡️ HRD & Conflict Flows
- N07 → N08 — HRD retaliation patterns inform federal LE conflict assessment.  
- N08 → N04 — Federal LE conflicts influence mandamus pathways.

🔒 Stage‑2 Activation Conditions
- N01 → N09 — Federal statute exhaustion required.  
- N04 → N09 — Mandamus exhaustion required.

---

🗺️ 4. Surfaces (Collapse Regions)

🟦 S01 — Municipal Collapse Surface
Nodes: N03, N04, N06  
Represents the intersection of:

- municipal nondiscretionary duties  
- mandamus prerequisites  
- disability‑rights barriers  

This surface identifies structural contradictions in municipal enforcement.

---

🟥 S02 — Federal Conflict Surface
Nodes: N01, N07, N08  
Represents the convergence of:

- federal statutes  
- HRD retaliation patterns  
- federal LE conflicts  

This surface highlights compromised federal enforcement pathways.

---

🟩 S03 — Extraterritoriality Surface
Nodes: N01, N05  
Represents the mapping between:

- extraterritorial statutes  
- embassy jurisdiction  

This surface clarifies cross‑border applicability constraints.

---

⚙️ 5. Operators (Structural Transformations)

🔄 Holonomy Operator
Detects jurisdictional loops such as:

- municipal → judicial → municipal  
- federal → municipal → federal  

Used to identify circular remedy pathways.

---

🔳 Modal Lattice Operator
Separates:

- judicial acts  
- administrative acts  

Used to clarify mandamus prerequisites and structural boundaries.

---

💥 Collapse Surface Detector
Identifies structural contradictions such as:

- unmet nondiscretionary duties  
- procedural barriers  
- enforcement conflicts  

Used to map exhaustion failures.

---

🔗 Spectral Bundle Operator
Maps interactions between:

- federal statutes  
- municipal duties  
- extraterritorial constraints  

Used to understand cross‑layer structural relationships.

---

🔒 6. Activation Rules (Stage‑2 Contingency)

Stage‑2 remains locked until:

- all Stage‑1 tasks are complete  
- all nondiscretionary duty flows are documented  
- all collapse surfaces are mapped  
- mandamus pathways are fully exhausted  

Only then can N09 (foreign‑jurisdiction contingency) activate.

---

📘 7. Relationship to Other Repo Files

JSON Grammar
visual-grammar.json  
Machine‑readable structural representation.

Developer Notes
devnotes/PROJECTSCOPE_NOTE.md  
Defines project identity and boundaries.

devnotes/VISUALGRAMMARDEVELOPERNOTE.md  
Defines grammar semantics and evolution rules.

Loader
loader.py  
Operationalizes roadmap + task tracker + grammar.

---

📚 8. Summary

The visual grammar provides:

- a clear structural map  
- a geometric representation of procedural flows  
- a way to understand collapse surfaces  
- a foundation for operator stubs  
- a bridge between documentation and tooling  

It is structural, procedural, and non‑interpretive.

---

