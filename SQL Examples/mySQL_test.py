import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    host="localhost",
    user="username",
    password="password",
    database="database_name"
)

# Create a cursor
cursor = cnx.cursor()

# Get the user input
user_input = input("Enter your username: ")

# Sanitize the user input
sanitized_input = mysql.connector.escape_string(user_input)

# Construct a SQL query using the sanitized input
query = f"SELECT * FROM users WHERE username = '{sanitized_input}'"

# Execute the query
cursor.execute(query)

# Fetch the results
results = cursor.fetchall()

# Iterate over the results
for result in results:
    print(result)

# Close the cursor and connection
cursor.close()
cnx.close()
