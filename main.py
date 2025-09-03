import gspread
from google.oauth2.service_account import Credentials

scopes = [
    "https://www.googleapis.com/auth/spreadsheets",
]
Credentials = Credentials.from_service_account_file("Credentials.json", scopes=scopes)
client = gspread.Client(auth=Credentials)
sheet_id = "1PqrXAdkuprzTd8HgKSbOfclIaIEMAb8fEh3i-GDkk4I"
workbook = client.open_by_key(sheet_id)


sheet = workbook.worksheet("Ark1")
# Example 1: Find a cell and insert a value nearby
cell = sheet.find("Alias")  # Find the cell containing "Alias"
print(f"Found 'Alias' at row {cell.row}, column {cell.col}")

# Insert a value in the cell to the right of "Alias"
sheet.update_cell(cell.row, cell.col + 1, "New Value")

# Example 2: Append a new row to the sheet
new_row = ["John Doe", "john@example.com", 25]  # Example data
sheet.append_row(new_row, value_input_option="USER_ENTERED")

# Example 3: Update a range of cells (e.g., A2:C2)
range_to_update = "A2:C2"
values = [["Alice", "alice@example.com", 30]]  # 2D list for a range
sheet.update(range_to_update, values, value_input_option="USER_ENTERED")

print("Values inserted successfully!")