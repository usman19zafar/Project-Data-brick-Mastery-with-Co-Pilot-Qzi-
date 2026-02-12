Module 1.1 — Validation Required
We must confirm:

Notebook runs without cluster errors

Markdown + Python + SQL all execute

Output cells appear

Evidence needed:  
A screenshot or copy/paste of the output cells.

Module 1.2 — Validation Required
We must confirm:

Raw → cleaned → aggregated → written

Parquet + Delta files created

df.explain() output captured

Evidence needed:

Output of df_raw.show()

Output of df_clean.show()

Output of df_agg.show()

Output of df_agg.explain()

Confirmation that Parquet + Delta paths exist

Module 1.3 — Validation Required
We must confirm:

Delta table created

CRUD operations executed

Time travel versions exist

Table registered

Evidence needed:

Output of df.show()

Output of CRUD results

Output of history.show()

Output of version 0 + latest version

HOW WE VALIDATE (MECHANICAL, ZERO DRIFT)
Step 1 — You run each notebook in Databricks
(You already have the files.)

Step 2 — You paste the outputs here
Just the text output is enough.
Screenshots optional.

Step 3 — I verify each KPI one by one
I will mark:

Code
KPI‑X — VALIDATED
or

Code
KPI‑X — FAILED (fix required)
Step 4 — Once all KPIs are validated
I will update:

Level 1 README

KPIs_Level1.md

Module READMEs

with validated status, not just “posted”.

Step 5 — Only then we proceed to Level 2
This keeps your repo professional, auditable, and portfolio‑grade.
