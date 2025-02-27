import time
import math
import random


class Jammer:
    """
    This class simulates jamming by introducing errors, increasing delay, or blocking messages.
    """
    def __init__(self, jamming_probability=0.3, noise_intensity=0.7, jamming_power_dbm=-70):
        self.jamming_probability = jamming_probability
        self.noise_intensity = noise_intensity  # Higher value increases interference
        self.jamming_power_dbm = jamming_power_dbm  # Default jamming signal power in dBm

    def jam_signal(self, message):
        selected_attack = 3
        if random.random() > self.jamming_probability:
            return message, False  

        print("[Jammer] Jamming message:", message)

        # Check if the message should be completely lost
        if random.random() < self.noise_intensity:
            print("[Jammer] Message completely lost!")
            return None, True  # Message is lost

        # Apply selected jamming attack
        if selected_attack == 1:
            result = self.cw_jamming(message)
        elif selected_attack == 2:
            result = self.pulsed_noise_jamming(message)
        elif selected_attack == 3:
            result = self.sweeping_jamming(message)
        elif selected_attack == 4:
            result = self.directional_jamming(message)
        elif selected_attack == 5:
            result = message, False  
        else:
            result = self.degrade_message(message) 

        return result
                    
    def jamming_signal_power(self):
        """Returns the power of the jamming signal in dBm."""
        return self.jamming_power_dbm

    def cw_jamming(self, message, frequency=1.0):
        self.noise_intensity = 1

        time_factor = time.time() * frequency
        interference = self.noise_intensity * (1 if int(time_factor) % 2 == 0 else -1)

        print("[Jammer] CW Jamming Active!")
        return self.degrade_message(message)


    def sweeping_jamming(self, message, min_freq=0.1, max_freq=5.0, sweep_rate=10):
        time_factor = time.time() * sweep_rate

        phase = time_factor % 2
        if phase < 1:
            sweep_freq = min_freq + (max_freq - min_freq) * phase
        else:
            sweep_freq = max_freq - (max_freq - min_freq) * (phase - 1)
        interference = 0.01 * (1 if int(time_factor * sweep_freq) % 2 == 0 else -1)

        print("[Jammer] Sweeping Jamming Active!")
        return self.degrade_message(message)

    def pulsed_noise_jammer(self, message):
            #randomize the pulse rate and width for more realism
            pulse_rate = random.uniform(8, 20) 
            pulse_width = random.uniform(0.1, 0.4) 
            time_factor = time.time() * pulse_rate
            pulse_active = (math.sin(time_factor * 2 * math.pi) > (1 - 2 * pulse_width))
            if pulse_active == True:
                distortion = self.noise_intensity * random.uniform(0.6, 1.5)
                print("[Jammer] Pulse Noise Jamming Active!")
                return self.interference_calc(message, distortion), True
            else:
                print("[Jammer] Pulse Noise Jammer Status: CLEAR")
                return message, False

    def directional_jamming(self, message, target_lat=37.7749, target_long=-122.4194, jamming_radius=0.01):
        drone_lat = message['latitude']
        drone_long = message['longitude']

        lat_diff = drone_lat - target_lat
        long_diff = drone_long - target_long
        squared_distance = lat_diff**2 + long_diff**2

        if squared_distance <= jamming_radius**2:
            #drone in range
            print("[Jammer] Directional Jamming Active - Target in range!")
            return self.degrade_message(message)
        else:
            #drone is out of range
            print("[Jammer] Drone outside jamming range - No interference.")
            return message, False

    def degrade_message(self, message):
        """Randomly corrupts the message or blocks it."""
        if random.random() < self.noise_intensity:
            print("[Jammer] Message completely lost!")
            return None, True  # Message is lost
        else:
            # Introduce random errors
            message['latitude'] += random.uniform(-0.1, 0.1)
            message['longitude'] += random.uniform(-0.1, 0.1)
            message['altitude'] += random.uniform(-100, 100)
            return message, True