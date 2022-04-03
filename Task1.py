# TASK 1
# One of our products is in charge of downloading and ingesting millions of records from our clients.
# Recently during ingesting a large dataset we had our entire DB(postgres) go down and the entire ingestion process from a
# pandas dataframe to sql took around 2-3 hours because of the RAM unavailability. Now this has two simple fixes
#
# - Increase ram/ scale the db on demand
# - change our code to accommodate these restrictions and make the entire ingestion process much faster on the way.
#
# How would you approach this? We are not looking for a full blown ingestion logic. Just a small script to take a given csv file and
# upload it to DB in an efficient manner.
# Write code to take a large csv file( > 1GB ) and ingest it to table - public.test_od

import pandas as pd
from pyspark.sql.functions import *
from pyspark.sql.session import SparkSession

df = pd.read_csv("csv_location.csv")

# There can be many solutions to solve the memory issues either scaling vertically or horizantally.

# Vertical scaling requires adding more RAM to the system however because of size of the data is huge i would recommand to use spark
# instead of pandas dataframe.



spark = SparkSession.builder \
    .master("local") \
    .appName("Task1") \
    .getOrCreate()

spark_df = spark.read.csv("csv_location.csv", header=True, sep=",")

# Clean up / Prodess some data

#  Show stats

spark_df.count()
spark_df.printSchema()
spark_df.show(20, False)

# load the data

spark_df.write.format("jdbc")\
    .option("url", "jdbc:postgresql://localhost:5432/public") \
    .option("driver", "org.postgresql.Driver").option("dbtable", "test_od") \
    .option("user", "user").option("password", "password").save()

# ============================================================================









