//-------------------------------
// Example: Shift Register
//
//-------------------------------

module shift_reg (
  input reset_n,
  input clk,
  input data_ena,
  input serial_data,
  output logic [1:0] parallel_data);
  
  always @ (posedge clk, negedge reset_n)
    if(!reset_n)
      parallel_data <= ’0;
  else if (data_ena)
    parallel_data <= {serial_data, parallel_data[width-1:1]};

endmodule
//--------------------------------