# Global variables (shared by all requisitions)
requisition_counter = 0
all_requisitions = []


class Requisition:
    def __init__(self, date, staff_id, staff_name):
        global requisition_counter
        requisition_counter = requisition_counter + 1

        self.date = date
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.requisition_id = 10000 + requisition_counter
        self.total = 0
        self.status = "Pending"
        self.approval_reference = "Not available"

        all_requisitions.append(self)

    def add_requisition(self, items):
        # items is a list of (item name, cost), for example [("Pens", 200), ("Paper", 250)]
        total = 0
        for item in items:
            total = total + item[1]
        self.total = total
        self.approve_requisition()
        return self.total

    def approve_requisition(self):
        # Under $500 is approved automatically, otherwise it stays pending
        if self.total < 500:
            self.status = "Approved"
            self.make_reference()
        else:
            self.status = "Pending"
            self.approval_reference = "Not available"

    def make_reference(self):
        # Staff ID + last 3 digits of the requisition ID, for example FN19001
        last_three = str(self.requisition_id)[-3:]
        self.approval_reference = self.staff_id + last_three

    def respond_to_requisition(self, decision):
        # A manager can only respond to a pending requisition
        if self.status == "Pending":
            if decision == "Approved":
                self.status = "Approved"
                self.make_reference()
            elif decision == "Not approved":
                self.status = "Not approved"
                self.approval_reference = "Not available"
            else:
                print("Invalid decision. Use Approved or Not approved.")
        else:
            print("Requisition", self.requisition_id, "is not pending.")

    def display_requisitions(self):
        # Prints every requisition that has been created
        for r in all_requisitions:
            print("Date:", r.date)
            print("Requisition ID:", r.requisition_id)
            print("Staff ID:", r.staff_id)
            print("Staff Name:", r.staff_name)
            print("Total: $" + str(r.total))
            print("Status:", r.status)
            print("Approval Reference Number:", r.approval_reference)
            print()

    def requisition_statistics(self):
        total = 0
        approved = 0
        pending = 0
        not_approved = 0

        for r in all_requisitions:
            total = total + 1
            if r.status == "Approved":
                approved = approved + 1
            elif r.status == "Pending":
                pending = pending + 1
            elif r.status == "Not approved":
                not_approved = not_approved + 1

        print("Statistics:")
        print("Displaying the Requisition Statistics")
        print()
        print("The total number of requisitions submitted:", total)
        print()
        print("The total number of approved requisitions:", approved)
        print()
        print("The total number of pending requisitions:", pending)
        print()
        print("The total number of not approved requisitions:", not_approved)