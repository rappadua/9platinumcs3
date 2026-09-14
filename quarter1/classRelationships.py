class SmartWatch:
    def __init__(self, device_id: str, step_count: int, battery_level: float, heart_rate_monitor: bool):
        self.device_id = device_id                   
        self.step_count = step_count                 
        self._battery_level = battery_level           
        self.is_heart_rate_active = heart_rate_monitor 
      
    def log_steps(self, amount: int):
        """Adds steps and safely decreases battery level based on activity."""
        if amount > 0:
            self.step_count += amount
            battery_loss = (amount / 1000) * 1.0
            self._battery_level = max(0.0, self._battery_level - battery_loss)

    def toggle_heart_rate_monitor(self):
        """Toggles the heart rate monitor state."""
        self.is_heart_rate_active = not self.is_heart_rate_active

    def get_battery_level(self) -> float:
        """Safely reads the private battery level attribute."""
        return self._battery_level


class UserAccount:
    """New class representing a fitness user managing one or more SmartWatches."""
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email
        self.devices = [] 

    def register_device(self, watch: SmartWatch):
        """Adds a SmartWatch object reference to the user's devices list."""
        self.devices.append(watch)

    def display_connected_devices(self):
        """Iterates through all linked SmartWatch objects to fetch and display data."""
        if not self.devices:
            print(f"No devices connected to account '{self.username}'.")
            return

        print(f"Devices connected to account: {self.username} ({self.email})")
        for watch in self.devices:
            print(f" - Device ID: {watch.device_id} | Steps: {watch.step_count} | Battery: {watch.get_battery_level()}%")


user = UserAccount(username="AlexRunner", email="alex@example.com")

watch1 = SmartWatch(device_id="SW-101", step_count=2500, battery_level=95.0, heart_rate_monitor=False)
watch2 = SmartWatch(device_id="SW-202", step_count=1000, battery_level=80.0, heart_rate_monitor=True)
watch3 = SmartWatch(device_id="SW-303", step_count=8200, battery_level=60.0, heart_rate_monitor=True)

print("=== BEFORE RELATIONSHIP ===")[cite: 3]
print(f"Created User: {user.username}")
print(f"Created Devices: {watch1.device_id}, {watch2.device_id}, {watch3.device_id}\n")

print("=== BUILDING RELATIONSHIP ===")[cite: 3]
user.register_device(watch1)[cite: 3]
user.register_device(watch2)[cite: 3]
user.register_device(watch3)[cite: 3]
print("Registering SmartWatch objects to AlexRunner's account...\n")

print("=== AFTER RELATIONSHIP ===")[cite: 3]
user.display_connected_devices()[cite: 3]
