import os
import shutil
import pythondata_cpu_vexriscv
from litex.soc.integration.soc_core import SoCCore
from litex.soc.integration.builder import Builder
from litex_boards.platforms import digilent_arty

class CapstoneSoC(SoCCore):
    def __init__(self):
        platform = digilent_arty.Platform(variant="a7-35")
        
        SoCCore.__init__(
            self,
            platform=platform,
            clk_freq=int(100e6),
            cpu_type="vexriscv",
            cpu_reset_address=0x10000000,
            ident="CAPSTONE Edge-Health SoC",
            with_ctrl=False,
            uart_name="stub",
            with_timer=False,
            integrated_main_ram_size=0x2000,
        )

def main():
    soc = CapstoneSoC()
    
    gateware_dir = os.path.join("build", "gateware")
    builder = Builder(
        soc, 
        output_dir="build", 
        compile_software=False
    )

    builder.build(run=False)

    # Correct path resolution directly from pythondata_cpu_vexriscv
    vexriscv_src = os.path.join(
        pythondata_cpu_vexriscv.data_location, 
        "VexRiscv.v"
    )
    
    # Fallback search if layout varies
    if not os.path.exists(vexriscv_src):
        vexriscv_src = os.path.join(
            pythondata_cpu_vexriscv.data_location, 
            "verilog", 
            "VexRiscv.v"
        )

    vexriscv_dst = os.path.join(gateware_dir, "VexRiscv.v")

    if os.path.exists(vexriscv_src):
        shutil.copyfile(vexriscv_src, vexriscv_dst)
        print(f"\n[SUCCESS] Copied VexRiscv.v -> {os.path.abspath(vexriscv_dst)}")
    else:
        print(f"\n[WARNING] Still searching... Checked path: {vexriscv_src}")

if __name__ == "__main__":
    main()