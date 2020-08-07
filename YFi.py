from alpha_vantage.sectorperformance import SectorPerformances
import matplotlib.pyplot as plt

sp = SectorPerformances(key='85IAAJZVJLIKZZ26', output_format='pandas')
data, meta_data = sp.get_sector()
data['Rank A: Real-Time Performance'].plot(kind='bar')
plt.title('Crecimiento por sectores en tiempo Real')
plt.tight_layout()
plt.show()
