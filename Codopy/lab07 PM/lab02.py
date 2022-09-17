#point in square

#input
print(f'Upper left corner coordinate:')
x_axiu =  int(input(f'  << x axis: '))
y_axil =  int(input(f'  << y axis: '))
E_ast  =  int(input(f'  << Eastern: '))
S_out  =  int(input(f'  << Southern: '))
#process
x_point =   x_axiu + E_ast
y_point =   y_axil - S_out 
#rec_tangle = E_ast * S_out
print(f'Enter a coordinate:')
x_axis =  int(input(f'  << x axis: '))
y_axis =  int(input(f'  << y axis: '))
if ((x_axiu <= x_axis)and (x_axis <= x_point)) and ((y_axil >= y_axis) and (y_axis >= y_point)) :
    x = ''
else:
    x = 'not '
#output
print(f'>>> ({x_axis:.2f}, {y_axis:.2f}) is {x}inside the rectangle.')