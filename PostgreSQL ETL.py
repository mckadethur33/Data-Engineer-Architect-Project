
"""
The following is an example my skills for Python and Pyspark to show how I would go about extracting data
from a PostgreSQL server and then proceed to transform it.
"""

import pyspark

#Create Spark session
spark = pyspark.sql.SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config('spark.driver.extraClassPath', "/Users/User/Downloads/postgresql-42.3.1.jar") \
    .getOrCreate()

#Read Payment table
payment_df = spark.read \
    .format("jdbc") \
    .option("url","jdbc:postgresql://localhost:5432/dvdrental") \
    .option("dbtable", "payment") \
    .option("user", "postgres") \
    .option("password","48#489mnb") \
    .option("driver", "org.postgresql.Driver") \
    .load()

#Read Staff table
staff_df = spark.read \
    .format("jdbc") \
    .option("url","jdbc:postgresql://localhost:5432/dvdrental") \
    .option("dbtable", "staff") \
    .option("user", "postgres") \
    .option("password","48#489mnb") \
    .option("driver", "org.postgresql.Driver") \
    .load()

#transforming tables
avg_amount = payment_df.groupBy("StaffID").mean("Amount")

#join the staff table and the avg_amount table on id
df = staff_df.join(avg_amount, staff_df.PaymentID == avg_amount.ID )

print(payment_df.show())
print(staff_df.show())
print(df.show())

