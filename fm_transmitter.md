# FM Transmitter Block Diagram

```mermaid
graph TD
    A[Message Signal m(t)] --> B[Pre-emphasis & LPF]
    B --> C[Amplifier]
    C --> D[VCO]
    E[Crystal Oscillator] --> F[Frequency Multiplier]
    F --> G[Carrier fc]
    G --> D
    D --> H[Power Amplifier]
    H --> I[Band-pass Filter]
    I --> J[FM Output s(t)]
    
    D -.->|Feedback| K[PLL]
    K -.->|Control Voltage| D

    style A fill:#e1f5fe
    style D fill:#f3e5f5
    style G fill:#e8f5e8
    style J fill:#fff3e0
