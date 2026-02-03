"""
ASK Modulation Visualization
Generates binary input, carrier, and ASK output signals
Saves plots as PNG and SVG formats
"""
import numpy as np
import matplotlib.pyplot as plt
import os

# Parameters
binary_seq = [1, 0, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1]
fc = 5  # Low carrier frequency for clear visualization (Hz)
T_bit = 1.0  # Duration of one bit in seconds
fs = 1000    # Sampling frequency
t_per_bit = np.linspace(0, T_bit, int(fs * T_bit), endpoint=False)
A = 1.0      # Amplitude for '1'

# Generate time axis and signals
t = []
carrier = []
ask_signal = []

for i, bit in enumerate(binary_seq):
    t_bit = t_per_bit + i * T_bit
    carrier_bit = np.cos(2 * np.pi * fc * t_bit)
    ask_bit = A * carrier_bit if bit == 1 else np.zeros_like(t_bit)
    
    t.extend(t_bit)
    carrier.extend(carrier_bit)
    ask_signal.extend(ask_bit)

t = np.array(t)
carrier = np.array(carrier)
ask_signal = np.array(ask_signal)

# Create figure with three subplots
fig, axes = plt.subplots(3, 1, figsize=(14, 8), sharex=True)

# 1. Binary input sequence
axes[0].step(range(len(binary_seq)), binary_seq, where='post', linewidth=2, color='black')
axes[0].set_ylim(-0.2, 1.5)
axes[0].set_yticks([0, 1])
axes[0].set_ylabel('Binary Input', fontsize=12)
axes[0].grid(True, alpha=0.3)
axes[0].set_title(f'ASK Modulation', fontsize=14, fontweight='bold')

# Add binary values on top
for i, bit in enumerate(binary_seq):
    axes[0].text(i + 0.5, 1.2, str(bit), ha='center', fontsize=10, fontweight='bold')

# 2. Carrier signal
axes[1].plot(t, carrier, 'blue', linewidth=1.2)
axes[1].set_ylabel('Carrier Signal', fontsize=12)
axes[1].grid(True, alpha=0.3)
axes[1].set_xlim(0, min(5 * T_bit, t[-1]))  # Show first 5 bits for clarity

# 3. ASK output signal
axes[2].plot(t, ask_signal, 'red', linewidth=1.5)
axes[2].set_ylabel('ASK Output', fontsize=12)
axes[2].set_xlabel('Time (seconds)', fontsize=12)
axes[2].grid(True, alpha=0.3)
axes[2].set_xlim(0, t[-1])

# Mark bit boundaries
for i in range(len(binary_seq) + 1):
    axes[2].axvline(x=i * T_bit, color='gray', linestyle='--', alpha=0.5, linewidth=0.8)
    axes[1].axvline(x=i * T_bit, color='gray', linestyle='--', alpha=0.3, linewidth=0.5)

plt.tight_layout()
plt.subplots_adjust(hspace=0.1)

# Save the plots
output_dir = "ask_output"
os.makedirs(output_dir, exist_ok=True)

# Save as PNG
png_path = os.path.join(output_dir, "ask_modulation.png")
plt.savefig(png_path, dpi=300, bbox_inches='tight')
print(f"Graph saved as PNG: {png_path}")

# Save as SVG
svg_path = os.path.join(output_dir, "ask_modulation.svg")
plt.savefig(svg_path, bbox_inches='tight')
print(f"Graph saved as SVG: {svg_path}")

plt.show()

# Print summary
print(f"\nGraph Parameters:")
print(f"Binary sequence: {binary_seq}")
print(f"Carrier frequency: {fc} Hz")
print(f"Bit duration: {T_bit} seconds")
print(f"Total time: {len(binary_seq) * T_bit} seconds")
print(f"Files saved in directory: '{output_dir}/'")
