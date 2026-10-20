# STRUCTURALBATCHINGNOTE.md

Developer Note — Structural File Batching and Expansion Sequence

1. Purpose
This note documents the batching structure for the 30+ Stage‑1 structural files.  
It explains:

- how files are grouped  
- why the groups exist  
- the order in which they must be created  
- how they relate to unlock logic  
- why they are not toolkit dependencies  

This prevents architectural drift and ensures contributors follow the correct expansion sequence.

---

2. Why Batching Exists
The structural files correspond to:

- nodes  
- edges  
- surfaces  
- operator outputs  
- structural reports  
- Stage‑1 summaries  

These must be created in a specific order so that:

- unlock logic can evaluate completeness  
- toolkit diagnostics can run safely  
- operators have stable documentation targets  
- contributors do not create files prematurely  

Batching enforces this order.

---

3. The Six Batches (Canonical)

Batch 1 — Layer Files
Documentation for each node.

Batch 2 — Surface Files
Documentation for collapse surfaces.

Batch 3 — Flow Files
Documentation for edges.

Batch 4 — Operator Output Templates
Human‑readable locations for operator results.

Batch 5 — Structural Reports
System‑level summaries.

Batch 6 — Stage‑1 Summary Files
Final checkpoint before unlock logic evaluates Stage‑2 readiness.

---

4. Why These Are Not Toolkit Dependencies
The .py Toolkit must remain independent from:

- documentation structure  
- batching rules  
- contributor workflow  
- file naming conventions  

Toolkit modules operate only on:

- grammar  
- operators  
- structural outputs  
- unlock logic conditions  

They do not depend on documentation batching.

This separation ensures:

- runtime stability  
- safe evolution  
- clear boundaries  
- predictable behavior  

---

5. Machine‑Readable Version
A .json version of this batching map will be created:

`
structural_batches.json
`

It will be used by:

- diagnostics  
- consistency checker  
- unlock logic completeness checks  
- future automation  

It will not be used by operators or loader.

---

6. Summary
This Developer Note defines the batching structure for Stage‑1 expansion.  
It ensures contributors follow the correct sequence and keeps the toolkit independent from documentation organization.

---

