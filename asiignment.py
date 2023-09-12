class FlightTable:
    def __init__(self):
        self.data = []

    def add_flight(self, p_id, process, start_time_ms, priority):
        self.data.append((p_id, process, start_time_ms, priority))

    def sort_by_p_id(self):
        self.data.sort(key=lambda x: x[0])

    def sort_by_start_time(self):
        self.data.sort(key=lambda x: x[2])

    def sort_by_priority(self):
        priority_map = {"Low": 0, "MID": 1, "High": 2}
        self.data.sort(key=lambda x: priority_map[x[3]])

    def display(self):
        print("P_ID\tProcess\tStart Time (ms)\tPriority")
        for item in self.data:
            print(f"{item[0]}\t{item[1]}\t{item[2]}\t\t{item[3]}")


def main():
    flight_table = FlightTable()

    flight_table.add_flight("P1", "VSCode", 100, "MID")
    flight_table.add_flight("P23", "Eclipse", 234, "MID")
    flight_table.add_flight("P93", "Chrome", 189, "High")
    flight_table.add_flight("P42", "JDK 9", 9, "High")
    flight_table.add_flight("P9", "CMD", 7, "High")
    flight_table.add_flight("P87", "NotePad", 23, "Low")

    while True:
        print("\nSelect sorting parameter:")
        print("1. Sort by P_ID")
        print("2. Sort by Start Time")
        print("3. Sort by Priority")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            flight_table.sort_by_p_id()
        elif choice == "2":
            flight_table.sort_by_start_time()
        elif choice == "3":
            flight_table.sort_by_priority()
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
            continue

        flight_table.display()


if __name__ == "__main__":
    main()
