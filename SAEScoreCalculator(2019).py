#SAE Aero Design Advanced Class Flight score calculator
NumRounds=int(input("Enter Number of Rounds: ")) #Takes user input for number of rounds in competition
Colonists=int(input("Enter Colonist number: ")) #Takes user input for amount of passengers on CDA
Habitats=int(input("Enter Habitat number: ")) #Takes user input for number of Nerf balls to be dropped
Water=float(input("Enter Water Bottle weight (fl oz): ")) #Takes user input for number of water bottles to be dropped
WatMod=Water*16.9 #Converts amount of water bottels to its weight in fluid ounces
StaticPayload=float(input("Enter Static Payload weight (lbs): ")) #Takes user input for amount of static payload on PA (under the assumption that static payload is constant)
Range1=Colonists/(8*Habitats) #Finds first range for score calculation
Range2=Colonists/WatMod #Finds second range for score calculation
Payload=1-(max(Range1,Range2)) #Determines vaule of current payload ratios
DaysHabitable=25*(2**Payload) #Determines amount of days colony will function using current payload calculation
FlightScore1=(Colonists*DaysHabitable)/(15*NumRounds) #Determines first part of flight score based on passengers, days, and rounds in competition
FlightScore2=(2*StaticPayload)/NumRounds #Determines second part of flight score based on static paylod and rounds in competition
FinalFS=FlightScore1+FlightScore2 #Determines culmulative flight score
print("Maximum score possible:")
print(FinalFS)