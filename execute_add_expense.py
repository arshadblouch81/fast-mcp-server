import sqlite3

DB_PATH = r"D:\LangGraph-workspace\mcp-server\expenses.db"

with sqlite3.connect(DB_PATH) as conn:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO expenses(date, amount, category, subcategory, note) VALUES (?,?,?,?,?)",
        ("2025-09-26", 500.0, "food", "dining_out", "")
    )
    conn.commit()
    expense_id = cursor.lastrowid
    
print("✓ Expense added successfully!")
print(f"  ID: {expense_id}")
print(f"  Date: 2025-09-26 (Last Friday)")
print(f"  Amount: Rs 500")
print(f"  Category: food")
print(f"  Subcategory: dining_out")
