THE EXECUTABLE PLAN (SMALL PARTS, ZERO DRIFT)
Four levels → modules → tasks → KPIs.  
You can run this as a 30‑day Databricks mastery program.

LEVEL 1 — FOUNDATIONS (Community Edition or Azure)
Objective: Spark + Delta + Notebooks + Your own dataset.

Module 1.1 — Workspace + Notebooks
Tasks

Create cluster (DBR 13.x LTS).

Create Python + SQL notebooks.

Run %python, %sql, %md.

KPIs

Notebook runs without cluster errors.

One notebook mixing markdown + code + results.

Module 1.2 — Spark DataFrames
Tasks

Read /databricks-datasets/ CSV/JSON/Parquet.

Transform: select, filter, withColumn, groupBy, agg.

Write back as Parquet + Delta.

KPIs

Mini ETL: raw → cleaned → aggregated → written.

df.explain() interpreted at high level.

Module 1.3 — Your Own Delta Dataset
Tasks

Create synthetic dataset (sales, IoT, clickstream).

Write as Delta to DBFS.

Register table with CREATE TABLE ... USING DELTA.

KPIs

One fully owned Delta table.

Update + delete + re-read to confirm.

LEVEL 2 — AUTOMATION + DELTA ADVANCED (Azure Databricks)
Objective: Workflows + Jobs + Pipelines + Time Travel.

Module 2.1 — Workflows (Jobs)
Tasks

Convert Level 1 ETL notebook into a scheduled job.

Add parameters (date, environment).

Add email/slack alerts.

KPIs

Job runs end‑to‑end without manual intervention.

Parameterized notebook executed via job.

Module 2.2 — Multi‑Task Pipeline
Tasks

Split into Bronze → Silver → Gold notebooks.

Chain tasks in one Workflow.

Add retry policies.

KPIs

3‑layer Delta pipeline automated.

Failure + retry behavior demonstrated.

Module 2.3 — Time Travel + Schema Evolution
Tasks

Update/delete data.

Query VERSION AS OF and TIMESTAMP AS OF.

Add new column via schema evolution.

KPIs

Two versions of same table visible.

Schema evolution without breaking downstream reads.

LEVEL 3 — OPTIMIZATION + DLT + UNITY CATALOG (Azure)
Objective: Managed pipelines, cost reduction, governance.

Module 3.1 — Delta Live Tables
Tasks

Create DLT pipeline (Bronze/Silver/Gold).

Add expectations (data quality rules).

Run pipeline and inspect lineage.

KPIs

One DLT pipeline runs clean.

At least one expectation enforced.

Module 3.2 — Z‑ORDER + OPTIMIZE + VACUUM
Tasks

Identify high-selectivity column.

Run OPTIMIZE ... ZORDER BY (col).

Run VACUUM with safe retention.

KPIs

Before/after query timing comparison.

Old files removed beyond retention.

Module 3.3 — Structured Streaming + Delta
Tasks

Build streaming ingest (file source or autoloader).

Write to Delta.

Connect streaming to DLT.

KPIs

Streaming job runs 10–15 minutes.

DLT consumes streaming input.

Module 3.4 — Unity Catalog
Tasks

Create catalog + schema.

Register Delta tables under UC.

Connect to Postgres/Iceberg via UC (if enabled).

KPIs

All core tables under UC.

One external table visible via UC.

LEVEL 4 — PERFORMANCE + COST + GOVERNANCE (Azure)
Objective: Architect‑level mastery.

Module 4.1 — Spark Performance
Tasks

Inspect Spark UI: stages, tasks, shuffle, skew.

Create skewed dataset and fix with salting/repartition.

KPIs

Before/after skew mitigation.

Explain Spark UI metrics.

Module 4.2 — Memory + Photon
Tasks

Tune partitions (repartition, coalesce).

Compare Photon vs non‑Photon cluster.

KPIs

Runtime or shuffle reduction.

Cost/performance comparison table.

Module 4.3 — PII Governance
Tasks

Use UC permissions to restrict access.

Implement masking/tokenization.

KPIs

Non‑privileged users see masked data.

Documented PII flow: raw → masked → analytics.

Module 4.4 — Cost Optimization + Multi‑Cloud
Tasks

Document cost levers: cluster size, autoscaling, Photon, OPTIMIZE, VACUUM.

Compare Databricks behavior across Azure vs AWS/GCP.

KPIs

One‑page cost playbook.

Multi‑cloud architecture note.
