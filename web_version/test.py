from prettytable import PrettyTable

table = PrettyTable()
table.field_names = ["Name"]
table.add_row(["Alice", 30])
table.add_row(["Bob", 25])

print(table)#B60000
