Level 1 – Databricks + Spark + Delta fundamentals
Module 1.1 – Workspace and notebooks
Goal: Be fluent in basic Databricks navigation and notebooks.

Tasks:

Create workspace assets:

Create a cluster (or SQL warehouse) with sensible defaults (autoscaling on, DBR LTS runtime).

Create a notebook in Python and another in SQL.

Notebook basics:

Run cells, attach/detach cluster, use %sql, %python, %md.

KPIs:

KPI-1: Create and run 2 notebooks (Python + SQL) without cluster errors.

KPI-2: Demonstrate markdown + code + results in a single notebook as a mini report.

Module 1.2 – Spark DataFrames and basic transformations
Goal: Comfort with Spark DataFrame lifecycle.

Tasks:

Read sample data:

Use built-in datasets (e.g., /databricks-datasets/), read CSV/JSON/Parquet into DataFrames.

Transform:

select, filter, withColumn, groupBy, agg, orderBy.

Write:

Write DataFrames back as Parquet and Delta to your own path (e.g., /mnt/... or dbfs:/FileStore/...).

KPIs:

KPI-3: Implement a mini ETL: read raw CSV → clean → aggregate → write as Parquet.

KPI-4: Show df.explain() and interpret at least the high-level plan (logical vs physical).

Module 1.3 – Delta as default data lake format
Goal: Treat Delta as the default storage format.

Tasks:

Create your own Delta dataset:

Start from a small synthetic dataset (e.g., sales, IoT, clickstream).

Write it as Delta: format("delta").save(path) and CREATE TABLE ... USING DELTA LOCATION ....

CRUD operations:

Insert, update, delete rows in a Delta table.

KPIs:

KPI-5: One fully owned Delta table (schema you designed, path you chose, table registered).

KPI-6: Demonstrate an update and delete on that table and re-read to confirm changes.

Level 2 – Databricks Workflows + Delta advanced features
Module 2.1 – Databricks Workflows: jobs and tasks
Goal: Automate notebooks as jobs.

Tasks:

Create a job:

Turn your Level 1 ETL notebook into a scheduled job.

Configure cluster, parameters, email/slack alerts (if available).

Multi-task job:

Split logic into 2–3 notebooks (ingest, transform, publish) and chain them in a single job.

KPIs:

KPI-7: One job that runs end-to-end without manual intervention.

KPI-8: At least one parameterized notebook (e.g., date, environment) used in a job.

Module 2.2 – Databricks Workflows + Spark in unison
Goal: Treat Spark code and Workflows as a single system.

Tasks:

Pipeline pattern:

Ingest → Bronze Delta → Silver Delta → Gold Delta using separate tasks.

Error handling:

Add simple retry policies and failure notifications.

KPIs:

KPI-9: A 3-layer Delta pipeline (Bronze/Silver/Gold) orchestrated by a single Workflow.

KPI-10: Demonstrate a failed run and show how retries/alerts behave.

Module 2.3 – Delta time travel and schema evolution
Goal: Use Delta’s “database-like” features.

Tasks:

Time travel:

Perform updates/deletes on your Delta table, then query older versions using VERSION AS OF or TIMESTAMP AS OF.

Schema evolution:

Add a new column via mergeSchema or ALTER TABLE, then write new data.

KPIs:

KPI-11: Show at least 2 different versions of the same table with different content.

KPI-12: Successfully evolve schema without breaking downstream reads.

Level 3 – Optimization, Delta Live Tables, Unity Catalog
Module 3.1 – Delta Live Tables (DLT) basics
Goal: Build a managed pipeline with DLT.

Tasks:

Create a DLT pipeline:

Define Bronze/Silver/Gold as DLT tables/views using Python or SQL.

Configure pipeline settings (trigger, target, storage location).

Monitoring:

Use the DLT UI to inspect lineage, expectations, and run history.

KPIs:

KPI-13: One DLT pipeline that runs successfully end-to-end.

KPI-14: At least one data quality expectation (e.g., non-null, range check) enforced in DLT.

Module 3.2 – Delta optimization: Z-ORDER, OPTIMIZE, VACUUM
Goal: Reduce cost and improve query performance.

Tasks:

