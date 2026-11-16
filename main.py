from requisition import Requisition

r = Requisition("03/04/2024", "FN19", "John Paul")
r.add_requisition([("Pens", 200), ("Paper", 250)])
Requisition.display_requisitions()
Requisition.requisition_statistics()