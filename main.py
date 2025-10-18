from turbine import Turbine

import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def create_production_graphic(turbine, step):
    max_flow = turbine.calculate_max_steam_flow()

    x_values = np.linspace(0, max_flow + (max_flow * 0.1), step)

    y_values = []
    for dx in x_values:
        y_values.append(turbine.produce_energy(dx))

    plt.style.use("dark_background")
    _, ax = plt.subplots(layout="constrained")
    ax.set_title("Turbine Energy Production")
    ax.grid(True)

    ax.set_ylabel("Energy Production (FE/t)")
    ax.set_xlabel("Steam Flow (mb/t)")

    ax.get_yaxis().set_major_formatter(ticker.FuncFormatter(lambda x, p: format(int(x), ',')))

    ax.plot(x_values, y_values)
    plt.show()

if __name__ == '__main__':
    turbine = Turbine(17, 18, 10, 20, 585, 224, 5)

    create_production_graphic(turbine, 1000)

    max_steam_flow = turbine.calculate_max_steam_flow()
    steam_storage = turbine.calculate_steam_storage()

    energy_storage = turbine.calculate_energy_storage()
    max_energy_production = turbine.produce_energy(max_steam_flow)

    print("=========================================")
    print(f"Max Steam Storage: {steam_storage} mb | {steam_storage / max_steam_flow:1.3} ticks before full")
    print(f"Max Steam Flow: {max_steam_flow:1.0f} mb/t -> {max_steam_flow / steam_storage * 100:1.1f}% of storage per tick")
    print(" ")
    print(f"Energy Storage: {energy_storage:1.0f} FE | {energy_storage / max_energy_production:1.3f} ticks before full")
    print(f"Max Energy Production: {np.floor(max_energy_production)} -> {max_energy_production / energy_storage * 100:1.1f}% of storage per tick")
