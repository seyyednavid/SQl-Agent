#  SQL AI Agent  

🔗 Project Links
- **Live Demo:**  https://sql-agent-production-4f10.up.railway.app/
- More Description : https://seyyednavid.github.io/2025/11/19/gen-ai-sql-agent-bot.html


<img width="918" height="426" alt="SQL-AGENT" src="https://github.com/user-attachments/assets/59506390-c936-4e24-ac27-a98e20c63104" />

An AI-powered SQL assistant that converts natural language questions into accurate PostgreSQL SELECT queries.

This project allows users to ask questions about customer demographics and purchase behavior.  
The system automatically generates SQL queries and returns clear summaries using OpenAI + LangChain.

---

##  Features
- Natural language → PostgreSQL SELECT queries  
- Strict read-only queries (no INSERT/UPDATE/DELETE)  
- Supports joins, aggregations, grouping, and date filtering  
- Smart handling of ambiguous questions  
- Flask web interface  
- Hosted on Render  
- Uses LangChain SQL toolkit + GPT-4.1 reasoning

---

##  Database Schema

### **1. grocery_db.customer_details tabel – one row per customer*

| Column              | Type           
|--------------------|---------------|
| customer_id        | INT           | 
| distance_from_store| NUMERIC(10,2) | 
| gender             | VARCHAR(2)    |
| credit_score       | NUMERIC(3,2)  | 

---

### **2. grocery_db.transactions tabel – one row per combination of customer, transaction, and product area**

| Column            | Type            | 
|------------------|------------------|
| customer_id      | INT              |
| transaction_id   | INT              |
| transaction_date | DATE             |
| product_area_id  | INT (1–5)        |
| num_items        | INT              |
| sales_cost       | NUMERIC(10,2)    |

---

###  Join Relationship
customer_details.customer_id = transactions.customer_id

---

 ## Example Question

User:

"Which gender lives furthest from the store on average?"

AI Response:

“Female customers live the furthest on average.”
