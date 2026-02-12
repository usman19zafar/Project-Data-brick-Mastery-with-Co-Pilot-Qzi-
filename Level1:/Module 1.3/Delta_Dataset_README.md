Module 1.3 — Your Own Delta Dataset
Objective
Create your own fully owned Delta dataset, perform CRUD operations, and validate time‑travel behavior.
This module establishes your foundational Delta Lake skills before moving into workflows, DLT, and governance.

Tasks
1. Create Synthetic Dataset
Generate a deterministic dataset (sales, IoT, clickstream, or categorical numeric).
Notebook 1 (01_generate_delta_dataset.py) produces:

Schema definition

Synthetic data generation

DataFrame creation

Delta write to DBFS

2. Register Delta Table
Use:

Code
CREATE TABLE ... USING DELTA LOCATION ...
This makes the dataset queryable from SQL and accessible to downstream modules.

3. Perform CRUD Operations
Notebook 2 (02_transform_and_crud.py) performs:

UPDATE

DELETE

INSERT (via MERGE)

Re‑read validation

4. Validate Time Travel
Use:

deltaTable.history()

versionAsOf

Read version 0

Read latest version

This confirms Delta versioning and ACID behavior.

KPIs (Success Criteria)
```Code
+--------+--------------------------------------------------------------+
|  KPI   | Description                                                  |
+--------+--------------------------------------------------------------+
| KPI-5  | One fully owned Delta table created                          |
| KPI-6  | Update + delete + re-read operations validated               |
| KPI-7  | Multiple versions created and time travel confirmed          |
| KPI-8  | Table registered with CREATE TABLE USING DELTA               |
+--------+--------------------------------------------------------------+
```
All KPIs must be satisfied for Module 1.3 completion.

Delivered Artifacts
Notebook 1 — 01_generate_delta_dataset.py
Synthetic dataset

Delta write

Table registration

Preview output

Notebook 2 — 02_transform_and_crud.py
CRUD operations

MERGE insert

Time travel

Version validation

Both notebooks are deterministic and Databricks‑ready.

Completion Status
✔ Notebook 1 saved
✔ Notebook 2 saved
✔ All KPIs satisfied
✔ Module 1.3 complete
