# author:njw
# import pdb
from pylfsr import LFSR

# 19级LFSR
# state1 = [0 for i in range(19)]
# state1[0] = 1
# fpoly1 = [19, 18, 17, 14]
# # pdb.set_trace()
# L1 = LFSR(fpoly=fpoly1, initstate=state1)
#
# # Generate K-bits
# k1 = 38
# seq_k1 = L1.runKCycle(k1)
#
# print("38 bits")
# print(L1.arr2str(seq_k1))
# print("")

# # Generate bits of one full period.
# # Expected period of LFSR = 2^M-1, for M-bit LFSR).
# # seq_full1  = L1.runFullPeriod()
# #
# # print(L1.arr2str(seq_full1))
#
# # Vizualise LFSR.
# L1.Viz()
# 22级LFSR
# state2 = [0 for i in range(22)]
# state2[0] = 1
# fpoly2 = [22,21]
# L2 = LFSR(fpoly=fpoly2,initstate =state2)
#
#
#
# k1=44
# seq_k1  = L2.runKCycle(k1)
#
# print('44 bits')
# print(L2.arr2str(seq_k1))
# print('')
# # Generate bits of one full period.
# # Expected period of LFSR = 2^M-1, for M-bit LFSR).
# # seq_full2  = L2.runFullPeriod()
# #
# # print(L2.arr2str(seq_full2))
#
# # Vizualise LFSR.
# L2.Viz()
#
# 23级LFSR
# state3 = [0 for i in range(23)]
# state3[0] = 1
# fpoly3 = [23,22,21,8]
# L3 = LFSR(fpoly=fpoly3,initstate =state3)
# k1=46
# seq_k1  = L3.runKCycle(k1)
#
# print('46 bits')
# print(L3.arr2str(seq_k1))
# print('')
# seq_full3  = L3.runFullPeriod()
#
# print(L3.arr2str(seq_full3))

# L3.Viz()
