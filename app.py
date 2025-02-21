from dotenv import load_dotenv
load_dotenv()  # Load all the environment variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai

# Configure API key
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

# Function to generate a response
def get_gemini_response(question, prompt):
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content([prompt[0], question])
    
    # Extract only the SQL query from the response
    sql_query = response.text.strip()
    
    # Remove unwanted prefixes like "SQL Query:" or Markdown formatting
    sql_query = sql_query.replace("SQL Query:", "").replace("```sql", "").replace("```", "").strip()

    return sql_query

# Function to query the database
def read_sql_query(sql, db):
    conn = sqlite3.connect(db)
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    conn.close()
    return rows

# Define the prompt
prompt = [
    """
    You are an expert in converting English questions to SQL queries!
    The SQL database has the name STUDENTS and has the following columns - NAME, CLASS,
    SECTION and MARKS. For example:
    
    Example 1: How many entries of records are present?
    SQL Query: SELECT COUNT(*) FROM STUDENTS;
    
    Example 2: Provide the average marks of all students.
    SQL Query: SELECT AVG(MARKS) FROM STUDENTS;
    """
]

# Streamlit App
st.set_page_config(page_title="Gemini SQL Query Generator", page_icon="🔍", layout="wide")
st.header("Gemini App to Retrieve SQL Data")

# User input
question = st.text_input("Enter your question in plain English:")

# Button to generate SQL query
if st.button("Ask the Question"):
    try:
        # Generate SQL query
        sql_query = get_gemini_response(question, prompt)
        st.subheader("Generated SQL Query:")
        st.code(sql_query)

        # Fetch data
        results = read_sql_query(sql_query, 'students.db')

        # Extract and display only the number
        if results and isinstance(results[0], tuple):  # Ensures valid data exists
            st.subheader("Result:")
            st.write(results[0][0])  # Displays only the numeric value
        else:
            st.warning("No valid data returned.")
    except Exception as e:
        st.error(f"Error: {e}")
