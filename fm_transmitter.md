# FM Transmitter Block Diagram

```mermaid
graph TD
    A["Message Signal m(t)"] --> B[Pre-emphasis Circuit]
    B --> C[Low-pass Filter]
    C --> D[Amplifier / Driver]
    D --> E[Voltage-Controlled Oscillator VCO]
    F[Crystal Oscillator] --> G[Frequency Multiplier]
    G --> H["Carrier Frequency fc"]
    H --> E
    E --> I[Buffer Amplifier]
    I --> J[Power Amplifier]
    J --> K[Band-pass Filter]
    K --> L["FM Signal Output s(t)"]
    
    M[Phase-Locked Loop PLL] -.->|Optional for stability| E
    N[Frequency Feedback] -.->|From E to M| M

    style A fill:#e1f5fe
    style E fill:#f3e5f5
    style H fill:#e8f5e8
    style L fill:#fff3e0
