from app import *

from flask import jsonify
# categories = [
#     {"name": "Daily"},
#     {"name": "Weekly"},
#     {"name": "Yearly"}
# ]

# for cat in categories:
#     new_cat = Category(
#         name=cat['name']
#     )
#     session.add(new_cat)
#     session.commit()

category = session.query(Category).filter(Category.id == 1).first()
# expenses = [
#     {"name": "Rent"},
#     {"name": "Electricity"},
#     {"name": "Water"}
# ]


# for exp in expenses:
#     new_exp = Expense(
#         name=exp["name"],
#         category_id=category.id
#     )
#     session.add(new_exp)
#     session.commit()


print("printing test\n__________________\n")
category_dict = category.__dict__
expense_list = category.expense
all_exp = []
for i in expense_list:
    del i.__dict__['_sa_instance_state']
    all_exp.append(i.__dict__)
    so = i.__dict__


test = [
    {"category_name": category.__dict__.get('name'), "expense": all_exp}
]

print((test))
