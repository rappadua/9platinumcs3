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
            # Deduct 1% battery for every 1000 steps taken
            battery_loss = (amount / 1000) * 1.0
            self._battery_level = max(0.0, self._battery_level - battery_loss)

    def toggle_heart_rate_monitor(self):
        """Toggles the heart rate monitor state."""
        self.is_heart_rate_active = not self.is_heart_rate_active

    def get_battery_level(self) -> float:
        """Safely reads the private battery level attribute."""
        return self._battery_level


watch1 = SmartWatch(device_id="SW-101", step_count=2500, battery_level=95.0, heart_rate_monitor=False)
watch2 = SmartWatch(device_id="SW-202", step_count=1000, battery_level=80.0, heart_rate_monitor=True)

print("=== BEFORE ACTION ===")
print(f"Watch 1 ({watch1.device_id}) -> Steps: {watch1.step_count}, Battery: {watch1.get_battery_level()}%")
print(f"Watch 2 ({watch2.device_id}) -> Steps: {watch2.step_count}, Battery: {watch2.get_battery_level()}%\n")

print("--> Performing action: Logging 5000 steps on Watch 1...\n")
watch1.log_steps(5000)

print("=== AFTER ACTION ===")
print(f"Watch 1 ({watch1.device_id}) -> Steps: {watch1.step_count}, Battery: {watch1.get_battery_level()}%")
print(f"Watch 2 ({watch2.device_id}) -> Steps: {watch2.step_count}, Battery: {watch2.get_battery_level()}%")
