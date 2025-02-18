import numpy as np

class CWJammer:
    """
    A Continuous Wave (CW) Jammer that continuously transmits a jamming signal 
    to interfere with ADS-B communications.
    """
    def __init__(self, jamming_power_dbm=-50):
        """
        :param jamming_power_dbm: Power of the jamming signal in dBm.
        """
        self.jamming_power_dbm = jamming_power_dbm

    def jamming_signal_power(self):
        """
        Returns the effective jamming signal power in dBm.
        """
        return self.jamming_power_dbm

    def generate_signal(self, duration=1.0, sample_rate=1e6, frequency=1090e6):
        """
        Generates a CW jamming signal.
        :param duration: Duration of the signal in seconds.
        :param sample_rate: Number of samples per second.
        :param frequency: Frequency of the CW jammer (ADS-B operates at 1090 MHz).
        :return: Numpy array of the generated signal.
        """
        t = np.arange(0, duration, 1/sample_rate)
        signal = np.sin(2 * np.pi * frequency * t)  # CW signal
        return signal
