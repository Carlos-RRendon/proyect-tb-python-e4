 // Code your design here
`include "pc_des.sv"
`include "add_des.sv"
`include "rom_des.sv"
`include "ram_des.sv"
`include "alu_des.sv"
`include "aluC_des.sv"
`include "div_des.sv"

module TOP #(parameter a1=8,	parameter qw=9 , 
             parameter f5 = 10)(clk_T, data_rd_T,input[5:0] in1, in2 ,
                                 input h2, 
                                output jjh);

//module TOP (clk_T, data_rd_T,input[5:0] in1, in2 ,
//                                input h2, 
//                                output jjh);
  
  //wire [5:0] func_cod_T;
  //wire [1:0] func_T;
  input [6:0] clk_T;
  output [31:0] data_rd_T;
  
  wire [31:0] PCResult_T;
  wire [31:0] PCNext_T; 
  wire [31:0] PC_aux_T;
  
  wire [31:0] Instruction_T;
  
  wire [4:0] address_rs_T;
  wire [4:0] address_rt_T;
  wire [4:0] address_rd_T;
  //wire [31:0] data_rd_T;
  wire [31:0] data_rs_T;
  wire [31:0] data_rt_T;
  
  wire [5:0] func_cod_T;
  wire [1:0] func_T;
  
  assign address_rs_T = Instruction_T[25:21];
  assign address_rt_T = Instruction_T[20:16];
  assign address_rd_T = Instruction_T[15:11];
  assign func_cod_T = Instruction_T[5:0];
  
  
  ADD U1(.PCResult_s(PCResult_T), .PCNext_s(PCNext_T));
  
  PC U2(.clk(clk_T), .rst(rst_T), .PCNext(PCNext_T), .PCResult(PCResult_T));
  
  div U3(.in(PCResult_T), .out(PC_aux_T));
  
  InstructionMemory U4(.clk(clk_T), .Address(PC_aux_T),
                       .Instruction(Instruction_T));
  
  mem_reg U5(.clk(clk_T), .en (1), .we(1), .address_rs(address_rs_T), 
             .address_rt(address_rt_T), .address_rd(address_rd_T), 
             .data_rd(data_rd_T), .data_rs(data_rs_T), .data_rt(data_rt_T));
  
  Alu_C U7(.func_cod(func_cod_T), .func(func_T));
  
  Alu U8(.data1(data_rs_T), .data2(data_rt_T), .func(func_T), .result(data_rd_T));

endmodule