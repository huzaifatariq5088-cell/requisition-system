from requisition import Requisition

# Under $500 (auto approved)
r1 = Requisition("03/04/2024", "FN19", "John Paul")
r1.add_requisition([("Pens", 200), ("Paper", 250)])        # 450

r2 = Requisition("03/05/2024", "FN02", "Catlin White")
r2.add_requisition([("Markers", 190), ("Folders", 300)])   # 490

# $500 or more (pending)
r3 = Requisition("05/04/2024", "FN20", "Tracy Brown")
r3.add_requisition([("Printer", 700), ("Ink", 300)])       # 1000

r4 = Requisition("07/05/2024", "FN15", "Emma Wellington")
r4.add_requisition([("Laptop", 3500)])                     # 3500

r5 = Requisition("10/05/2024", "FN08", "Sam Lee")
r5.add_requisition([("Monitor", 600)])                     # 600

print("=== BEFORE MANAGER RESPONSE ===\n")
Requisition.display_requisitions()
Requisition.requisition_statistics()

# Manager responses
r3.respond_to_requisition("Approved")
r4.respond_to_requisition("Not approved")
# r5 stays pending

print("\n\n=== AFTER MANAGER RESPONSE ===\n")
Requisition.display_requisitions()
Requisition.requisition_statistics()