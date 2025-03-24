import numpy as np

total_exp = 47 + 335 + 73 + 161 + 28 + 86

quiescent = 47.0 / total_exp
transition = 335.0 / total_exp
fhxr = 73.0 / total_exp
fim = 161.0 / total_exp
fsxr = 28.0 / total_exp
hyper = 86.0 / total_exp

total_frac = quiescent + transition + fhxr + fim + fsxr + hyper
print("Sanity check on fraction: " + str(total_frac))

# total time in ori file:
times = np.arange(1835487300.0,1843467256.0,1.0)
total_time = 1843467255.0 - 1835487255.0

t0 = 1835487300.0
component_list = [quiescent,transition,fhxr,fim,fsxr,hyper]
name_list = ["cygX3_quiescent_lc.dat","cygX3_transition_lc.dat","cygX3_FHXR_lc.dat", \
        "cygX3_FIM_lc.dat","cygX3_FSXR_lc.dat","cygX3_hypersoft_lc.dat"]

for i in range(len(component_list)):

    t_high = t0 + total_time*component_list[i]

    print()
    print("component: " + name_list[i])
    print("t_high: " + str(t_high))
    print()

    f = open(name_list[i],"w")
    f.write("IP LINLIN\n")
    for i in range(len(times)):
        if (times[i] >= t0) & (times[i] < t_high): 
            this_line = "DP %s 1.0\n" %str(times[i])
        else:
            this_line = "DP %s 0.0\n" %str(times[i])
        f.write(this_line)
    f.write("EN")
    f.close()

    t0 = t_high
