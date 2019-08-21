
from netlist import t_port, t_wire, t_inst, t_module
import sys
import re

class parser:

    def __init__(self):
        self.file_name = ""
        self.designs = [] #multi module
        
    def read_netlist(self, file_name):
        self.file_name = file_name
        
        f = open(self.file_name, "r")
        print("Reading netlist: {} ...".format(self.file_name))
        self.nl = f.readlines()
        print("Done!")
        
        print("Compile ...")
        self.split_netlist()
        print("Done!")

    def split_netlist(self):
        m = []
        tl = len(self.nl)
        for i in range(tl):
            l = self.nl[i]
            m.append(l)
            if l.startswith('endmodule'):
                #got a complete module
                self.read_module(m)

                #print process
                #print(i, tl)
                sys.stdout.write("\r  {}% ...".format((100*i)//tl))
                sys.stdout.flush()
                
                #clean temp variable
                m = []

    def read_module(self, m):
        #remove comment lines and empty lines
        m1 = []
        for l in m:
            if re.match(r'^\s*\/\/', l) or re.match(r'^\s*\n$', l):
                pass
            else:
                m1.append(l)
        
        #divide module by ';'
        n = ''.join(m1)
        m1 = n.split(';')

        #print("len of m1: {}".format(len(m1)))
        
        for i in range(len(m1)):
            #module name
            ret = re.match(r'^module\s+(\w+)\s+', m1[i], re.S)
            if ret:
                module_name = ret.group(1)
                module_temp = t_module(module_name)
                self.designs.append(module_temp)
                continue

            #port
            found = 0
            m1_temp = re.sub(r'\n', '', m1[i], re.S)
            ret = re.match(r'^(input|output|inout)\s+\[(\d+):(\d+)\]\s+(\w+)', m1_temp, re.S)
            if ret:
                port_direction = ret.group(1)
                port_msb = ret.group(2)
                port_lsb = ret.group(3)
                port_name = ret.group(4)
                found = 1
                
            else:
                ret = re.match(r'^(input|output|inout)\s+\[(\d+)\]\s+(\w+)', m1_temp, re.S)
                if ret:
                    port_direction = ret.group(1)
                    port_msb = ret.group(2)
                    port_lsb = ret.group(2)
                    port_name = ret.group(3)
                    found = 1
                    
                else:
                    ret = re.match(r'^(input|output|inout)\s+(\w+)', m1_temp, re.S)
                    if ret:
                        port_direction = ret.group(1)
                        port_msb = '0'
                        port_lsb = '0'
                        port_name = ret.group(2)
                        found = 1

            if found == 1:
                port_msb = int(port_msb)
                port_lsb = int(port_lsb)
                
                port_temp = t_port()
                port_temp.new_port(port_name, port_direction, "wire", port_msb, port_lsb)
                module_temp.add_port(port_temp)
            
                for i in range(port_lsb, port_msb):
                    wire_temp = t_wire("{}{}".format(port_name, i))
                    wire_temp.add_conn(None, "{}[{}]".format(port_name, i))
                    module_temp.add_wire(wire_temp)

                continue

            #wire
            ret = re.match(r'^wire\s+\[(\d+):(\d+)\]\s+(\w+)', m1_temp, re.S)
            if ret:
                port_direction = "input"
                port_msb = ret.group(1)
                port_lsb = ret.group(2)
                port_name = ret.group(3)
                
                port_msb = int(port_msb)
                port_lsb = int(port_lsb)
                
                for i in range(port_lsb, port_msb):
                    wire_temp = t_wire("{}{}".format(port_name, i))
                    wire_temp.add_conn(None, "{}[{}]".format(port_name, i))
                    module_temp.add_wire(wire_temp)
                    
                continue

            #endmodule
            ret = re.match(r'^\s*endmodule', m1_temp, re.S)
            if ret:
                continue
                    
            #inst
            ret = re.match(r'^\s*(\w+)\s+(\w+)\s+\((.*)\)\s*$', m1_temp, re.S)
            if ret:
                #print(m1_temp)
                mod_name = ret.group(1)
                inst_name = ret.group(2)
                port_map_s = ret.group(3)
                
                inst_temp = t_inst(inst_name);
                inst_temp.new_inst(mod_name, inst_name);

                port_map_s = re.sub(r'\n', '', port_map_s, re.S)
                port_map_s = re.sub(r'\s', '', port_map_s, re.S)
                #print(port_map_s)
                port_map_l = port_map_s.split(',')
                for pm in port_map_l:
                    r = re.match(r'\.(\w+)\((.*)\)', pm) #.* match xx[2], xx[2:0]
                    #print(r)
                    if r:
                        inst_temp.add_port_map(r.group(1), r.group(2))
                        if module_temp.exist_wire(r.group(2)):
                            i = module_temp.find_wire(r.group(2))
                            module_temp.wires[i].add_conn(inst_name, r.group(1))
                        else:
                            wire_temp = t_wire(r.group(2))
                            wire_temp.add_conn(inst_name, r.group(1))
                            module_temp.add_wire(wire_temp)
                            

                #inst_temp.print_this()
                module_temp.add_inst(inst_temp)
            else:
                print(m1_temp)

                
if __name__ == '__main__':
    parser = parser()
    parser.read_netlist("test.v")

    #parser.designs[0].print_this()
    parser.designs[0].get_wires()
    
    
            
        
        

    
