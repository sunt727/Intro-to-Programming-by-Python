#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:32:50 2017

@author: sunt@mit.edu
"""

# 1_ps2 1B
# Name: Tuo Sun
# Collaborators: none
# Time Spent: 0:10
# Late Days Used: 0

"initialize information"

#annual salary
annual_salary = float(input("Enter your annual salary: "))
#a certain amount of your salary each month to saving for the down payment
portion_saved = float(input("Enter the percent of your salary to save, as a decimal: "))
#the cost of your dream home
total_cost = float(input("Enter the cost of your dream home: "))
#The semi-annual salary raise 
semi_annual_raise = float(input("Enter the semi-annual salary raise: "))

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
        
    


