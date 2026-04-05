import csv
from pathlib import Path

import matplotlib.pyplot as plt


def load_data(csv_path: Path) -> dict[str, list[float]]:
    data = {
        "omega_rad_s": [],
        "U_ind_V": [],
        "U_k_10ohm_V": [],
        "U_k_100ohm_V": [],
        "U_k_1000ohm_V": [],
        "U_theo_V": [],
    }

    with csv_path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            for key in data:
                data[key].append(float(row[key]))

    return data


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    csv_path = project_dir / "data.csv"
    plots_dir = project_dir / "plots"
    plots_dir.mkdir(exist_ok=True)

    data = load_data(csv_path)

    plt.figure(figsize=(8, 5))
    plt.plot(data["omega_rad_s"], data["U_ind_V"], marker="o", label="U_ind")
    plt.plot(data["omega_rad_s"], data["U_k_10ohm_V"], marker="s", label="U_k (10 Ω)")
    plt.plot(data["omega_rad_s"], data["U_k_100ohm_V"], marker="^", label="U_k (100 Ω)")
    plt.plot(data["omega_rad_s"], data["U_k_1000ohm_V"], marker="d", label="U_k (1000 Ω)")
    plt.plot(data["omega_rad_s"], data["U_theo_V"], marker="x", label="U_theo")

    plt.xlabel("Angular velocity ω (rad/s)")
    plt.ylabel("Voltage U (V)")
    plt.title("E15: Voltage as a Function of Angular Velocity")
    plt.legend()
    plt.tight_layout()

    output_path = plots_dir / "voltage_vs_omega.png"
    plt.savefig(output_path, dpi=300)
    plt.close()

    print(f"Plot saved to: {output_path}")


if __name__ == "__main__":
    main()
