"""
Simple salary calculation module.
"""

def calculate_salary(hours, rate):
    """
    Calculate employee salary.
    """
    return hours * rate


if __name__ == "__main__":
    SALARY = calculate_salary(8, 500)
    print(f"Daily Salary: {SALARY}")