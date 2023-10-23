# author:njw
# 二元域上的Berlekamp-Massey算法

# 二元域上的多项式类
class Polynomial:
    def __init__(self, coefficients):
        self.coefficients = coefficients
        self.degree = len(coefficients) - 1

    # 二元域上的多项式的加法，做异或运算
    def __add__(self, other):
        if self.degree > other.degree:
            return Polynomial(
                [
                    self.coefficients[i] ^ other.coefficients[i]
                    for i in range(other.degree + 1)
                ]
                + self.coefficients[other.degree + 1 :]
            )
        else:
            return Polynomial(
                [
                    self.coefficients[i] ^ other.coefficients[i]
                    for i in range(self.degree + 1)
                ]
                + other.coefficients[self.degree + 1 :]
            )


# 线性综合解类（用于存储线性综合解）（二元组）
class LinearCombinationSolution:
    def __init__(self, polynomial, order):
        self.polynomial = polynomial
        self.order = order


# 二元域上的Berlekamp-Massey算法
# 输入：0-1序列(采取0-1列表表示)
def Berlekamp_Massey_algorithm(sequence):
    # 初始化
    n = 0
    # 找到第一个不等于0的位
    for i in range(len(sequence)):
        if sequence[i] == 1:
            n = i
            break

    d = [0 for i in range(n)]
    d.extend([1])

    linear_combination_solutions = []
    for i in range(n):
        linear_combination_solutions.append(
            LinearCombinationSolution(Polynomial([1]), 0)
        )

    linear_combination_solutions.append(
        LinearCombinationSolution(Polynomial([1] + [0 for i in range(n)] + [1]), n + 1)
    )

    # 迭代
    for i in range(n, len(sequence) - 1):
        # 计算新的d
        temp_d = 0
        for j in range(linear_combination_solutions[-1].polynomial.degree + 1):
            temp_d += (
                linear_combination_solutions[-1].polynomial.coefficients[j]
                * sequence[i - j + 1]
            )

        temp_d = temp_d % 2
        d.append(temp_d)
        # 如果d为0，那么线性综合解不变
        if temp_d == 0:
            linear_combination_solutions.append(linear_combination_solutions[-1])
        # 如果d不为0，那么线性综合解更新
        else:
            m = len(linear_combination_solutions) - 1
            # 寻找当前最后一个跳跃的l
            for k in range(len(linear_combination_solutions)):
                if (
                    linear_combination_solutions[m - k].order
                    < linear_combination_solutions[-1].order
                ):
                    # 更新线性综合解
                    linear_combination_solutions.append(
                        LinearCombinationSolution(
                            # 更新线性综合解的联接多项式
                            linear_combination_solutions[-1].polynomial.__add__(
                                Polynomial(
                                    [0 for l in range(i - m + k)]
                                    + linear_combination_solutions[
                                        m - k
                                    ].polynomial.coefficients
                                )
                            ),
                            # 更新线性综合解的阶
                            max(
                                linear_combination_solutions[-1].order,
                                i + 2 - linear_combination_solutions[-1].order,
                            ),
                        )
                    )
                    break
    return linear_combination_solutions[-1]
# 返回线性综合解的联接多项式和阶

# 测试
if __name__ == "__main__":
    # test1
    sequence = [0,0,1,0,1,1,0,1]
    # test211
    # sequence = [0,0,1,1,1,0,1]
    # test3 都是用之前编写的LFSR产生的序列
    # sequence = [0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1]
    # test4
    # sequence = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1]
    # test5
    # sequence = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1]
    # sequence = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,0,0,1,1,1]
    linear_combination_solution = Berlekamp_Massey_algorithm(sequence)
    print(linear_combination_solution.polynomial.coefficients)
    print(linear_combination_solution.order)
    # 结果说明：[1,1,0,1],3是指联接多项式为1+x+x^3，阶为3