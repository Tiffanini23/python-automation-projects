#Workspace Rate Tracker 
members = ["Alice", "Thembi", "Langa", "Ayanda", "Michael"]
hourly_rate = 1

#Hours booked per member 
hours_booked = [4, 4, 6, 4, 9]

print("===Daily Booking Report===")

total_revenue = 0
total_hours = 0

for i in range (len(members)):
    member_revenue = hours_booked[i] * hourly_rate
    print(f"{members[i]}:{hours_booked[i]} hours = ${member_revenue}")
    total_revenue += member_revenue
    total_hours += hours_booked[i]

print(f"\nTotal Revenue: ${total_revenue}")
print(f"Total Member-Hours:{total_hours}")
print(f"Average hours per member:{total_hours/len(members):.1f}")
    
#Loyalty Tier System 
print('\n===Loyalty Tier System===')

for i in   range (len(members)):
      if   hours_booked[i] >= 9:
           tier = 'Gold'
           discount = 0.15
      elif hours_booked[i] >= 6:
           tier = 'Silver'
           discount = 0.10
      else:
           tier = 'Bronze'
           discount = 0.05

      print (f"{members[i]}: {tier} tier ({discount*100:.0f} % discount)") 
