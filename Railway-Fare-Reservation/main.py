passengers = [
    ("Anil", 35, "Sleeper", 350, "BOOK"),
    ("Maya", 65, "AC3", 260, "BOOK"),
    ("Ritu", 10, "Sleeper", 180, "CANCEL"),
]

classes = [
    ("Sleeper", 1.20, 40),
    ("AC3", 2.00, 80),
    ("AC2", 3.00, 120),
]

print("=" * 68)
print("RAILWAY FARE AND RESERVATION CALCULATOR")
print("=" * 68)
print("Distance slabs: first 100 km at base rate, next 200 at 1.5x,")
print("remaining distance at 2x. Child concession 50%; senior concession 40%.")
print("Reservation fee is class-based. Cancellation penalty is 25% of fare.")
print("-" * 68)

for passenger in passengers:
    name, age, class_name, distance, action = passenger
    class_found = False
    base_rate = 0
    reservation_fee = 0

    for rail_class in classes:
        rail_name, rail_rate, rail_reservation_fee = rail_class
        if rail_name == class_name:
            class_found = True
            base_rate = rail_rate
            reservation_fee = rail_reservation_fee

    if not class_found or age < 0 or distance <= 0:
        print(name, "- INVALID passenger, class, or distance.")
    else:
        slabs = [(100, base_rate), (200, base_rate * 1.5),
                 (999999, base_rate * 2)]
        remaining_distance = distance
        distance_fare = 0

        for slab_distance, slab_rate in slabs:
            if remaining_distance > 0:
                if remaining_distance < slab_distance:
                    charged_distance = remaining_distance
                else:
                    charged_distance = slab_distance
                distance_fare = distance_fare + charged_distance * slab_rate
                remaining_distance = remaining_distance - charged_distance

        concession_rate = 0
        if age <= 12:
            concession_rate = 0.50
        elif age >= 60:
            concession_rate = 0.40

        discounted_distance_fare = distance_fare * (1 - concession_rate)
        total_fare = discounted_distance_fare + reservation_fee

        if action == "CANCEL":
            cancellation_fee = total_fare * 0.25
            refund = total_fare - cancellation_fee
            print(name, "| cancellation fee:", round(cancellation_fee, 2),
                  "| refund:", round(refund, 2))
        else:
            print(name, "| class:", class_name, "| distance:", distance,
                  "| concession:", round(concession_rate * 100, 0), "%",
                  "| reservation:", reservation_fee,
                  "| fare:", round(total_fare, 2))

print("=" * 68)
