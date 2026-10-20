# CAPSTONE Edge-Health SoC

A LiteX-based System-on-Chip (SoC) project targeting the Digilent Arty A7-35 platform. The design uses a VexRiscV CPU, a small integrated RAM, and a minimal generated hardware/software build structure, making it suitable as a capstone platform for embedded or edge-health experimentation.

## Overview

This repository contains the source and generated artifacts for a custom SoC built with:

- LiteX
- LiteX-Boards
- VexRiscV CPU
- Digilent Arty A7-35 FPGA board

The main entry point is `soc/main.py`, which configures the SoC, builds the gateware, and copies the generated `VexRiscv.v` source into the project `build/gateware` directory.

## Project Structure

```text
.
├── README.md
├── .gitignore
├── soc/
│   └── main.py
└── build/
    ├── csr.csv
    ├── csr.json
    ├── gateware/
    │   ├── VexRiscv.v
    │   ├── digilent_arty.v
    │   ├── digilent_arty.tcl
    │   ├── digilent_arty.xdc
    │   ├── build_digilent_arty.bat
    │   └── ...
    └── software/
        └── include/generated/
            ├── csr.h
            ├── git.h
            ├── mem.h
            ├── soc.h
            ├── regions.ld
            ├── output_format.ld
            └── variables.mak
```

## Key Features

- SoC configuration based on `SoCCore`
- VexRiscV CPU selected as the processor
- FPGA target: Digilent Arty A7-35
- Minimal UART stub configuration
- Small onboard main RAM (`0x2000` bytes)
- Auto-generation and copying of CPU Verilog into the build directory
- Build output ready for downstream FPGA synthesis and software integration

## Requirements

Before running the build, install the following:

- Python 3.9+
- LiteX
- LiteX-Boards
- Python package for VexRiscV (`pythondata-cpu-vexriscv`)
- FPGA toolchain for the Arty board (for actual synthesis and bitstream generation)

## Build and Run

From the repository root:

```bash
python soc/main.py
```

This script:

1. Creates a `CapstoneSoC` instance
2. Builds the SoC hardware configuration
3. Locates the VexRiscV RTL source
4. Copies it into `build/gateware/VexRiscv.v`

## Notes

- `compile_software=False` is set in the build configuration, so this project focuses on gateware generation and RTL preparation.
- The system is configured with `uart_name="stub"`, `with_ctrl=False`, and `with_timer=False`, indicating a stripped-down design for a compact embedded target.
- The generated hardware and software artifacts under `build/` are expected outputs from the LiteX build process.

## License

This project does not currently declare a license in the repository. If you plan to publish or distribute it, consider adding an appropriate open-source license.

## Contributing

This is a capstone-style project and may be extended with:

- peripheral devices
- custom memory maps
- software applications
- additional FPGA board support
- debugging and validation tooling

## Summary

The repository provides a small but complete FPGA SoC starting point for embedded and edge-health applications, built around LiteX and VexRiscV on the Digilent Arty platform.
