MAX_BLADES = 28 #HARD CODED IN MEKANISM CODE
JOULES_TO_RF = 2.5

BLADES_PER_COIL = 4                     #Default: 4
VENT_GAS_FLOW = 256000.0                #Default: 32000
DISPENSER_GAS_FLOW = 10240.0            #Default: 1280
GAS_PER_TANK = 512000                  #Default: 64000
MAX_ENERGY_PER_STEAM = 10               #Default: 10
ENERGY_CAPACITY_PER_VOLUME = 16000000   #Default: 16000000

class Turbine:
    def __init__(self, width, height, rotor_count, blades_count, vents_count, pressure_dispenser_count, coil_count):
        self.width = width
        self.width_sq = width ** 2
        self.height = height

        self.rotor_count = rotor_count
        self.blades_count = blades_count

        self.vents_count = vents_count
        self.pressure_dispenser_count = pressure_dispenser_count
        self.coil_count = coil_count

    # Storage
    def calculate_steam_storage(self):
        return self.width_sq * self.rotor_count * GAS_PER_TANK

    def calculate_energy_storage(self):
        return (self.width_sq * self.height * ENERGY_CAPACITY_PER_VOLUME) / JOULES_TO_RF

    # Production
    def calculate_blade_rate(self):
        a = self.blades_count / MAX_BLADES
        b = self.coil_count * BLADES_PER_COIL / MAX_BLADES

        return min(a, b)

    def calculate_max_steam_flow(self):
        a = self.vents_count * VENT_GAS_FLOW
        b = self.width_sq * self.rotor_count * self.pressure_dispenser_count * DISPENSER_GAS_FLOW

        return min(a, b)

    # Energy

    def produce_energy(self, steam_flow):
        return (MAX_ENERGY_PER_STEAM * self.calculate_blade_rate() * min(steam_flow, self.calculate_max_steam_flow())) / JOULES_TO_RF #converts to FE
