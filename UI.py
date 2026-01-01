class UI:

    def message(self, msg):
        print(msg)

    def customer_form(self):
        print("Customer account creation form")
        name = input("Enter customers name: ")
        email = input("Enter customers email: ")
        phone = input("Enter customers phone: ")
        customer_type = input("Enter customers type (INDIVIDUAL, TEAM): ")
        return {
            "name":name,
            "email":email,
            "phone":phone,
            "customer_type":customer_type
        }

    def hall_form(self):
        print("Hall creation form")
        name = input("Enter hall name: ")
        sport_type = input("Select hall sport type (options FOOTBALL, BASKETBALL, VOLLEYBALL, BADMINTON, HANDBALL, FLORBALL): ")
        if sport_type.upper() not in ["FOOTBALL", "BASKETBALL", "VOLLEYBALL", "BADMINTON", "HANDBALL", "FLORBALL"]:
            print("Invalid sport type")
            self.hall_form()
        hourly_rate = float(input("Enter hall hourly rate: "))
        if hourly_rate < 0:
            print("Invalid hourly rate")
            self.hall_form()
        capacity = int(input("Enter hall capacity: "))
        if capacity <= 0:
            print("Invalid capacity")
            self.hall_form()
        return {
            "name":name,
            "sport_type":sport_type.upper(),
            "hourly_rate":hourly_rate,
            "capacity":capacity
        }

    def service_form(self):
        print("Service creation form")
        name = input("Enter service name: ")
        price_per_hour = float(input("Enter service price per hour: "))
        if price_per_hour < 0:
            print("Invalid price per hour")
            self.service_form()
        optional = input("Is service optional (Y/N): ")
        if optional.upper() == "Y":
            optional = True
        elif optional.upper() == "N":
            optional = False
        else:
            print("Invalid input")
            self.service_form()

        return {
            "name":name,
            "price_per_hour":price_per_hour,
            "optional":optional
        }

    def menu(self, actions:dict):
        print("Available actions:")
        for key, value in actions.items():
            print(f"{key}: {value.__name__}")