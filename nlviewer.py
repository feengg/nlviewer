
from netlist import t_port, t_wire, t_inst, t_module
        
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

    module_adder = t_module("adder");
    
    port_a = t_port()
    port_a.new_port("a", "input", "wire", 3, 0)
    wire_a0 = t_wire("a0")
    wire_a0.add_conn(None, "a[0]")
    wire_a1 = t_wire("a1")
    wire_a1.add_conn(None, "a[1]")
    wire_a2 = t_wire("a2")
    wire_a2.add_conn(None, "a[2]")
    wire_a3 = t_wire("a3")
    wire_a3.add_conn(None, "a[3]")
    module_adder.add_port(port_a)
    module_adder.add_wire(wire_a0)
    module_adder.add_wire(wire_a1)
    module_adder.add_wire(wire_a2)
    module_adder.add_wire(wire_a3)
    
    port_b = t_port()
    port_b.new_port("b", "input", "wire", 3, 0)
    wire_b0 = t_wire("b0")
    wire_b0.add_conn(None, "b[0]")
    wire_b1 = t_wire("b1")
    wire_b1.add_conn(None, "b[1]")
    wire_b2 = t_wire("b2")
    wire_b2.add_conn(None, "b[2]")
    wire_b3 = t_wire("b3")
    wire_b3.add_conn(None, "b[3]")
    module_adder.add_port(port_b)
    module_adder.add_wire(wire_b0)
    module_adder.add_wire(wire_b1)
    module_adder.add_wire(wire_b2)
    module_adder.add_wire(wire_b3)
    
    port_c = t_port()
    port_c.new_port("c", "output", "wire", 3, 0)
    wire_c0 = t_wire("c0")
    wire_c0.add_conn(None, "c[0]")
    wire_c1 = t_wire("c1")
    wire_c1.add_conn(None, "c[1]")
    wire_c2 = t_wire("c2")
    wire_c2.add_conn(None, "c[2]")
    wire_c3 = t_wire("c3")
    wire_c3.add_conn(None, "c[3]")
    module_adder.add_port(port_c)
    module_adder.add_wire(wire_c0)
    module_adder.add_wire(wire_c1)
    module_adder.add_wire(wire_c2)
    module_adder.add_wire(wire_c3)
    
    inst_u0 = t_inst("U0");
    inst_u0.new_inst("XOR", "U0");
    inst_u0.add_port_maps([["Y", "c[0]"], ["A", "a[0]"], ["B", "b[0]"]])
    wire_a0.add_conn(inst_u0, "A")
    wire_b0.add_conn(inst_u0, "B")
    wire_c0.add_conn(inst_u0, "C")
    module_adder.add_inst(inst_u0)
    
    inst_u1 = t_inst("U1");
    inst_u1.new_inst("XOR", "U1");
    inst_u1.add_port_maps([["Y", "c[1]"], ["A", "a[1]"], ["B", "b[1]"]])
    wire_a1.add_conn(inst_u1, "A")
    wire_b1.add_conn(inst_u1, "B")
    wire_c1.add_conn(inst_u1, "C")
    module_adder.add_inst(inst_u1)
    
    inst_u2 = t_inst("U2");
    inst_u2.new_inst("XOR", "U2");
    inst_u2.add_port_maps([["Y", "c[2]"], ["A", "a[2]"], ["B", "b[2]"]])
    wire_a2.add_conn(inst_u2, "A")
    wire_b2.add_conn(inst_u2, "B")
    wire_c2.add_conn(inst_u2, "C")
    module_adder.add_inst(inst_u2)
    
    inst_u3 = t_inst("U3");
    inst_u3.new_inst("XOR", "U3");
    inst_u3.add_port_maps([["Y", "c[3]"], ["A", "a[3]"], ["B", "b[3]"]])
    wire_a3.add_conn(inst_u3, "A")
    wire_b3.add_conn(inst_u3, "B")
    wire_c3.add_conn(inst_u3, "C")
    module_adder.add_inst(inst_u3)                            

    #print
    module_adder.print_this()

    
