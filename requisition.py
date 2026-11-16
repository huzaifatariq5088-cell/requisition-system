class Requisition:
    next_id = 10001
    all_requisitions = []

    def __init__(self, date, staff_id, staff_name):
        self.date = date
        self.requisition_id = Requisition.next_id
        Requisition.next_id += 1
        self.staff_id = staff_id
        self.staff_name = staff_name
        self.items = []
        self.total = 0
        self.status = "Pending"
        self.approval_ref = "Not available"
        Requisition.all_requisitions.append(self)

    def add_requisition(self, items):
        """items = list of (item_name, cost). Returns the total."""
        self.items = items
        self.total = sum(cost for _, cost in items)
        self.approve_requisition()
        return self.total

    def approve_requisition(self):
        """Under $500 = auto approved, otherwise stays pending."""
        if self.total < 500:
            self.status = "Approved"
            self._generate_reference()
        else:
            self.status = "Pending"
            self.approval_ref = "Not available"

    def respond_to_requisition(self, decision):
        """Manager marks a pending requisition Approved or Not approved."""
        if self.status != "Pending":
            print(f"Requisition {self.requisition_id} is not pending.")
            return
        if decision == "Approved":
            self.status = "Approved"
            self._generate_reference()
        elif decision == "Not approved":
            self.status = "Not approved"
            self.approval_ref = "Not available"
        else:
            print("Invalid decision. Use 'Approved' or 'Not approved'.")

    def _generate_reference(self):
        self.approval_ref = f"{self.staff_id}{str(self.requisition_id)[-3:]}"

    @classmethod
    def display_requisitions(cls):
        for r in cls.all_requisitions:
            print(f"Date: {r.date}")
            print(f"Requisition ID: {r.requisition_id}")
            print(f"Staff ID: {r.staff_id}")
            print(f"Staff Name: {r.staff_name}")
            print(f"Total: ${r.total:g}")
            print(f"Status: {r.status}")
            print(f"Approval Reference Number: {r.approval_ref}\n")

    @classmethod
    def requisition_statistics(cls):
        reqs = cls.all_requisitions
        stats = {
            "total": len(reqs),
            "approved": sum(r.status == "Approved" for r in reqs),
            "pending": sum(r.status == "Pending" for r in reqs),
            "not_approved": sum(r.status == "Not approved" for r in reqs),
        }
        print("Statistics:")
        print("Displaying the Requisition Statistics\n")
        print(f"The total number of requisitions submitted: {stats['total']}\n")
        print(f"The total number of approved requisitions: {stats['approved']}\n")
        print(f"The total number of pending requisitions: {stats['pending']}\n")
        print(f"The total number of not approved requisitions: {stats['not_approved']}")
        return stats