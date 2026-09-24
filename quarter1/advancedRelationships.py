class Device:
    def __init__(self, device_id: str, brand: str):
        self.device_id = device_id
        self.brand = brand

    def get_device_info(self) -> str:
        return f"ID: {self.device_id} | Brand: {self.brand}"

class HeartRateSensor:
    def __init__(self, sensor_model: str):
        self.sensor_model = sensor_model
        self.is_active = False

    def toggle_sensor(self):
        self.is_active = not self.is_active

class SmartWatch(Device):
    def __init__(self, device_id: str, brand: str, step_count: int, battery_level: float, sensor_model: str):
        super().__init__(device_id, brand)
        
        self.step_count = step_count
        self._battery_level = battery_level
        
        self.sensor = HeartRateSensor(sensor_model)

    def log_steps(self, amount: int):
        if amount > 0:
            self.step_count += amount
            battery_loss = (amount / 1000) * 1.0
            self._battery_level = max(0.0, self._battery_level - battery_loss)

    def get_battery_level(self) -> float:
        return self._battery_level


class UserAccount:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.devices = []

    def register_device(self, watch: SmartWatch):
        self.devices.append(watch)

    def display_connected_devices(self):
        if not self.devices:
            print(f"No devices connected to account '{self.username}'.")
            return

        print(f"Devices connected to account: {self.username} ({self.email})")
        for watch in self.devices:
            sensor_status = "Active" if watch.sensor.is_active else "Inactive"
            print(f" - {watch.get_device_info()} | Steps: {watch.step_count} | Battery: {watch.get_battery_level()}% | Sensor ({watch.sensor.sensor_model}): {sensor_status}")


if __name__ == "__main__":
    print("=== TEST 1: INHERITANCE & COMPOSITION INITIALIZATION ===")
    watch1 = SmartWatch(device_id="SW-101", brand="FitTech", step_count=2500, battery_level=95.0, sensor_model="HR-V2")
    watch2 = SmartWatch(device_id="SW-202", brand="FitTech", step_count=1000, battery_level=80.0, sensor_model="HR-V2")

    print(f"Watch 1 Inherited Info: {watch1.get_device_info()}")
    print(f"Watch 1 Internal Sensor Model: {watch1.sensor.sensor_model}\n")

    print("=== TEST 2: TOGGLING COMPOSED OBJECT & LOGGING STEPS ===")
    watch1.sensor.toggle_sensor()
    watch1.log_steps(3000)
    print("Toggled watch1 sensor to ON and logged 3000 steps.\n")

    print("=== TEST 3: SYSTEM INTEGRATION WITH USER ACCOUNT ===")
    user = UserAccount(username="AlexRunner", email="alex@example.com")
    user.register_device(watch1)
    user.register_device(watch2)
    user.display_connected_devices()
