# 📋 Stage‑1 Task Tracker

U.S. Domestic Remedy Exhaustion — Human‑Readable Workflow

This document outlines all tasks required to fully populate Stage 1: U.S. Domestic Remedy Exhaustion, including priorities, dependencies, and completion criteria. It is the human‑readable counterpart to task-tracker.json.

---

🧭 How to Use This Tracker

- High‑priority tasks establish the legal and structural foundation.  
- Medium‑priority tasks implement Python toolkits and structural analysis.  
- Dependencies ensure tasks are completed in the correct order.  
- Completion criteria define when a task is truly finished.  
- Locked tasks cannot begin until Stage‑1 exhaustion is complete.

---

⚖️ 01 — Federal Criminal Statutes

T01 — Draft Federal Statute Summaries
Deliverables: 241conspiracyrights.md, 242coloroflaw.md, 2340Atorture_extraterritorial.md  
Priority: High  
Dependencies: None  
Completion: All statute summaries drafted and internally consistent.

T02 — Build Statute Interaction Matrix
Deliverable: statuteinteractionmatrix.md  
Priority: Medium  
Dependencies: T01  
Completion: Matrix populated with cross‑statute interactions.

T03 — Implement statute_graph.py
Deliverable: statute_graph.py  
Priority: Medium  
Dependencies: T02  
Completion: Graph generation functional with roadmap.json input.

---

🏛️ 02 — Judicial Branch Constraints

T04 — Document Judicial Immunity & Administrative Acts
Deliverables: judicialimmunitymap.md, judicialvsadministrative_acts.md  
Priority: High  
Dependencies: None  
Completion: Clear separation of judicial and non‑judicial acts established.

T05 — Implement judicialmodallattice.py
Deliverable: judicialmodallattice.py  
Priority: Medium  
Dependencies: T04  
Completion: Modal lattice operational and validated.

---

🚓 03 — Municipal Policing (Washington, D.C.)

T06 — Document MPD & Mayor Nondiscretionary Duties
Deliverables: MPDnondiscretionaryduties.md, mayorhomerule_duties.md  
Priority: High  
Dependencies: None  
Completion: Duty map complete and cross‑referenced with federal statutes.

T07 — Implement nondiscretionarydutyflow.py
Deliverable: nondiscretionarydutyflow.py  
Priority: Medium  
Dependencies: T06  
Completion: Flow visualization functional and integrated with roadmap.json.

---

📝 04 — Mandamus (DC Court of Appeals)

T08 — Draft Mandamus Test & Duty Analysis
Deliverables: mandamustest.md, nondiscretionaryduty_analysis.md  
Priority: High  
Dependencies: T06  
Completion: Mandamus prerequisites mapped and linked to municipal failures.

T09 — Implement mandamusstructuraltest.py
Deliverable: mandamusstructuraltest.py  
Priority: Medium  
Dependencies: T08  
Completion: Structural test operational and validated.

---

🌍 05 — Embassy & Extraterritoriality

T10 — Document Embassy Jurisdiction & Extraterritorial Statutes
Deliverables: embassyjurisdiction.md, extraterritorialstatute_map.md  
Priority: High  
Dependencies: T01  
Completion: Extraterritoriality map complete and consistent with federal statutes.

T11 — Implement extraterritoriality_matrix.py
Deliverable: extraterritoriality_matrix.py  
Priority: Medium  
Dependencies: T10  
Completion: Matrix functional and validated with sample scenarios.

---

♿ 06 — Disability Rights & Access to Justice

T12 — Document Disability‑Rights Barriers
Deliverables: accesstojusticebarriers.md, CRPDarticle13analogues.md  
Priority: High  
Dependencies: None  
Completion: Barrier documentation complete and linked to mandamus analysis.

T13 — Implement disabilitybarriermap.py
Deliverable: disabilitybarriermap.py  
Priority: Medium  
Dependencies: T12  
Completion: Barrier map functional and integrated with roadmap.json.

---

🛡️ 07 — Human Rights Defender Protections

T14 — Document HRD Protections & Retaliation Patterns
Deliverables: HRDprotections.md, retaliationanalysis.md  
Priority: High  
Dependencies: None  
Completion: HRD documentation complete and cross‑linked with federal statutes.

T15 — Implement hrdpatterndetector.py
Deliverable: hrdpatterndetector.py  
Priority: Medium  
Dependencies: T14  
Completion: Pattern detector functional with sample timelines.

---

🔍 08 — Federal Law Enforcement Conflict Assessment

T16 — Document Compromised Pathways & Alternatives
Deliverables: compromisedpathways.md, alternativedomestic_mechanisms.md  
Priority: High  
Dependencies: T01, T06  
Completion: Conflict assessment complete and linked to exhaustion criteria.

T17 — Implement conflictsurfacedetector.py
Deliverable: conflictsurfacedetector.py  
Priority: Medium  
Dependencies: T16  
Completion: Detector functional and validated with known contradictions.

---

🌐 99 — Stage‑2 Contingency (Foreign Jurisdiction)

Locked until Stage‑1 exhaustion is complete.

T18 — Draft Stage‑2 Contingency Documentation
Deliverables: UKCJA1988section134.md, POAsection6privateprosecution.md  
Priority: Locked  
Dependencies: T01, T06, T08, T16  
Completion: Unlocked only after full Stage‑1 exhaustion.

T19 — Implement stage2geometricplanner.py
Deliverable: stage2geometricplanner.py  
Priority: Locked  
Dependencies: T18  
Completion: Activated only after Stage‑1 completion.

---

