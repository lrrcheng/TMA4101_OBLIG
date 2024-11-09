import numpy as np
import matplotlib.pyplot as plt


R = 100e3
C = 10e-6
V_batt = 9

t = np.linspace(0, 5, 100)
v_theoretical = V_batt * (1 - np.exp(-t / (R * C)))

t_measured = np.array([0, 1, 2, 3, 4, 5])
v_measured = np.array([0.0, 5.6, 7.8, 8.6, 8.9, 9.0])


plt.figure(figsize=(10, 6))
plt.plot(t, v_theoretical, label='Teoretisk kurve', color='blue')
plt.plot(t_measured, v_measured, 'o-', label='Målte data', color='red')
plt.xlabel('Tid (s)')
plt.ylabel('Spenning (V)')
plt.title('Spenning over kondensatoren ved lading')
plt.legend()
plt.grid()
plt.show()
