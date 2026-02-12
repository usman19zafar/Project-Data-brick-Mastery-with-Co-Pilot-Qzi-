Module 1.1 — Workspace & Notebooks
Objective
Establish core Databricks workspace skills:

Creating clusters

Creating notebooks

Running Python, SQL, and Markdown in a single workflow

This module ensures you can operate inside the Databricks environment without errors before moving into Spark DataFrames and Delta Lake.

Tasks
1. Create Cluster
Runtime: DBR 13.x LTS

Mode: Single Node or Standard

Language: Python

2. Create Notebooks
One Python notebook

One SQL notebook

Or a single mixed notebook containing all three:

%md

%python

%sql

3. Execute Basic Commands
Markdown cell

Python DataFrame creation

SQL query using a temp view

KPIs (Success Criteria)
KPI	Description
KPI‑1	Notebook runs without cluster errors
KPI‑2	Notebook mixes markdown + code + results in a clean sequence
Both KPIs must be satisfied for Module 1.1 to be considered complete.
```code
+--------+--------------------------------------------------------------+
|  KPI   | Description                                                  |
+--------+--------------------------------------------------------------+
| KPI-1  | Notebook runs without cluster errors                         |
| KPI-2  | Notebook mixes markdown + code + results in a clean sequence |
+--------+--------------------------------------------------------------+
```
Delivered Artifact
Notebook: module_1_1_workspace_notebooks.py
Contents include:

Markdown introduction

Python DataFrame creation + display

SQL query using %sql

Clean output cells

This notebook satisfies all Module 1.1 tasks and both KPIs.

Completion Status
✔ Module 1.1 tasks completed
✔ KPI‑1 satisfied
✔ KPI‑2 satisfied

Module 1.1 is now ready for Level 1 integration.
