Level 1 — Foundations
Objective
Establish core skills in Databricks:

Workspace navigation

Notebook execution

Spark DataFrames

Delta Lake fundamentals

CRUD + time travel

Your own dataset stored as Delta

Level 1 ensures you can operate independently inside Databricks before moving into workflows, pipelines, and advanced engineering.

Modules Overview
Module 1.1 — Workspace + Notebooks
Focus:

Create cluster

Create notebooks

Run %md, %python, %sql

Deliverable:

Mixed‑language notebook

KPIs:

Notebook runs without cluster errors

Notebook mixes markdown + code + results

Module 1.2 — Spark DataFrames
Focus:

Read raw data

Transform with select/filter/withColumn/groupBy/agg

Write Parquet + Delta

Explain plan

Deliverable:

sample_etl_demo.py

KPIs:

Mini ETL: raw → cleaned → aggregated → written

Explain plan interpreted

Module 1.3 — Your Own Delta Dataset
Focus:

Create synthetic dataset

Write Delta

Register table

CRUD operations

Time travel

Deliverables:

01_generate_delta_dataset.py

02_transform_and_crud.py

KPIs:

Delta table created

CRUD validated

Time travel validated

Table registered

Completion Status

```code
+------------+-------------+
|  Module    |   Status    |
+------------+-------------+
| Module 1.1 | ✔ Complete  |
| Module 1.2 | ✔ Complete  |
| Module 1.3 | ✔ Complete  |
+------------+-------------+
```
Level 1 is now fully satisfied and ready for Level 2 progression.
