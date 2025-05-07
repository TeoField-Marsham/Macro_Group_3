# Solow model simulation for Sweden done by Lynn
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load parameters
def load_params_from_excel(path="pwt100.xlsx", country="Sweden", start_year=1999, end_year=2019):
    df = pd.read_excel(path, sheet_name="Data")
    sweden = df[df['country'] == country]
    years = (sweden['year'] >= start_year) & (sweden['year'] <= end_year)
    data = sweden.loc[years].sort_values("year").reset_index(drop=True).copy()

    alpha = 1 - data['labsh'].mean()
    n = data['pop'].pct_change().mean()
    delta = data['delta'].mean()
    g = (data['rgdpna'] / data['pop']).pct_change().mean()
    s = data['csh_i'].mean()
    s_new = s * 1.1

    return {
        "alpha": alpha,
        "s": s,
        "s_new": s_new,
        "n": n,
        "g": g,
        "delta": delta,
        "shock_period": 20,
        "T": 100,
        "k0": 0.5
    }

params = load_params_from_excel()

time = np.arange(1, params["T"] + 1)
A_t = (1 + params["g"]) ** np.arange(params["T"])


def simulate_capital_path(T, alpha, s_pre, s_post, n, g, delta, k0, shock_period=None):
    k = np.zeros(T)
    k[0] = k0
    for t in range(1, T):
        s = s_pre if (shock_period is None or t < shock_period) else s_post
        k[t] = (s * k[t - 1] ** alpha + (1 - delta) * k[t - 1]) / ((1 + n) * (1 + g))
    return k


def compute_series(k, A, s_rate):
    y = k ** params["alpha"]
    c = (1 - s_rate) * y if np.isscalar(s_rate) else (1 - np.array(s_rate)) * y
    k_per_eff, y_per_eff, c_per_eff = k / A, y / A, c / A
    ln_y, ln_c = np.log(y), np.log(c)
    g_y = np.zeros_like(y)
    g_y[1:] = ln_y[1:] - ln_y[:-1]
    return pd.DataFrame({
        "k_per_eff": k_per_eff, "y_per_eff": y_per_eff, "c_per_eff": c_per_eff,
        "A": A, "k": k, "y": y, "c": c,
        "ln_y": ln_y, "ln_c": ln_c, "g_y": g_y
    })


def get_combined_data():
    k_growth = simulate_capital_path(
        T=params["T"], alpha=params["alpha"], s_pre=params["s"], s_post=params["s"],
        n=params["n"], g=params["g"], delta=params["delta"], k0=params["k0"]
    )
    k_shock = simulate_capital_path(
        T=params["T"], alpha=params["alpha"], s_pre=params["s"], s_post=params["s_new"],
        n=params["n"], g=params["g"], delta=params["delta"], k0=params["k0"], shock_period=params["shock_period"]
    )

    s_vector = [params["s"]] * params["shock_period"] + [params["s_new"]] * (params["T"] - params["shock_period"])

    df_growth = compute_series(k_growth, A_t, params["s"])
    df_shock = compute_series(k_shock, A_t, s_vector)

    df_growth["case"] = "no shock with growth"
    df_shock["case"] = "shock with growth"

    df_all = pd.concat([df_growth, df_shock], ignore_index=True)
    df_all["Period"] = np.tile(time, 2)
    return df_all

def plot_all_combined(df_all):
    plot_vars = {
        "k_per_eff": "Capital per Effective Worker (k̃ₜ)",
        "y_per_eff": "Output per Effective Worker (Žₜ)",
        "c_per_eff": "Consumption per Effective Worker (čₜ)",
        "k": "Capital per Worker (kₜ)",
        "y": "Output per Worker (yₜ)",
        "c": "Consumption per Worker (cₜ)",
        "ln_y": "Log of Output per Worker (ln(yₜ))",
        "ln_c": "Log of Consumption per Worker (ln(cₜ))",
        "g_y": "Growth of Output per Worker (g˨ₜ)"
    }

    colors = {"no shock with growth": "#1f77b4", "shock with growth": "#ff7f0e"}
    styles = {"no shock with growth": "-", "shock with growth": "--"}
    plot_order = ["no shock with growth", "shock with growth"]

    n_vars = len(plot_vars)
    n_cols = 3
    n_rows = (n_vars + n_cols - 1) // n_cols

    fig, axes = plt.subplots(n_rows, n_cols, figsize=(18, 4.5 * n_rows), sharex=False)
    axes = axes.flatten()

    for idx, (var, title) in enumerate(plot_vars.items()):
        ax = axes[idx]
        ax.axvline(x=params["shock_period"], color="gray", linestyle="-", zorder=0)

        for i, label in enumerate(plot_order):
            group = df_all[df_all["case"] == label]
            ax.plot(group["Period"], group[var],
                    label=label,
                    color=colors[label],
                    linestyle=styles[label],
                    linewidth=2.0,
                    zorder=i + 1)

        ax.set_title(title, fontsize=12)
        ax.set_ylabel(title, fontsize=10)
        ax.grid(True, linestyle='--', alpha=0.6)
        ax.legend(loc="best", fontsize=9)

    # Hide any unused subplots
    for j in range(n_vars, len(axes)):
        fig.delaxes(axes[j])

    for idx, ax in enumerate(axes):
        ax.set_xlabel("Period", fontsize=10)
        ax.tick_params(axis='both', labelsize=9)
        ax.margins(x=0)
        ax.set_xlim(left=0)

    plt.tight_layout()
    os.makedirs("solow_plots", exist_ok=True)
    plt.savefig("solow_plots/solow_combined_grid.png", dpi=150)
    plt.close()

def compute_steady_state(s):
    denom = params["n"] + params["g"] + params["delta"]
    kstar = (s / denom) ** (1 / (1 - params["alpha"]))
    ystar = kstar ** params["alpha"]
    return kstar, ystar


def print_steady_state_changes():
    k_before, y_before = compute_steady_state(params["s"])
    k_after, y_after = compute_steady_state(params["s_new"])

    k_change_in_percent = ((k_after - k_before) / k_before) * 100
    y_change_in_percent = ((y_after - y_before) / y_before) * 100

    print(f"Steady state per worker before shock: {k_before:.3f}")
    print(f"Steady state per worker after shock: {k_after:.3f}")
    print(f"Change in steady state per worker: {k_change_in_percent:.1f}%\n")

    print(f"Steady state output per worker before: {y_before:.3f}")
    print(f"Steady state output per worker after : {y_after:.3f}")
    print(f"Change in output: {y_change_in_percent:.1f}%")

    print("\nParameters for Sweden (1999-2019):")
    print(f"  Capital share (alpha): {params['alpha']:.4f}")
    print(f"  Population growth rate (n): {params['n']:.4f}")
    print(f"  Output per capita growth rate (g): {params['g']:.4f}")
    print(f"  Depreciation rate (delta): {params['delta']:.4f}")
    print(f"  Investment rate (s): {params['s']:.4f}")
    print(f"  Investment rate (s_new) after shock: {params['s_new']:.4f}\n")

if __name__ == "__main__":
    df_all = get_combined_data()
    df_all.to_csv("solow_timeseries_sweden.csv", index=False)
    plot_all_combined(df_all)
    print_steady_state_changes()
    print("done")
