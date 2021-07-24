# given info about the problem
#sales= 150
import numpy as np

jan_sales = [1834., 1918.,  812., 1680., 2492., 2776., 2390., 2297.]
feb_sales = [2148., 1745., 2190., 1863., 2589., 2345., 2724., 2239., 2785., 1483., 2038., 2021.]
mar_sales = [1968., 1718., 1634., 2126., 1252., 2538., 2837., 1223., 2034., 1611., 2791.]
apr_sales = [2496., 2733.,  706., 2386., 3382., 1844., 1440., 2594., 1978., 2023., 2559., 1577.]
may_sales = [2832., 1681., 1954., 1801., 2294., 1732., 1638., 1949., 2676., 2329., 2370.]
jun_sales = [2335., 2538., 2186., 2186., 2622., 2564., 1269., 3124., 1286., 1689., 2627., 1345.]
jul_sales = [1651., 1957.,  853., 2229., 2990., 3148., 2917.,  952., 1583., 2447., 2491.]
aug_sales = [2520., 2540., 1756., 1562., 972., 2258., 1413., 1779., 2503., 2860.]
sep_sales = [1827., 2003., 1349., 1858., 1370., 1076., 2897., 2238.,   91., 1951., 2509., 2933.]
oct_sales = [1273., 3169., 1192., 2219., 2195., 3157., 2912., 2012.,  722.,  922.]
nov_sales = [1827., 2003., 1349., 1858., 1370., 1076., 2897., 2238.,   91., 1951., 2509., 2933.]
dec_sales = [2200., 2460., 1260., 3157., 2912., 2012.,  722.,  922.]
jan=sum(np.array(jan_sales))
feb=sum(np.array(feb_sales))
mar= sum(np.array(mar_sales))
apr=sum(np.array(apr_sales))
may=sum(np.array(may_sales))
jun=sum(np.array(jun_sales))
jul=sum(np.array(jul_sales))
aug=sum(np.array(aug_sales))
sep=sum(np.array(sep_sales))
oct=sum(np.array(oct_sales))
nov=sum(np.array(nov_sales))
dec=sum(np.array(dec_sales))
sales=(sum(np.array(jan_sales)) + sum(np.array(feb_sales))+ sum(np.array(mar_sales))+sum(np.array(apr_sales))+sum(np.array(may_sales))+sum(np.array(jun_sales))
               + sum(np.array(jul_sales))+sum(np.array(aug_sales))+sum(np.array(sep_sales))+sum(np.array(oct_sales))+sum(np.array(nov_sales))+sum(np.array(dec_sales)))
total_months=len(jan_sales)+len(feb_sales)+len(mar_sales)+len(apr_sales)+len(may_sales)+len(jun_sales)+len(jul_sales)+len(aug_sales)+len(sep_sales) +len(oct_sales)+len(nov_sales)+len(dec_sales)
average_price=sales/total_months


cogs_percentage= input("Enter the cogs precentage as a fraction (e.g. 0.6): ")
cogs_percentage=float(cogs_percentage)
# Formulas for gross revenue
annual_gross_revenue=sales
monthly_gross_revenue=annual_gross_revenue/12;
q1_gross_revenue=(sum(np.array(jan_sales)) + sum(np.array(feb_sales))+ sum(np.array(mar_sales)))/3;
q2_gross_revenue=(sum(np.array(apr_sales))+sum(np.array(may_sales))+sum(np.array(jun_sales)))/3
q3_gross_revenue= (sum(np.array(jul_sales))+sum(np.array(aug_sales))+sum(np.array(sep_sales)) )/3
q4_gross_revenue = ( sum(np.array(oct_sales))+sum(np.array(nov_sales))+sum(np.array(dec_sales)))/3
#summarizes the gross revenue
print("annual gross revenue = ${:0.2f}".format(annual_gross_revenue))
print("{:.2f}\n{:.2f}".format(jan,feb))
print("quarterly gross revenue\nQ1= ${:.2f}\nQ2= ${:.2f}\nQ3= ${:.2f}\nQ4= ${:.2f}".format(q1_gross_revenue,q2_gross_revenue,q3_gross_revenue,q4_gross_revenue))
print("monthly gross revenue\njan= ${:.2f}\nfeb= ${:.2f}\nmar= ${:.2f}\napr= ${:.2f}\nmay= ${:.2f}\njun= ${:.2f}\njul= ${:.2f}\naug= {:.2f}\nsep= ${:.2f}\noct= ${:.2f}\nnov= ${:.2f}\ndec= ${:.2f}\n".format(jan,feb,mar,apr,may,jun,jul,aug,sep,oct,nov,dec))


# Formulas for net revenue
complement_cogs_percentage=1-cogs_percentage
annual_net_revenue=complement_cogs_percentage*annual_gross_revenue
monthly_net_revenue=annual_net_revenue/12
q1_net_revenue= q1_gross_revenue*complement_cogs_percentage
q2_net_revenue=q2_gross_revenue*complement_cogs_percentage
q3_net_revenue=q3_gross_revenue*complement_cogs_percentage
q4_net_revenue=q4_gross_revenue*complement_cogs_percentage
jan_net=jan*complement_cogs_percentage
feb_net=feb*complement_cogs_percentage
mar_net=mar*complement_cogs_percentage
apr_net=apr*complement_cogs_percentage
may_net=may*complement_cogs_percentage
jun_net=jun*complement_cogs_percentage
jul_net=jul*complement_cogs_percentage
aug_net=aug*complement_cogs_percentage
sep_net=sep*complement_cogs_percentage
oct_net=oct*complement_cogs_percentage
nov_net=nov*complement_cogs_percentage
dec_net=dec*complement_cogs_percentage
print("\nNow for the net revenues: \n")
#summarizes the net revenue
print("annual net revenue = ${:0.2f}".format(annual_net_revenue))
print("quarterly net revenue\nQ1= ${:.2f}\nQ2= ${:.2f}\nQ3= ${:.2f}\nQ4= ${:.2f}".format(q1_net_revenue,q2_net_revenue,q3_net_revenue,q4_net_revenue))
print("monthly net revenue\njan= ${:.2f}\nfeb= ${:.2f}\nmar= ${:.2f}\napr= ${:.2f}\nmay= ${:.2f}\njun= ${:.2f}\njul= ${:.2f}\naug= {:.2f}\nsep= ${:.2f}\noct= ${:.2f}\nnov= ${:.2f}\ndec= ${:.2f}\n".format(jan_net,feb_net,mar_net,apr_net,may_net,jun_net,jul_net,aug_net,sep_net,oct_net,nov_net,dec_net))