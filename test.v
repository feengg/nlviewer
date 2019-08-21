
module xor4 (a , b , c);
input  [3:0] a ;
input  [3:0] b ;
output  [3:0] c ;


XOR U0 (.A2 ( b[0] ) , .A1 ( a[0] ) , .Y ( c[0] ) ) ;
XOR U1 (.A2 ( b[1] ) , .A1 ( a[1] ) , .Y ( c[1] ) ) ;
XOR U2 (.A2 ( b[2] ) , .A1 ( a[2] ) , .Y ( c[2] ) ) ;
XOR U3 (.A2 ( b[3] ) , .A1 ( a[3] ) , .Y ( c[3] ) ) ;
  
endmodule


module xor8 (a, b, c);
input [7:0] a ;
input [7:0] b ;
output [7:0] c ;

xor4 U0 (.a(a[3:0]), .b(b[3:0]), .c(c[3:0]));
xor4 U0 (.a(b[7:4]), .b(b[7:4]), .c(c[7:4]));

endmodule



