
from netlist import t_port, t_wire, t_inst, t_module
import parser

if __name__ == '__main__':
    
#
# module adder
#   (
#       input wire [3:0] a,
#       input wire [3:0] b,
#       output wire [3:0] c
#   );
#
#  XOR U0 (.Y(c[0]), .A(a[0]), .B(b[0]));
#  XOR U1 (.Y(c[1]), .A(a[1]), .B(b[1]));
#  XOR U2 (.Y(c[2]), .A(a[2]), .B(b[2]));
#  XOR U3 (.Y(c[3]), .A(a[3]), .B(b[3]));
#    
# endmodule
#

    parser = parser.parser()
    parser.read_netlist("tcon_top_pr.v")

    #parser.designs[0].print_this()
    parser.designs[0].get_wires()
    
