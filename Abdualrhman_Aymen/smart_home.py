class SmartDevice:

    def __init__(self, device_id):
        self.device_id = device_id
        self.status = False

    def turn_on(self):
        self.status = True

    def turn_off(self):
        self.status = False


class SmartAC(SmartDevice):

    def __init__(self, device_id, temperature=24):
        super().__init__(device_id)
        self.__temperature = temperature

    def increase_temp(self):
        if self.__temperature < 30:
            self.__temperature += 1

    def decrease_temp(self):
        if self.__temperature > 16:
            self.__temperature -= 1

    def get_info(self):
        state = "ON" if self.status else "OFF"
        return (
            f"Device ID: {self.device_id}\n"
            f"Status: {state}\n"
            f"Temperature: {self.__temperature}°C\n"
        )


# إنشاء كائنين

hall_ac = SmartAC("Hall_AC")
room_ac = SmartAC("Room_AC")

hall_ac.turn_on()
hall_ac.increase_temp()
hall_ac.increase_temp()

room_ac.turn_on()
room_ac.decrease_temp()
room_ac.decrease_temp()

# حفظ النتائج داخل TXT

with open("AC_Status.txt", "w") as file:
    file.write("===== Hall AC =====\n")
    file.write(hall_ac.get_info())
    file.write("\n")

    file.write("===== Room AC =====\n")
    file.write(room_ac.get_info())

print("Data saved successfully.")