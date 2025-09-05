from pyflink.table import EnvironmentSettings, TableEnvironment
from pyflink.table import DataTypes

# 1. Create a TableEnvironment
env_settings = EnvironmentSettings.in_batch_mode()  # Or in_streaming_mode() for streaming
table_env = TableEnvironment.create(env_settings)

# 2. Define a source table from in-memory data
# You can also define source tables from external systems like Kafka, files, etc.
data = [("Jack", 100), ("Rose", 300), ("Jack", 200), ("Jack", 200), ("Rose", 300)]
source_table = table_env.from_elements(
    data,
    DataTypes.ROW([
        DataTypes.FIELD("name", DataTypes.STRING()),
        DataTypes.FIELD("revenue", DataTypes.INT())
    ])
)

# 3. Register the source table as a temporary view
table_env.create_temporary_view("orders", source_table)

# 4. Execute a SQL query or use Table API operations
# This example uses SQL to group by name and sum revenue
result_table = table_env.sql_query("SELECT name, SUM(revenue) AS total_revenue FROM orders GROUP BY name")

# 5. Print the results to the console
# For production scenarios, you would typically write to a sink (e.g., Kafka, database, file)
result_table.execute().print()