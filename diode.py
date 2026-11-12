import numpy as np
import matplotlib.pyplot as plt
def diode_current(voltage, Is=1e-12, n=1):
    """
    ダイオードの電流-電圧特性を計算する関数
    :param voltage: 電圧 (V)
    :param Is: 飽和電流 (A)
    :param n: 理想係数
    :return: 電流 (A)
    """
    Vt = 0.02585  # 熱電圧 (V) at room temperature
    current = Is * (np.exp(voltage / (n * Vt)) - 1)
    return current
# 電圧範囲の設定
voltages = np.linspace(-0.2, 0.7, 100)
currents = diode_current(voltages)
# グラフの描画
plt.figure(figsize=(8, 6))
plt.plot(voltages, currents, label='Diode I-V Characteristic')
plt.xlabel('Voltage (V)')
plt.ylabel('Current (A)')
plt.title('Diode I-V Characteristic Curve')
plt.grid()
plt.show()