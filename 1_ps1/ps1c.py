#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 09:32:50 2017

@author: sunt@mit.edu
"""

# 1_ps2 1C
# Name: Tuo Sun
# Collaborators: none
# Time Spent: 0:45
# Late Days Used: 0


"initialize information"

# initial_deposit
initial_deposit = float(input("Enter the initial deposit: "))

"default information"
# the cost of your dream home
total_cost = 800000
# the portion of the cost needed for a down payment
portion_down_payment = 0.3
# best annual return rate
best_r = 0
# the number of months required
months = 48
# down payment
down_payment = total_cost * portion_down_payment
# Steps in bisection search
steps = 0
# Low estimated number
low = 0
# high estimated number
high = 1
# Initialize current saving as initial deposit
current_savings = initial_deposit

"Calculation running code"

# Testify whether deposit is higher than down payment%
if initial_deposit < down_payment:

    # Make sure best annual return rate less than 100%
    if initial_deposit * ((1 + 1 / 12) ** (months)) > down_payment:

        # your savings to be within $100 of the required down payment
        while abs(current_savings - down_payment) > 100:

            best_r = int((high + low) / 2 * 10000) / 10000  # make the result in 4 digits precision
            steps += 1
            current_savings = initial_deposit * ((1 + best_r / 12) ** (months))

            # if guess number is less than best annual return rate, make lower number as best annual return rate
            if current_savings < down_payment:
                low = best_r
            else:
                # if guess number is higher than best annual return rate, make high number as best annual return rate
                high = best_r

        print("Best savings rate: ", best_r, " [or very close to this number]")
        print("Steps in bisection search: ", steps, " [or very close to this number]")


    else:
        best_r = 'It is not possible to pay the down payment in three years.'
        print("Best savings rate:", best_r)
        print("Steps in bisection search: [May vary based on how you " \
              "implemented your bisection search]")


else:
    print("Best savings rate: ", 0.0, " [or very close to this number]")
    print("Steps in bisection search: [May vary based on how you " \
          "implemented your bisection search]")
