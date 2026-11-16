from requisition import Requisition

r = Requisition("03/04/2024", "FN19", "John Paul")
print(r.add_requisition([("Pens", 200), ("Paper", 250)]))
print(r.status, r.approval_ref)