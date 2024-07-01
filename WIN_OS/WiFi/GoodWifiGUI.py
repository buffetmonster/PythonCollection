import matplotlib.pyplot as plt

# Define dBm ranges and corresponding descriptions
dBm_ranges = [
    (-30, "Excellent"),  # Very strong signal
    (-50, "Good"),       # Good for most activities
    (-70, "Fair"),       # May experience occasional issues
    (-80, "Weak")        # Frequent connection drops likely
]

# Create the horizontal bars with a larger figure size
plt.figure(figsize=(6.5, 4.5))
bars = plt.barh(range(len(dBm_ranges)), [range[0] for range in dBm_ranges], color='skyblue')

# Add labels and title
plt.xlabel('dBm (lower is better)')
#plt.ylabel('Signal Strength')
plt.ylabel('')
plt.title('Ideal Wi-Fi Signal Strength')

# Add descriptive labels for each bar
for bar, (dBm_min, description) in zip(bars, dBm_ranges):
    plt.text(bar.get_width() + 2, bar.get_y() + bar.get_height() / 2, description, ha='left', va='center')

# Set grid and limits
plt.grid(axis='x', linestyle='--', alpha=0.6)
plt.xlim(-80, -15)  # Adjust x-axis limits for better visualization
plt.yticks(ticks=[3, 2, 1, 0], labels=[1,2,3,4]) 

# Add text box at the top
textstr = '2.4GHz (20MHz channel in range 2400 to 2500 MHz)\n Ch:1, 6, and 11\n 5GHz (20/40/80 or 160 MHz in range 5100 to 5300 MHz)\n Ch:36,40,44 (DFS Channels):100 104, 108,112 '
text_content = "2.4GHz (20MHz channel in range 2400 to 2500 MHz)\n"
text_content += "Ch: 1, 6, and 11\n"
text_content += "5GHz (20/40/80 or 160 MHz in range 5100 to 5300 MHz)\n"
text_content += "Ch: 36, 40, 44 (DFS Channels): 100, 104, 108, 112"
#plt.figtext(0.5, 0.95, textstr, wrap=True, horizontalalignment='center', fontsize=10, bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 5})
#plt.figtext(0.5, 0.05, textstr, wrap=True, horizontalalignment='center', fontsize=10, bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 5})
plt.figtext(0.1, 0.175, text_content, wrap=True, horizontalalignment='left', fontsize=10, bbox={'facecolor': 'white', 'alpha': 0.5, 'pad': 3})
# Compress the x-axis by setting the aspect ratio
#plt.gca().set_aspect(aspect=7.5)
#plt.gca().set_aspect(aspect=2.5)
# Display the plot
plt.tight_layout()
plt.show()