# given info about the problem
#sales= 150
average_price=2100
cogs_percentage= 0.59
sales= input("Enter teh amount of sales as numbers: ")
sales=float(sales)
# Formulas for gross revenue
annual_gross_revenue=sales*average_price
monthly_gross_revenue=annual_gross_revenue/12
quarterly_gross_revenue=annual_gross_revenue/4
#summarizes the gross revenue
print("annual gross revenue = ${:0.2f}".format(annual_gross_revenue))
print("monthly gross revenue = ${:.2f}".format(monthly_gross_revenue))
print("quarterly gross revenue = ${:.2f}".format(quarterly_gross_revenue))

# Formulas for net revenue
complement_cogs_percentage=1-cogs_percentage
annual_net_revenue=complement_cogs_percentage*annual_gross_revenue
monthly_net_revenue=annual_net_revenue/12
quarterly_net_revenue=annual_net_revenue/4
print("\nNow for the net revenues: \n")
#summarizes the net revenue
print("annual net revenue = ${:0.2f}".format(annual_net_revenue))
print("monthly net revenue = ${:.2f}".format(monthly_net_revenue))
print("quarterly net revenue = ${:.2f}".format(quarterly_net_revenue))