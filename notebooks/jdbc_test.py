# Run this Python script locally to test external connection to Databricks SQL

jdbc_url = "jdbc:databricks://<server-host>:443/default;transportMode=http;ssl=1;httpPath=sql/protocolv1/o/<workspace-id>/<endpoint-id>"
table_name = "<schema>.<delta_table>"
properties = {
    "user": "<token>",
    "password": "<personal-access-token>",
    "driver": "com.databricks.client.jdbc.Driver"
}

df = spark.read.jdbc(url=jdbc_url, table=table_name, properties=properties)
display(df)