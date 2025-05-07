# Economics: Macro for Computer Science  
## A Country Comparison of Norway, Finland and Sweden

## Solow Growth Model Simulations

This repository contains Python implementations of the **general Solow growth model** for Norway, Finland and Sweden, calibrated with data from the Penn World Table (v10.0).

---

## Repository Structure

```
.
├── data                            # Raw Penn World data
│   └── ...
├── plots                           # Output figures
│   └── ...
└── scripts                         # Country‐specific Solow model scripts
    └── ...
 
```

* **`data/`**

  * **`pwt100.xlsx`**: the full Penn World Table Excel.
  * **`solow_timeseries_sweden.csv`**: cleaned Sweden GDP, capital, population series used by the Sweden script.

* **`plots/`**

  * Output figures for Norway and Sweden (Finland is shown in the script).

* **`scripts/`**

  * Each `*_solow_model.py` implements Tasks a) – g) for each country:

    1. Calibration of the model parameters from PWT
    2. Steady‐state computation
    3. 100‐period simulation with a policy shock at t=20
    4. Plotting figures

---

## Contributors

* **Max** – Norway 
* **Lynn** – Sweden 
* **Theo** – Finland

---
