line = "-" * 40 
print(line)

#Freelance rate calculator
print("===Freelance Earning Calculator===")

#Get user input
hourly_rate = float(input("Your hourly rate (USD):$"))
hours_worked = float(input("Hours worked this week:"))

#Calculate
weekly_usd = hourly_rate * hours_worked
monthly_usd = weekly_usd * 4
monthly_eur = monthly_usd * 0.92  # USD to EUR conversion

#Display results
print(f"Weekly:${weekly_usd}")
print(f"Monthly:${monthly_usd:.2f}(€{monthly_eur:.2f})")

#New Macbook M5 16"
target = 3500
if monthly_eur >= target:
   print("✅ You've got enough to buy a brand new Macbook M5 16"!")
else:
   gap = target - monthly_eur
   print(f" ❌ You dont €{gap:.2f} more/month for Macbook M5 16"!")
  
print(line) 
