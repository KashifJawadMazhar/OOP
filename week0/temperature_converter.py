class TemperatureConverter:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def setTemperature(self, temperature) -> None:
        self.temperature = temperature

    def toCelsius(self):
        return f'{self.temperature} C'

    def toFahrenheit(self):
        return f'{(self.temperature * 9/5) + 32} F'

    def toKelvin(self):
        return f'{self.temperature + 273.15} K'