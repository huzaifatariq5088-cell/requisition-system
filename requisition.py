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

    def _generate_reference(self):
        self.approval_ref = f"{self.staff_id}{str(self.requisition_id)[-3:]}"