module shift_reg_tb;
reg reset_n_tb;
reg clk_tb;
reg data_ena_tb;
reg serial_data_tb;
wire parallel_data_tb;

shift_reg UUT (
.reset_n (reset_n_tb),
.clk (clk_tb),
.data_ena (data_ena_tb),
.serial_data (serial_data_tb),
.parallel_data (parallel_data_tb)
);
initial
begin
end


endmodule