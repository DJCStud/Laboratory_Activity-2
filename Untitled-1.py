class StudentEnrollment:
    def __init__(self, cash):
        self.cash = cash
        self.downpayment_paid = False
        self.units = 0
        self.cost_per_unit = 1200
        self.downpayment_amount = 1000

    def enroll(self):
        try:
            if not self.downpayment_paid:
                print("\nYou must pay the downpayment first.")
                choice = input("Pay downpayment? (Y/N): ").upper()

                if choice == "Y":
                    if self.cash >= self.downpayment_amount:
                        self.cash -= self.downpayment_amount
                        self.downpayment_paid = True
                        print("Downpayment successful!")
                        print("Remaining cash:", self.cash)
                    else:
                        print("Insufficient cash for downpayment.")
                else:
                    print("Enrollment cancelled.")
                return

            units = int(input("Enter number of units (max 25): "))

            if units < 1 or units > 25:
                raise ValueError("Invalid unit amount.")

            total_cost = units * self.cost_per_unit

            if total_cost > self.cash:
                print("Not enough cash to enroll.")
                return

            self.units = units
            self.cash -= total_cost
            print(f"Successfully enrolled in {units} units.")
            print("Remaining cash:", self.cash)

        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def view_tuition(self):
        tuition = self.units * self.cost_per_unit
        print("\n--- Tuition Summary ---")
        print("Units:", self.units)
        print("Total Tuition:", tuition)

    def deposit(self):
        try:
            amount = int(input("Enter deposit amount: "))
            if amount <= 0:
                raise ValueError

            self.cash += amount
            print("Deposit successful.")
            print("New balance:", self.cash)

        except ValueError:
            print("Invalid deposit amount.")

    def show_balance(self):
        print("\nCurrent cash balance:", self.cash)


def main():
    try:
        starting_cash = int(input("Enter starting cash: "))
        system = StudentEnrollment(starting_cash)

        while True:
            print("\n--- Student Enrollment System ---")
            print("1. Enroll")
            print("2. View Tuition")
            print("3. Deposit Cash")
            print("4. Show Balance")
            print("5. Exit")

            choice = int(input("Choose option (1-5): "))

            if choice == 1:
                system.enroll()
            elif choice == 2:
                system.view_tuition()
            elif choice == 3:
                system.deposit()
            elif choice == 4:
                system.show_balance()
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                print("Invalid menu choice.")

    except ValueError:
        print("Invalid starting cash input.")


if __name__ == "__main__":
    main()