Z-ORDER:

Identify a high-selectivity column (e.g., customer_id, device_id, date) and apply OPTIMIZE ... ZORDER BY (col).

OPTIMIZE & VACUUM:

Run OPTIMIZE on large tables; run VACUUM with safe retention and understand what files are removed.

KPIs:

KPI-15: Before/after query timing on a filtered query to show Z-ORDER impact (even if small).

KPI-16: Demonstrate safe VACUUM and confirm old files are no longer accessible via time travel beyond retention.

Module 3.3 – Structured Streaming + Delta + DLT
Goal: Combine streaming with Delta and/or DLT.

Tasks:

Streaming ingest:

Build a simple Spark Structured Streaming job writing to a Delta table (e.g., from a file source or autoloader).

DLT + streaming:

Configure a DLT pipeline that uses streaming tables or views.

KPIs:

KPI-17: One streaming query writing to Delta that runs for at least 10–15 minutes.

KPI-18: DLT pipeline that consumes streaming input and maintains an up-to-date Gold table.

Module 3.4 – Unity Catalog and multi-technology access
Goal: Central governance and cross-engine access.

Tasks:

Unity Catalog setup:

Create a catalog, schema, and register Delta tables under UC.

External systems:

Explore reading/writing via UC to non-Delta (e.g., Postgres, Iceberg) if available in your environment.

KPIs:

KPI-19: All core Delta tables (Bronze/Silver/Gold) registered in Unity Catalog with clear naming.

KPI-20: At least one non-Delta asset (e.g., Postgres table or Iceberg table) visible/usable via UC.

Level 4 – Performance, cost, governance, multi-cloud thinking
Module 4.1 – Spark performance tuning under pressure
Goal: Understand how Spark behaves at scale and under skew.

Tasks:

Job profiling:

Use Spark UI to inspect stages, tasks, shuffle, and skew.

Skew handling:

Create or identify a skewed dataset and apply techniques like salting, repartitioning, or skewHint.

KPIs:

KPI-21: Before/after comparison of a skewed job with and without mitigation.

KPI-22: Ability to explain key Spark UI metrics (tasks, shuffle read/write, spill, etc.).

Module 4.2 – Memory, throughput, and Photon
Goal: Tune cluster and execution characteristics.

Tasks:

Memory & partitions:

Experiment with repartition, coalesce, and spark.sql.shuffle.partitions.

Photon evaluation:

Run the same workload on a Photon-enabled cluster vs non-Photon and compare cost/performance.

KPIs:

KPI-23: Show at least one job where tuning partitions reduces runtime or shuffle size.

KPI-24: Simple cost/performance comparison table: Photon vs non-Photon for the same workload.

Module 4.3 – Governance and PII protection
Goal: Apply real governance patterns, not just tech toys.

Tasks:

Access control:

Use Unity Catalog permissions to restrict access to PII tables/columns.

Masking/anonymization:

Implement column masking, tokenization, or hashing for PII fields (e.g., email, phone).

KPIs:

KPI-25: A table with PII where non-privileged users see masked data or no access.

KPI-26: Documented pattern for how PII flows from raw → masked → analytics.

Module 4.4 – Cost optimization and multi-cloud considerations
Goal: Think like an architect: cost, portability, governance.

Tasks:

Cost levers:

Document how cluster size, autoscaling, spot instances, Photon, OPTIMIZE/VACUUM, and storage format affect cost.

Multi-cloud posture:

Compare how Databricks behaves on at least two clouds conceptually (e.g., storage layer differences, networking, governance).

KPIs:

KPI-27: One-page cost playbook: “If cost is high, pull these levers in this order.”

KPI-28: Short architecture note on how you’d design a portable Delta/UC-based platform across clouds.

Execution pattern
Approach:

Phase 1: Levels 1–2 → functional competence (you can build and automate pipelines).

Phase 2: Level 3 → optimization, DLT, UC (you can run a governed lakehouse).

Phase 3: Level 4 → performance, cost, governance, multi-cloud (you think like a platform architect).

Cadence suggestion:

Per module: 1–2 focused sessions where you:

Build the artifact.

Capture screenshots/notes.

Log KPIs as “passed/failed”.
