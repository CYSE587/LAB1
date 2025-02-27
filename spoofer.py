import random
import numpy as np
import time

class Spoofer:
    """
    This class simulates  spoofing with gradual change
    Instead of a one-time random change it gradually drifts the drones
    reported latitude, longitude, and altitude. very slowly.
    """
    def __init__(self, spoof_probability=1, fake_drone_id="FAKE123"):
        self.spoof_probability = spoof_probability
        self.fake_drone_id = fake_drone_id
        # Initialize offset
        self.lat_offset = 0.0
        self.lon_offset = 0.0
        self.alt_offset = 0.0
        

    def spoof_message(self, message):
        """
        This is going to take the original message and drift incrementally
        by 0-0.05 with lat/lon and between -0.05 to 0.05 in alt.
        This will simulate gradual spoofing with a drone slowly veering off course.
        """
        if random.random() < self.spoof_probability:
            self.lon_offset
            # Update offsets gradually
            self.lat_offset += random.uniform(0, 0.05)
            self.lon_offset += random.uniform(0, 0.05)
            self.alt_offset += random.uniform(-0.05, 0.05)
            
            spoofed_message = message.copy()
 
            spoofed_message['latitude'] += self.lat_offset
            print("Spoofed Lat: ",spoofed_message['latitude'])
            spoofed_message['longitude'] += self.lon_offset
            print("Spoofed Lon: ",spoofed_message['longitude'])
            spoofed_message['altitude'] += self.alt_offset
            print("Spoofed Alt: ",spoofed_message['altitude'])
            spoofed_message['drone_id'] = self.fake_drone_id if random.random() < 0.5 else message['drone_id']
            return spoofed_message, True
        return message, False