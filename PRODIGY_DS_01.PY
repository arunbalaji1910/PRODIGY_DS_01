import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style("whitegrid")
sns.set_palette("Set2")  

file_path = r"D:\Python\PRODIGY_DS_01\API_SP.POP.TOTL_DS2_en_excel_v2_85347.csv"
data = pd.read_csv(file_path, skiprows=3)

data_2023 = data[["Country Name", "2023"]].dropna()

vibgyor_colors = ["#8B00FF","#4B0082", "#0000FF", "#00FF00", "#FFFF00", "#FF7F00", "#FF0000", "#FF1493", "#00CED1","#DAA520"]  
top10 = data_2023.sort_values(by="2023", ascending=False).head(10)

fig, axes = plt.subplots(1, 2, figsize=(15, 7), facecolor='#fdf6e3') 

ax1 = axes[0]
bars = ax1.bar(top10["Country Name"], top10["2023"] / 1e6,
               color=vibgyor_colors, edgecolor='black')

for bar in bars:
    yval = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2, yval + 20,
             f'{yval:.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold', color='black')

ax1.set_facecolor('#fff0f5')
ax1.set_title(" Top 10 Populated Countries (2023)", fontsize=16, fontweight='bold', color='#6a1b9a')
ax1.set_xlabel("Country", fontsize=12, fontweight='bold', color='#4a148c')
ax1.set_ylabel("Population (Millions)", fontsize=12, fontweight='bold', color='#4a148c')
ax1.tick_params(axis='x', rotation=45)
ax1.grid(axis='y', linestyle='--', alpha=0.4)

ax2 = axes[1]
sns.histplot(data_2023["2023"] / 1e6, bins=30, kde=True, ax=ax2, color='pink')  

ax2.set_facecolor('#e8f5e9')  
ax2.set_title(" Global Population Distribution (2023)", fontsize=16, fontweight='bold', color='#2e7d32')
ax2.set_xlabel("Population (Millions)", fontsize=12, fontweight='bold', color='#1b5e20')
ax2.set_ylabel("Number of Countries", fontsize=12, fontweight='bold', color='#1b5e20')
ax2.grid(axis='y', linestyle='--', alpha=0.4)

plt.suptitle(" Prodigy Task 01 ", fontsize=18, weight='bold', color='#3e2723')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()

print("\nData Visualization Completed by Arun Balaji! ")
