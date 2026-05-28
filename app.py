def calculate_salary(hours, rate):
    return hours * rate

if __name__ == "__main__":
    salary = calculate_salary(8, 500)
    print(f"Daily Salary: {salary}")