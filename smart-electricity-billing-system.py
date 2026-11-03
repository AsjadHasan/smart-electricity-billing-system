
class ElectricityBill:
    """Calculate electricity bills using tiered pricing."""

    service_charge = 100

    def __init__(self, customer_name, units_consumed):
        """Initialize customer and electricity consumption."""
        self.customer_name = customer_name
        self.__units_consumed = units_consumed

    def calculate_bill(self):
        """Calculate electricity charges based on consumption."""
        units = self.__units_consumed

        if units <= 100:
            bill = units * 5

        elif units <= 200:
            bill = (100 * 5) + ((units - 100) * 7)

        else:
            bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

        return bill

    def display_bill(self):
        """Display the complete electricity bill."""
        units = self.__units_consumed

        first = min(units, 100)
        second = min(max(units - 100, 0), 100)
        third = max(units - 200, 0)

        first_charge = first * 5
        second_charge = second * 7
        third_charge = third * 10

        total = self.calculate_bill() + self.service_charge

        print("\n========== ELECTRICITY BILL ==========")
        print(f"Customer Name: {self.customer_name}")
        print(f"Units Consumed: {units}")

        print(f"\nFirst {first} Units: ¥{first_charge}")
        print(f"Next {second} Units: ¥{second_charge}")
        print(f"Remaining {third} Units: ¥{third_charge}")

        print(f"Service Charge: ¥{self.service_charge}")
        print("--------------------------------------")
        print(f"Total Electricity Bill: ¥{total}")
        print("======================================")


def main():
    """Run the electricity billing system."""
    print("Welcome to Smart Electricity Billing System!")

    name = input("Enter customer name: ").strip()

    try:
        units = int(input("Enter electricity units consumed: "))

        if not name:
            print("Customer name cannot be empty!")
        elif units < 0:
            print("Units cannot be negative!")
        else:
            customer = ElectricityBill(name, units)
            customer.display_bill()

    except ValueError:
        print("Invalid input! Please enter a valid number.")


if __name__ == "__main__":
    main()