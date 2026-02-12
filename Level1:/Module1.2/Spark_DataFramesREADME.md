Module 1.2 — Spark DataFrames
Objective
Build a small, deterministic ETL pipeline using Spark DataFrames.
You will read raw data, transform it, and write it back as Parquet and Delta.

This module establishes your baseline Spark fluency before moving into Delta CRUD and time travel.

Tasks
1. Read Raw Data
Use Databricks sample datasets:

/databricks-datasets/learning-spark-v2/people/people-10m.delta

/databricks-datasets/airlines/part-00000

Supported formats:

CSV

JSON

Parquet

2. Transform Data
Apply core DataFrame operations:

select()

filter()

withColumn()

groupBy()

agg()

3. Write Outputs
Write transformed data to DBFS:

Parquet output

Delta output

KPIs (Success Criteria)
```Code
+--------+--------------------------------------------------------------+
|  KPI   | Description                                                  |
+--------+--------------------------------------------------------------+
| KPI-3  | Mini ETL: raw → cleaned → aggregated → written               |
| KPI-4  | df.explain() interpreted at a high level                     |
+--------+--------------------------------------------------------------+
```
Both KPIs must be satisfied for Module 1.2 completion.

Delivered Artifact
Script: sample_etl_demo.py
This script performs:

Raw read

Transformations

Aggregation

Parquet + Delta writes

Explain plan

Completion Status
Pending execution and validation.
