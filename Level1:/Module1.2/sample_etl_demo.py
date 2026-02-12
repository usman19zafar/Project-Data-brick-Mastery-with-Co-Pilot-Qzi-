# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, count, avg

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------
# 1. Read raw dataset (Parquet example)
raw_path = "/databricks-datasets/learning-spark-v2/people/people-10m.delta"
df_raw = spark.read.format("delta").load(raw_path)

# Preview
df_raw.show(5)

# COMMAND ----------
# 2. Transformations
df_clean = (
    df_raw
    .select("id", "gender", "salary")
    .filter(col("salary").isNotNull())
    .withColumn("salary_k", col("salary") / 1000)
)

df_clean.show(5)

# COMMAND ----------
# 3. Aggregation
df_agg = (
    df_clean
    .groupBy("gender")
    .agg(
        count("*").alias("count"),
        avg("salary").alias("avg_salary")
    )
)

df_agg.show()

# COMMAND ----------
# 4. Explain plan (KPI-4)
df_agg.explain()

# COMMAND ----------
# 5. Write outputs
parquet_path = "/mnt/etl_output/people_clean_parquet"
delta_path = "/mnt/etl_output/people_clean_delta"

df_clean.write.mode("overwrite").parquet(parquet_path)
df_clean.write.format("delta").mode("overwrite").save(delta_path)

# COMMAND ----------
# 6. Read back Delta for validation
df_check = spark.read.format("delta").load(delta_path)
df_check.show(5)

