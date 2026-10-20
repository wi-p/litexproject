"""
from amaranth import *
from amaranth.sim import Simulator
from amaranth.back import rtlil, verilog
import amaranth_playground


en = Signal()
count = Signal(4)
m = Module()
with m.If(en):
    m.d.sync += count.eq(count + 1)
m.d.comb += en.eq(count < 5)


async def testbench(ctx):
    for _ in range(10):
        await ctx.tick()
        print(f"count: {ctx.get(count)}")

sim = Simulator(m)
sim.add_clock(1e-6)
sim.add_testbench(testbench)
with amaranth_playground.show_waveforms(sim):
    sim.run()

amaranth_playground.show_verilog(verilog.convert(m, ports=[count]))
# amaranth_playground.show_rtlil(rtlil.convert(m, ports=[count]))
"""

from amaranth import *

class TestModule(Elaboratable): # module where the circuit goes in
    def __init__(self): # where we define the resources used by the circuit
        self.count  = Signal(16, reset = 0) # sinal de 16 bits e comeca em 0
        self.ncount = Signal(16, reset = 0)

    def elaborate(self, platform):# where we define the logic
        m = Module()
        
        m.d.comb += self.ncount.eq(~self.count)
        m.d.sync += self.count.eq(self.count + 1) # add 1 to the value

        with m.If(self.count == 42):# verify if count is 42, if yes, set it to 0
            m.d.sync += self.count.eq(0)

        return m

