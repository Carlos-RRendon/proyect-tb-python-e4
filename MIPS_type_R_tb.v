`timescale 1ns/1ps
module Top_Module_tb;
reg clk_tb;
reg rst_tb;
wire [31:0] out_G_tb;

Top_Module UUT (
.clk (clk_tb),
.rst (rst_tb),
.out_G (out_G_tb)
);
initial
begin
end


endmodule