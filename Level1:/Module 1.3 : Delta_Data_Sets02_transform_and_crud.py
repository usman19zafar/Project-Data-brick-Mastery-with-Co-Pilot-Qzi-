# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit
from delta.tables import DeltaTable

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

# 1. Define Delta path (same as Notebook 1)
delta_path = "/mnt/delta/usman_dataset_level1_module13"

# COMMAND ----------

# 2. Load Delta table
df = spark.read.format("delta").load(delta_path)
df.show(5)

# COMMAND ----------

# 3. Convert to DeltaTable object for CRUD
delta_tbl = DeltaTable.forPath(spark, delta_path)

# COMMAND ----------

# 4. UPDATE operation
# Increase value by 10 where category = 'A'
delta_tbl.update(
    condition="category = 'A'",
    set={"value": col("value") + 10}
)

# COMMAND ----------

# 5. DELETE operation
# Remove rows where value < 20
delta_tbl.delete("value < 20")

# COMMAND ----------

# 6. INSERT operation
# Insert a new synthetic row
new_data = spark.createDataFrame(
    [(9999, "Z", 123.45)],
    ["id", "category", "value"]
)

delta_tbl.alias("t").merge(
    new_data.alias("s"),
    "t.id = s.id"
).whenNotMatchedInsertAll().execute()

# COMMAND ----------

# 7. READ AFTER CRUD (validation)
df_after = spark.read.format("delta").load(delta_path)
df_after.show(10)

# COMMAND ----------

# 8. TIME TRAVEL — list versions
history = delta_tbl.history()
history.show(truncate=False)

# COMMAND ----------

# 9. TIME TRAVEL — read previous version
# Read version 0 (initial write)
df_v0 = spark.read.format("delta").option("versionAsOf", 0).load(delta_path)
df_v0.show(5)

# COMMAND ----------

# 10. TIME TRAVEL — read latest version
latest_version = history.select("version").orderBy(col("version").desc()).first()[0]
df_latest = spark.read.format("delta").option("versionAsOf", latest_version).load(delta_path)
df_latest.show(5)
