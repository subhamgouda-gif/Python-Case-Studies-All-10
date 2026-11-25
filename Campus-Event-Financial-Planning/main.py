event_name = "Campus Innovation Day"
planned_attendees = 120
sponsorship = 25000
registration_fee = 550

venue_cost = 28000
equipment_cost = 9500
catering_per_person = 350
transport_per_person = 100
certificate_per_person = 50

fixed_cost = venue_cost + equipment_cost
variable_cost_per_person = (
    catering_per_person + transport_per_person + certificate_per_person
)
planned_variable_cost = variable_cost_per_person * planned_attendees
total_cost = fixed_cost + planned_variable_cost
registration_income = registration_fee * planned_attendees
total_income = sponsorship + registration_income
shortfall = total_cost - total_income

if shortfall < 0:
    shortfall = 0

if planned_attendees > 0:
    contribution_per_attendee = shortfall / planned_attendees
else:
    contribution_per_attendee = 0

print("=" * 76)
print("CAMPUS EVENT FINANCIAL PLANNING")
print("=" * 76)
print("Event:", event_name, "| planned attendees:", planned_attendees)
print("Fixed costs: venue", venue_cost, "+ equipment", equipment_cost)
print("Variable cost per attendee: catering", catering_per_person,
      "+ transport", transport_per_person, "+ certificate", certificate_per_person)
print("-" * 76)
print("Total cost:", round(total_cost, 2))
print("Registration income:", round(registration_income, 2))
print("Sponsorship:", round(sponsorship, 2))
print("Total income:", round(total_income, 2))
print("Funding shortfall:", round(shortfall, 2))
print("Contribution per planned attendee to cover shortfall:",
      round(contribution_per_attendee, 2))

registration_margin = registration_fee - variable_cost_per_person
if registration_margin <= 0 and sponsorship < fixed_cost:
    print("Break-even: impossible at this registration fee and sponsorship.")
elif registration_margin <= 0:
    print("Break-even: sponsorship covers fixed costs; extra registrations do not")
    print("cover variable costs at the current registration fee.")
else:
    registrations_needed = 0
    while registrations_needed < 10000:
        projected_income = sponsorship + registrations_needed * registration_fee
        projected_cost = fixed_cost + registrations_needed * variable_cost_per_person
        if projected_income >= projected_cost:
            break
        registrations_needed = registrations_needed + 1

    if registrations_needed == 10000:
        print("Break-even: not reached within the 10000-registration search limit.")
    else:
        print("Minimum registrations to break even:", registrations_needed)
        print("Projected income:",
              round(sponsorship + registrations_needed * registration_fee, 2),
              "| projected cost:",
              round(fixed_cost + registrations_needed * variable_cost_per_person, 2))

print("=" * 76)
