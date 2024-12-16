# conv_ops.py
#
# Usage: python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p
# Determines output shape and operation count of a convolution layer
# Parameters:
# c_in   : input channel count
# h_in   : input height count
# w_in   : input width count
# n_filt : number of filters in the convolution layer
# h_filt : filter height count
# w_filt : filter width count
# s      : stride of convolution filters
# p      : amount of padding on each of the four input map sides
#
# Output:
# c_out : output channel count
# h_out : output height count
# w_out : output width count
# adds  : number of additions performed
# muls  : number of multiplications performed
# divs  : number of divisions performed

# Written by Anna Kosnic
#
# import Python modules
import sys # argv

# initialize script arguments
c_in    = 0
h_in    = 0
w_in    = 0
n_filt  = 0
h_filt  = 0
w_filt  = 0
s       = 0
p       = 0


# parse script arguments
if len(sys.argv)==9:
    c_in   = int(sys.argv[1])
    h_in   = int(sys.argv[2])
    w_in   = int(sys.argv[3])
    n_filt = int(sys.argv[4])
    h_filt = int(sys.argv[5])
    w_filt = float(sys.argv[6])
    s      = float(sys.argv[7])
    p      = float(sys.argv[8])
else:
    print(\
        'Usage: '\
        'python3 conv_ops.py c_in h_in w_in n_filt h_filt w_filt s p'\
            )
    exit()


# script below
c_out = n_filt
h_out = int((h_in + 2*p - h_filt)/s + 1)
w_out = int((w_in + 2*p - w_filt)/s + 1)
muls  = n_filt*h_out*w_out*c_in*h_filt*w_filt
adds  = n_filt*h_out*w_out*c_in*h_filt*w_filt
divs  = 0

print(int(c_out)) # output channel count
print(int(h_out)) # output height count
print(int(w_out)) # output width count
print(int(adds))  # number of additions performed
print(int(muls))  # number of multiplications performed
print(int(divs))  # number of divisions performed
