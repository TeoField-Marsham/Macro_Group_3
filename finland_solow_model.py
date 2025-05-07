import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load data
df = pd.read_excel("pwt100.xlsx", sheet_name="Data")
finland = df[df['country'] == 'Finland']
years = (finland['year'] >= 1999) & (finland['year'] <= 2019) # Use averages between 1999–2019 for key variables
data = finland.loc[years].sort_values("year").reset_index(drop=True).copy()

# Parameters
alpha = 1 - data['labsh'].mean()  # Capital share of income = 1 - labor share
n = data['pop'].pct_change().mean() # Average population growth rate
delta = data['delta'].mean()  # Average depreciation rate of capital
g = (data['rgdpna']/data['pop']).pct_change().mean() # Average output per capita growth rate
s = data['csh_i'].mean() # Average investment share of GDP
s_new = s + 0.05   # Raised investment rate permanent from period 20 onward

# Calculate the steady state values
def steady_state(alpha, s, n, g, delta):
    k_star = (s / (n + g + delta + n * g)) ** (1 / (1 - alpha))
    y_star = k_star ** alpha               # y_star = k^α
    c_star = (1 - s) * y_star
    return k_star, y_star, c_star

# Calculate the baseline steady state using pre-shock values
k_ss0, y_ss0, c_ss0 = steady_state(alpha, s, n, g, delta)

# Initial conditons for the model
N0 = data.iloc[0]["pop"] # Population in 1999
A0 = 1 # Inital technology level set to 1
K0 = k_ss0 * A0 * N0 # Initial aggregate capital 
T = 100  # Time periods
shock_t = 20 # Time when the shock occurs

# Table with all periods (rows) and variables (columns)
out = pd.DataFrame(index=range(T+1),
                   columns=['K','A','N','Y','C','k','y','c',
                            'ln_y','ln_c','g_y'])

out.loc[0,'K'] = K0 # Set initial capital
out.loc[0,'A'] = A0 # Set inital technology
out.loc[0,'N'] = N0 # Set inital population

# Function to get investment share for any t
def investment_share(t):
    return s_new if t >= shock_t else s

# Model simulation
for t in range(T):
    # Current investment share for a period
    s_t = investment_share(t)
    
    K_t, A_t, N_t = out.loc[t, ['K','A','N']]
    k_t = K_t / (A_t * N_t)                # k = K / (A·N)
    y_t = k_t ** alpha
    Y_t = y_t * A_t * N_t                  
    C_t = (1 - s_t) * Y_t
    
    # Record current per‑capita/effective‑worker values
    out.loc[t, ['k','y','c','Y','C']] = [k_t,y_t,c_t:=y_t*(1-s_t),Y_t,C_t]
    out.loc[t, ['ln_y','ln_c']] = np.log([y_t,c_t])

    # Evolve stocks
    K_next = (1 - delta) * K_t + s_t * Y_t
    A_next = A_t * (1 + g)
    N_next = N_t * (1 + n)
    
    out.loc[t+1, ['K','A','N']] = [K_next, A_next, N_next]

# Growth rate of output per worker
out['g_y'] = out['ln_y'].diff()
out['ky'] = out['k'] / out['y']

# Calculate the baseline steady state using post-shock values
k_ss1, y_ss1, c_ss1 = steady_state(alpha, s_new, n, g, delta)

# Print various data and parameters
print("\nSteady state per worker before shock:")
print(f"  k* = {k_ss0:.4f},   y* = {y_ss0:.4f},   c* = {c_ss0:.4f}")
print("Steady state per worker after shock:")
print(f"  k* = {k_ss1:.4f},   y* = {y_ss1:.4f},   c* = {c_ss1:.4f}")
print("Change in steady state per worker:")
print(f"  Δk*: {(k_ss1 - k_ss0) / k_ss0 * 100:.1f}%")
print(f"  Δy*: {(y_ss1 - y_ss0) / y_ss0 * 100:.1f}%")
print(f"  Δc*: {(c_ss1 - c_ss0) / c_ss0 * 100:.1f}%\n")

print("\nParameters for Finland (1999-2019):")
print(f"  Capital share (alpha): {alpha:.4f}")
print(f"  Population growth rate (n): {n:.4f}")
print(f"  Output per capita growth rate (g): {g:.4f}")
print(f"  Depreciation rate (delta): {delta:.4f}")
print(f"  Investment rate (s): {s:.4f}")
print(f"  Investment rate (s_new) after shock: {s_new:.4f}\n")

# Create plots
fig, ax = plt.subplots(3, 3, figsize=(12,10), sharex=True)

ax[0,0].plot(out.index, out['k']);       
ax[0,0].set_title("kₜ (capital / eff. worker)")

ax[0,1].plot(out.index, out['y']);       
ax[0,1].set_title("yₜ (output / eff. worker)")

ax[0,2].plot(out.index, out['c']);       
ax[0,2].set_title("cₜ (consumption / eff. worker)")

ax[1,0].plot(out.index, out['ln_y']);    
ax[1,0].set_title("ln(yₜ)")

ax[1,1].plot(out.index, out['g_y']);     
ax[1,1].set_title("gʸₜ")

ax[1,2].plot(out.index, out['ln_c']); 
ax[1,2].set_title("ln(cₜ)")

ax[2,1].plot(out.index, out['ky']); 
ax[2,1].set_title("kₜ / yₜ (capital-output ratio)")

ax[2,0].set_visible(False)
ax[2,2].set_visible(False)

# Styling for plots
for a in ax.flatten(): 
    a.axvline(shock_t, c='red', ls='--', lw=1)
    a.tick_params(axis='x', labelbottom=True)
    a.set_xlabel('t (periods)')
    a.margins(x=0)

plt.tight_layout(); 
plt.show()