# Write a class Train which has methods to book a ticket,
# get Status(number of seats) and get Fare Information
# of trains running Under Indain Railways.

class Train:
    company="Indian Railways"
    def __init__(self,name,seats,fare):
        self.name=name
        self.seats=seats
        self.fare=fare


    def bookTicket(self):
        if(self.seats>0):
            print(f"Your Ticket is Booked!!! Your Seat Number is {self.seats}")
            self.seats=self.seats-1

        else:
            print("Sorry !!! All Tickets are Sold.")


    def getStatus(self):

        print("----------------------------------- Ticket Info---------------------------------------")

        print(f"The name of the train is : {self.name}")
        print(f"The seats available in {self.name} are {self.seats}")

        print("-----------------------------------Thank You!!!---------------------------------------")


    def getFare(self):
        print(f"The price for the Ticket of {self.name} is Rs. {self.fare}")


    def cancelTicket(self):
        print(f"Your Ticket For seat number {self.seats}  is cancelled")
        self.seats=self.seats+1





tms=Train("Delhi Express : 22714",300,90)

tms.getStatus()
tms.getFare()
tms.bookTicket()
tms.getStatus()




