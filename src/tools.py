from langchain.tools import tool
from data_processor import HRDataProcessor

# Initialize the processor with your mock data
processor = HRDataProcessor("data/employee_database.csv")

@tool
def check_vacation_balance(employee_name: str) -> str:
    """Useful for when you need to check how many vacation days an employee has left."""
    record = processor.get_employee_record(employee_name)
    if record:
        return f"{employee_name} has {record['vacation_days']} days remaining."
    return "Employee not found."