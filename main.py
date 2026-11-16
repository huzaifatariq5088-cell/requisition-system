from requisition import Requisition

# Requisitions under $500 (approved automatically)
r1 = Requisition("03/04/2024", "FN19", "John Paul")
r1.add_requisition([("Pens", 200), ("Paper", 250)])

r2 = Requisition("03/05/2024", "FN02", "Catlin White")
r2.add_requisition([("Markers", 190), ("Folders", 300)])

# Requisitions of $500 or more (pending)
r3 = Requisition("05/04/2024", "FN20", "Tracy Brown")
r3.add_requisition([("Printer", 700), ("Ink", 300)])

r4 = Requisition("07/05/2024", "FN15", "Emma Wellington")
r4.add_requisition([("Laptop", 3500)])

r5 = Requisition("10/05/2024", "FN08", "Sam Lee")
r5.add_requisition([("Monitor", 600)])

print("=== BEFORE MANAGER RESPONSE ===")
print()
r1.display_requisitions()
r1.requisition_statistics()

# Manager responds to some pending requisitions
r3.respond_to_requisition("Approved")
r4.respond_to_requisition("Not approved")
# r5 stays pending

print()
print("=== AFTER MANAGER RESPONSE ===")
print()
r1.display_requisitions()
r1.requisition_statistics()