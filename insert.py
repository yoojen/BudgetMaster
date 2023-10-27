from models.user import User
from models.location import Location
from models.expenses import Expense
from models.category import Category
from models.incomes import Income


# Insert location

data = [
    {"Uganda": "Kampala"},
    {"Burundi": "Ngozi"},
    {"Kenya": "Mombasa"},
    {"DRC": "Goma"}
]

[Location(k, v).save() for i in range(len(data)) for k, v in data[i].items()]

#Inser User
usr_collection = [
    ["yoojen", "google@com", "Eugene", "Mutuyimana", "123", 1],
    ["reb12", "google@com", "Rebecca", "Isingizwe", "123", 2],
    ["joe32", "google@com", "Joe", "Dier", "123", 1],
]

[User(usr[0], usr[1], usr[2], usr[3], usr[4], usr[5]).save() for usr in usr_collection]
# Insert expense

exp_collection = [
    ["Rent", 1000, 1, 6],
    ["Electricy", 4500, 1, 4],
    ["Water Payment", 400, 1, 3],
    ["Internet Bill", 1200, 1, 2],
    ["Cost Overhead", 300, 1, 1]
]

[Expense(exp[0], exp[1], exp[2], exp[3]).save() for exp in exp_collection]


# Create Category

ct_collection = [
    "Daily Expense", "Weekly Expense", 
    "Monthly Expense", "Yearly Expense", 
    "Quarterly Expense", "Working Expense"
]

[Category(value).save() for value in ct_collection]


# Insert Incomes
inc_collection = [
    ["Sales", "Cash", 10000, 3, 7],
    ["Discount received","unrecognized", 4500, 3, 7],
]

[Income(inc[0], inc[1], inc[2], inc[3], inc[4]).save() for inc in inc_collection]
