#Travel Fare Calculator
FARE_RATE = 14 

name = input("Enter passenger name: ")
distance = float(input("Enter distance (km): "))
passengers = int(input("Enter number of passengers: "))

total_fare = distance*FARE_RATE*passengers

print("\nPassengers: ", name)
print("Total Fare: PHP", round(total_fare,2))

#Validation Rules:
#1.Passenger name -- Must not be empty
#2.Distance -- Number must be greater than 0
#3.Passengers -- Must be a positive whole number