module TOP_tb;
reg [5:0] in1_tb;
reg [5:0] in2_tb;
reg h2_tb;
reg f9_tb;
reg jk_tb;
reg j99_tb;
reg clk_tb;
reg reset_tb;
reg [31:0] bus_A_tb;
reg [6:0] clk_T_tb;
reg [15:0] module_Bus_B_tb;
wire wrr_898_tb;
wire jjh_tb;
wire [63:0] d877_tb;
wire [31:0] data_rd_T_tb;
wire f459_87__tb;

TOP UUT (
.in1 (in1_tb),
.in2 (in2_tb),
.h2 (h2_tb),
.f9 (f9_tb),
.jk (jk_tb),
.j99 (j99_tb),
.clk (clk_tb),
.reset (reset_tb),
.bus_A (bus_A_tb),
.clk_T (clk_T_tb),
.module_Bus_B (module_Bus_B_tb),
.wrr_898 (wrr_898_tb),
.jjh (jjh_tb),
.d877 (d877_tb),
.data_rd_T (data_rd_T_tb),
.f459_87_ (f459_87__tb)
);

initial

  begin 

    $dumpfile("TOP_tb.vcd");
    $dumpvars(0,"TOP_tb");

    clk_tb=0;
    reset_tb=0;

    #1
    in1_tb = 6'd1;
    in2_tb = 6'd41;
    h2_tb = 1'd0;
    f9_tb = 1'd1;
    jk_tb = 1'd0;
    j99_tb = 1'd1;
    bus_A_tb = 32'd363495322;
    clk_T_tb = 7'd71;
    module_Bus_B_tb = 16'd53392;

    $finish

  end

  always
  begin
  #1  clk_tb = ~clk_tb
  end

endmodule