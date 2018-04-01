def part_b(annual_salary, portion_saved, total_cost, semi_annual_raise):
	
	"default information"
	
	#the portion of the cost needed for a down payment
	portion_down_payment = 0.18
	#start with a current savings of $0
	current_savings = 0
	#an annual return rate
	r = 0.03
	#the number of months required
	months = 1
	
	# monthly salary
	monthly_salary = annual_salary/12
	
	#down payment
	down_payment = total_cost*portion_down_payment
	
	"Calculation running code"
	
	#assume you can make money for maximum 1000 months"
	while months < 1000:
	    #current saving increases by monthly rate and portion saved
	    current_savings = current_savings * (1 + (r/12))
	    current_savings += (monthly_salary * portion_saved)
	    
	    #raise your monthly salary every six months
	    if months%6 == 0:
	        monthly_salary *= (1 + semi_annual_raise)
	        
	    #make a comparison between your current saving and down payment
	    if  current_savings > down_payment:
	        #print the results of how many months you need to save money
	        print("Number of months: " + str(months))
	        break
	    else:
	        months+=1
	        
	    
	
	
	return months