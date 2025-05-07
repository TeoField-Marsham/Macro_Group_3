import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Task 2b) load data
df = pd.read_excel('../data/pwt100.xlsx', sheet_name='Data', engine='openpyxl')
nor = df[df['countrycode'] == 'NOR'].sort_values('year').reset_index(drop=True)
years = nor['year'].values

nor['y_pc'] = nor['rgdpo'] / nor['pop']
pop_growth = nor['pop'].pct_change().dropna()  # (pop_t / pop_{t-1}) - 1

# Parameters
alpha = 1 - nor['labsh'].mean()
A0 = 1.0
delta = nor['delta'].mean()
n = pop_growth.mean()
s = nor['csh_i'].mean()
g1 = (nor['rgdpna'] / nor['pop']).pct_change().mean()

shock_size = 0.005
g2 = g1 + shock_size

print("Parameters:")
print(f"alpha = {alpha:.4f}, A0 = {A0:.4f}, delta = {delta:.4f}, n = {n:.4f}, g = {g1:.4f}, s= {s:.4f} ")
print(f"shock_size = {shock_size:.4f}, g2 = {g2:.4f} ")


# Task 2c)
# Steady‑state values
def steady_state(g):
    kstar = (s / (n + g + delta + n * g)) ** (1 / (1 - alpha))
    cstar = (1 - s) * (s / (n + g + delta + n * g)) ** (alpha / (1 - alpha))
    ystar = (s / (n + g + delta + n * g)) ** (alpha / (1 - alpha))
    return kstar, cstar, ystar


kstar1, cstar1, ystar1 = steady_state(g1)
kstar2, cstar2, ystar2 = steady_state(g2)

# Task 2f) - simulation setup
T = 101
tt = np.arange(T)
tt_g = np.arange(1, T)
shock_year = 20


# Task 2d) & 2f)
def simulate_economy(g_schedule_arr):
    A = np.empty(T)
    k_tilde = np.empty(T)
    y_tilde = np.empty(T)
    c_tilde = np.empty(T)

    k = np.empty(T)
    y = np.empty(T)
    c = np.empty(T)
    ln_y = np.empty(T)
    ln_c = np.empty(T)
    k_over_y = np.empty(T)

    kstar, *_ = steady_state(g_schedule_arr[0])
    A[0] = A0 * (1 + g_schedule_arr[0])
    k_tilde[0] = kstar
    y_tilde[0] = kstar ** alpha
    c_tilde[0] = (1 - s) * y_tilde[0]

    k[0] = k_tilde[0] * A[0]
    y[0] = y_tilde[0] * A[0]
    c[0] = c_tilde[0] * A[0]
    ln_y[0] = np.log(y[0])
    ln_c[0] = np.log(c[0])
    k_over_y[0] = k[0] / y[0]

    kprev_tilde = k_tilde[0]

    for t in range(1, T):
        k_tilde[t] = (s * kprev_tilde ** alpha + (1 - delta) * kprev_tilde) / ((1 + n) * (1 + g_schedule_arr[t]))

        y_tilde[t] = k_tilde[t] ** alpha
        c_tilde[t] = (1 - s) * y_tilde[t]

        A[t] = A[t - 1] * (1 + g_schedule_arr[t])
        k[t] = k_tilde[t] * A[t]
        y[t] = y_tilde[t] * A[t]
        c[t] = c_tilde[t] * A[t]
        ln_y[t] = np.log(y[t])
        ln_c[t] = np.log(c[t])
        k_over_y[t] = k[t] / y[t]

        kprev_tilde = k_tilde[t]

    growth_y = ln_y[1:] - ln_y[:-1]
    return {
        "A": A, "k_tilde": k_tilde, "y_tilde": y_tilde, "c_tilde": c_tilde,
        "k": k, "y": y, "c": c, "ln_y": ln_y, "ln_c": ln_c,
        "k_over_y": k_over_y, "growth_y": growth_y
    }


# Task 2d)
g_schedule = np.full(T, g1)
g_schedule[shock_year:] = g2

g_base = np.full(T, g1)
g_shock = g_schedule

eco_base = simulate_economy(g_base)
eco_shock = simulate_economy(g_shock)


# Task 2c)
print("Steady‑state values:")
print(f"pre shock  k* = {kstar1:.4f}   c* = {cstar1:.4f}   y* = {ystar1:.4f}")
print(f"post shock  k* = {kstar2:.4f}   c* = {cstar2:.4f}   y* = {ystar2:.4f}\n")

# Task 2e)
print("Steady-state delta values:")
for name, (old, new) in [
    ('k*', (kstar1, kstar2)), ('y*', (ystar1, ystar2)), ('c*', (cstar1, cstar2))
]:
    pct = 100 * (new - old) / old
    print(f"%delta {name} = {pct:.2f}%")



# create pdf with all 11 plots
fig, axes = plt.subplots(nrows=4, ncols=3, figsize=(12, 12))
axes = axes.flatten()

plot_list = [
    (tt, eco_base["k_tilde"], eco_shock["k_tilde"], r'$\tilde{k}$ (Capital per efficiency unit)'),
    (tt, eco_base["y_tilde"], eco_shock["y_tilde"], r'$\tilde{y}$ (Output per efficiency unit)'),
    (tt, eco_base["c_tilde"], eco_shock["c_tilde"], r'$\tilde{c}$ (Consumption per efficiency unit)'),
    (tt, eco_base["k"], eco_shock["k"], r'$k_t$ (Capital per worker)'),
    (tt, eco_base["y"], eco_shock["y"], r'$y_t$ (Output per worker)'),
    (tt, eco_base["c"], eco_shock["c"], r'$c_t$ (Consumption per worker)'),
    (tt_g, eco_base["growth_y"], eco_shock["growth_y"], r'$g^{y}$ (Year-to-year output growth)'),
    (tt, eco_base["ln_y"], eco_shock["ln_y"], r'$\ln(y)$ (Log output per worker)'),
    (tt, eco_base["ln_c"], eco_shock["ln_c"], r'$\ln(c)$ (Log consumption per worker)'),
    (tt, eco_base["k_over_y"], eco_shock["k_over_y"], r'$k/y$ (Capital-output ratio per worker)'),
    (tt, eco_base["A"], eco_shock["A"], r'$A_t$ (Technology, normalized)'),

    (None, None, None, None)
]


for ax, (x, base, shock, title) in zip(axes, plot_list):
    if base is None:
        ax.axis('off')
        continue

    ax.plot(x, base, '-', label='Baseline', linewidth=1.5)
    ax.plot(x, shock, '--', label='Shock', linewidth=1.5)
    ax.axvline(shock_year, color='k', linestyle='--', linewidth=1)
    ax.set_title(title, fontsize=10)
    ax.legend(fontsize=8)

plt.tight_layout()

fig.savefig('../plots/no_solow_simulation.pdf', format='pdf')
