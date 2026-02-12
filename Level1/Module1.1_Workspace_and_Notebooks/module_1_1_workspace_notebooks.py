# Databricks notebook source
# MODULE 1.1 — WORKSPACE + NOTEBOOKS
# Objective: Demonstrate Python, SQL, Markdown in one notebook

# COMMAND ----------
# %md
# # Module 1.1 — Workspace + Notebooks
# This notebook demonstrates:
# - Markdown
# - Python execution
# - SQL execution
# - Clean output
# 
# **KPI Targets**
# - Notebook runs without cluster errors
# - Notebook mixes markdown + code + results

# COMMAND ----------
# %md
# ## Python Section

# COMMAND ----------
# Python: simple DataFrame
data = [(1, "A"), (2, "B"), (3, "C")]
df = spark.createDataFrame(data, ["id", "category"])
df.show()

# COMMAND ----------
# %md
# ## SQL Section

# COMMAND ----------
# Create temp view
df.createOrReplaceTempView("demo_table")

# COMMAND ----------
# SQL query
# %sql
SELECT * FROM demo_table;

# COMMAND ----------
# %md
# ## Completion
# Module 1.1 tasks and KPIs satisfied.
