# VISUALGRAMMARDEVELOPER_NOTE.md

Developer Note — Structural Grammar Specification & Integration

1. Purpose of This Note
This Developer Note defines the structure, semantics, and evolution rules for the visual grammar subsystem used in the Stage‑1 domestic‑remedy exhaustion repository.

It explains:

- what the visual grammar represents  
- how it integrates with loader.py  
- how geometric primitives are used structurally  
- how operators behave in this repo  
- how to maintain the boundary with AI interpretability work  

This note is developer‑facing and should not be included in public documentation.

---

2. What the Visual Grammar Represents
The visual grammar is a structural representation layer for:

- jurisdictional flows  
- nondiscretionary duty interactions  
- procedural dependencies  
- collapse surfaces (structural contradictions)  
- activation conditions for Stage‑2  

It is not an AI interpretability grammar.

It is a mapping tool that helps developers understand:

- how layers relate  
- where flows converge  
- where contradictions occur  
- how tasks and documentation interlock  

The grammar is descriptive, not prescriptive.

---

3. JSON Grammar Specification
The grammar uses four primitive types:

Node
A discrete structural unit representing:

- a layer  
- a duty cluster  
- a statute set  
- a jurisdictional domain  

Nodes correspond directly to roadmap layers.

Edge
A directional relationship between nodes representing:

- duty flows  
- dependencies  
- jurisdictional interactions  
- procedural pathways  

Edges correspond to structural flows, not legal advice.

Surface
A region where multiple edges converge, representing:

- collapse points  
- contradictions  
- structural failures  
- exhaustion bottlenecks  

Surfaces are used to identify where procedural remedies break down.

Operator
A geometric transformation applied to nodes, edges, or surfaces to reveal structure.

Operators in this repo are structural, not interpretability‑based.

---

4. Integration With loader.py
The visual grammar integrates with loader.py in three ways:

1. Structural Validation
loader.py ensures:

- all nodes correspond to real layers  
- all edges reference valid nodes  
- all surfaces reference valid node sets  
- all operators are defined in the grammar  

2. Repository State Mapping
loader.py can be extended to:

- check which deliverables exist  
- check which toolkits exist  
- map missing documentation to nodes  
- map missing toolkits to operators  

3. Future Operator Execution
As structural operators are implemented:

- holonomy loops  
- modal lattice separation  
- collapse‑surface detection  
- spectral bundle mapping  

loader.py will serve as the entry point for running them.

---

5. Operator Semantics (Structural Only)

Holonomy Operator
Detects loops in jurisdictional flows, such as:

- municipal → judicial → municipal  
- federal → municipal → federal  

Used to identify circular remedy pathways.

Modal Lattice Operator
Separates:

- judicial acts  
- administrative acts  

Used to clarify mandamus prerequisites.

Collapse Surface Detector
Identifies structural contradictions, such as:

- nondiscretionary duties unmet  
- procedural barriers blocking remedies  
- federal conflicts preventing enforcement  

Spectral Bundle Operator
Maps interactions between:

- federal statutes  
- municipal duties  
- extraterritorial constraints  

Used to understand cross‑layer interactions.

These operators are structural metaphors, not AI interpretability tools.

---

6. Evolution Rules
To maintain consistency:

Nodes
- must correspond to roadmap layers  
- must not represent runtime or interpretability concepts  

Edges
- must represent procedural or jurisdictional flows  
- must not represent latent‑space or model‑behavior flows  

Surfaces
- must represent structural contradictions  
- must not represent AI collapse surfaces  

Operators
- must remain procedural  
- must not import interpretability semantics  
- must not reference Shared‑Horizon membranes  

Versioning
- grammar_version must increment when primitives change  
- operators must be documented before implementation  
- surfaces must be justified by structural analysis  

---

7. Boundary With AI Interpretability
This grammar is not part of:

- CAUSA  
- CMR  
- Shared‑Horizon  
- NDH expressive layers  
- spectral truth alignment  
- runtime membranes  
- collapse‑surface detectors for model behavior  

It uses geometric primitives only for structural clarity.

The ontology is procedural, not computational.

---

8. Summary
The visual grammar is:

- structural  
- procedural  
- documentary  
- geometric in style  
- non‑interpretive  
- non‑runtime  
- non‑AI  

It provides a clear representation of:

- jurisdictional flows  
- duty interactions  
- collapse surfaces  
- activation conditions  

while maintaining a strict boundary from system‑agnostic AI interpretability.

---

