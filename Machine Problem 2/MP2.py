from Employees import employee_list

class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def setKey(self, key):
        self.key = key

    def getKey(self):
        return self.key

    def setValue(self, value):
        self.value = value

    def getValue(self):
        return self.value

class Array:
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.contents = [None] * capacity
        self.size = 0

    def getSize(self):
        return self.size

    def getCapacity(self):
        return self.capacity

    def isEmpty(self):
        return self.size == 0

class ArrayDictionary(Array):
    def insert(self, key, value):
        entry = Entry(key, value)

        # If the array is full, double its capacity
        if self.size >= self.capacity:
            self.capacity *= 2
            new_contents = [None] * self.capacity

            # Copy existing entries to the new array
            for i in range(self.size):
                new_contents[i] = self.contents[i]

            self.contents = new_contents

        # Initialize 'i' before the while loop
        i = self.size - 1
        # Find the correct position to insert the new entry
        while i >= 0 and self.contents[i].getKey() > key:
            self.contents[i + 1] = self.contents[i]
            i -= 1

        # Insert the new entry at the correct position
        self.contents[i + 1] = entry
        self.size += 1
        return None



class EmployeeFileHandler:
    def __init__(self, max_capacity):
        self.max_capacity = max_capacity
        self.employees = ArrayDictionary(max_capacity)                  # initialize an ArrayDictionary to store employee data

    # method to search for employees by name
    def search_by_name(self, name_to_search):
        results = []
        for employee in self.employees.contents:
            if employee is not None and name_to_search.lower() in employee.getValue()['name'].lower():
                results.append(employee.getValue())
        return results

    # method to seatch for employees by years active
    def search_by_years_active(self, years_active):
        results = []
        for employee in self.employees.contents:
            if employee is not None and employee.getValue()['years_active'] == years_active:
                results.append(employee.getValue())
        return results

    # method to search for employees by job
    def search_by_job(self, jobs):
        result = []
        for employee in self.employees.contents:
            if employee is not None and jobs.lower() in employee.getValue()['jobs'].lower():
                result.append(employee.getValue())
        return result

def main():
    employee_handler = EmployeeFileHandler(max_capacity=30)                                           # create an instance of EmployeeFileHandler with maximum capacity of 30 employees
    # iterate through employee_list and insert employee data into the employee_handler
    for employee_data in employee_list:
        key = employee_data.getFullName()
        value = {
            'name': employee_data.getFullName(),
            'address': employee_data.getAddress(),
            'years_active': int(employee_data.getYears()),
            'description': employee_data.getDesc(),
            'jobs': employee_data.getJobs(),
            'joblist': employee_data.joblist
        }
        employee_handler.employees.insert(key, value)

    # main user interface
    while True:
        print("\nMain Menu:")
        print("1. Search by Name")
        print("2. Search by Years Active")
        print("3. Search by Job")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        # process user input
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 4:
                if choice == 1:
                    name_to_search = input("Enter the name to search: ")
                    result = employee_handler.search_by_name(name_to_search)
                    print_results(result)
                elif choice == 2:
                    years_to_search = int(input("Enter the years active to search: "))
                    result = employee_handler.search_by_years_active(years_to_search)
                    print_results(result)
                elif choice == 3:
                    job_to_search = input("Enter the job to search: ")
                    result = employee_handler.search_by_job(job_to_search)
                    print_results(result)
                elif choice == 4:
                    print("Exiting program.\n")
                    break
            else:
                print("Invalid choice. Please enter a valid option.")
        else:
            print("Invalid choice. Please enter a valid option.")


def print_results(results):

    # functionto print search results
    if not results:             
        print("No matching records found.")
    else:
        # Sort results alphabetically by name
        results.sort(key=lambda x: x['name'].lower())   

        result_size = 30
        current_page = 0

        count = 0
        while current_page * result_size < len(results):
            print("\nMatching Records:")

            start = current_page * result_size
            end = (current_page + 1) * result_size

            for i in range(start, end):
                if i < len(results):
                    employee = results[i]   
                    print("\n===========| Employee Information |===========")
                    print("Name:", employee['name'])
                    print("Address:", employee['address'])
                    print("Years In Industry:", employee['years_active'])
                    print("Description:", employee['description'])
                    print("Jobs:", ", ".join(employee['joblist']))
                    print("===============================================")
                    count += 1
            
            print("\n[Result: " + str(count) + " of " + str(len(results)) + "]")
            print("- - - - - - - - - - - - - - - - - - - - - - - - \n")
            current_page += 1            
           
            if current_page * result_size < len(results):
                next_page = input("Press Enter to continue searching or 'q' to quit: ")
                if next_page.lower() == 'q':
                    break        

main()