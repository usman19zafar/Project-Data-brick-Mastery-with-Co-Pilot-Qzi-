# Databricks notebook source
from pyspark.sql import SparkSession
from pyspark.sql.functions import col, rand, expr
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, DoubleType

spark = SparkSession.builder.getOrCreate()

# COMMAND ----------

# 1. Define schema
schema = StructType([
    StructField("id", IntegerType(), False),
    StructField("category", StringType(), False),
    StructField("value", DoubleType(), False)
])

# COMMAND ----------

# 2. Generate synthetic dataset
df = (
    spark.range(0, 1000)
    .withColumn("category", expr("CASE WHEN id % 3 = 0 THEN 'A' WHEN id % 3 = 1 THEN 'B' ELSE 'C' END"))
    .withColumn("value", rand() * 100)
)

# COMMAND ----------

# 3. Apply schema
df_casted = spark.createDataFrame(df.rdd, schema)

# COMMAND ----------

# 4. Define Delta path
delta_path = "/mnt/delta/usman_dataset_level1_module13"

# COMMAND ----------

# 5. Write Delta table (overwrite for reproducibility)
(
    df_casted.write
    .format("delta")
    .mode("overwrite")
    .save(delta_path)
)

# COMMAND ----------

# 6. Register table in metastore
spark.sql("""
    CREATE TABLE IF NOT EXISTS usman_level1_delta
    USING DELTA
    LOCATION '/mnt/delta/usman_dataset_level1_module13'
""")

# COMMAND ----------

# 7. Display preview
df_casted.show(10)
