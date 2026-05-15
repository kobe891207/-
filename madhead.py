import random
import numpy as np
import math

def exp(p, pity): #計算抽大獎的期望抽數
    e = 0

    if pity is not None:
        for i in range(1, pity):
            e = e + i*p*pow(1-p, i-1)
            
        e = e + pity*1*pow(1-p, pity-1)
        return e
    else:
        e = 1/p
        return e
    
def PDF(p, exp): #計算機率密度函數
    pdf = 0

    for i in range(math.ceil(exp)):
        pdf = pdf + p*pow(1-p, i-1)

    return 1 - pdf

def simulate_one_player(p = 0.01, pity = 35):
    """
    模擬一位玩家抽到目標卡需要幾抽
    p: 每抽中目標卡的機率
    pity: 保底抽數，若沒有保底可設為 None
    """
    count = 0

    while True:
        count += 1

        # 如果有保底，抽到 pity 次就直接中
        if pity is not None and count == pity:
            return count

        # 隨機抽卡
        if random.random() < p:
            return count


def monte_carlo_simulation(num_players = 1000000, p = 0.01, pity = 35): #進行1000000次蒙地卡羅模擬
    results = []

    for _ in range(num_players):
        draws = simulate_one_player(p, pity)
        results.append(draws)

    return np.array(results)

#A合作卡匣:中獎機率1%，無保底，無大獎加倍
exp_A = exp(0.01, None)
pdf_A = PDF(0.01, exp_A)
results_A = monte_carlo_simulation(p = 0.01, pity = None)

print("合作卡匣:中獎機率1%，無保底")
print("計算期望抽數:", exp_A)
print("計算抽數超過期望值比例:", pdf_A)
print("模擬平均抽數:", results_A.mean())
print("中位數:", np.median(results_A))
print("90% 玩家抽數:", np.percentile(results_A, 90))
print("模擬超過期望值比例:", (np.sum(results_A > results_A.mean()))/1000000)
print("玩家平均石頭花費:", exp_A*5, '\n')

#B合作卡匣:中獎機率1%，35抽保底，無大獎加倍
exp_B = exp(0.01, 35)
pdf_B = PDF(0.01, exp_B)
results_B = monte_carlo_simulation(p = 0.01, pity = 35)

print("合作卡匣:中獎機率1%，35抽保底")
print("計算期望抽數:", exp_B)
print("計算抽數超過期望值比例:", pdf_B)
print("模擬平均抽數:", results_B.mean())
print("中位數:", np.median(results_B))
print("90% 玩家抽數:", np.percentile(results_B, 90))
print("模擬超過期望值比例:", (np.sum(results_B > results_B.mean()))/1000000)
print("玩家平均石頭花費:", exp_B*5, '\n')

#C合作卡匣:中獎機率2.5%，35抽保底，有大獎加倍
exp_C = exp(0.025, 35)
pdf_C = PDF(0.025, exp_C)
results_C = monte_carlo_simulation(p = 0.025, pity = 35)

print("合作卡匣:中獎機率2.5%，35抽保底")
print("計算期望抽數:", exp_C)
print("計算抽數超過期望值比例:", pdf_C)
print("模擬平均抽數:", results_C.mean())
print("中位數:", np.median(results_C))
print("90% 玩家抽數:", np.percentile(results_C, 90))
print("模擬超過期望值比例:", (np.sum(results_C > results_C.mean()))/1000000)
print("玩家平均石頭花費:", exp_C*5, '\n')

#D黑金卡匣:中獎機率0.8%，無保底
exp_D = exp(0.008, None)
pdf_D = PDF(0.008, exp_D)
results_D = monte_carlo_simulation(p = 0.008, pity = None)

print("黑金卡匣:中獎機率0.8%，無保底")
print("計算期望抽數:", exp_D)
print("計算抽數超過期望值比例:", pdf_D)
print("模擬平均抽數:", results_D.mean())
print("中位數:", np.median(results_D))
print("90% 玩家抽數:", np.percentile(results_D, 90))
print("模擬超過期望值比例:", (np.sum(results_D > results_D.mean()))/1000000)
print("玩家平均石頭花費:", exp_D*5, '\n')

#E黑金卡匣:中獎機率0.8%，40抽保底
exp_E = exp(0.008, 40)
pdf_E = PDF(0.008, exp_E)
results_E = monte_carlo_simulation(p = 0.008, pity = 40)

print("黑金卡匣:中獎機率0.8%，40抽保底")
print("計算期望抽數:", exp_E)
print("計算抽數超過期望值比例:", pdf_E)
print("模擬平均抽數:", results_E.mean())
print("中位數:", np.median(results_E))
print("90% 玩家抽數:", np.percentile(results_E, 90))
print("模擬超過期望值比例:", (np.sum(results_E > results_E.mean()))/1000000)
print("玩家平均石頭花費:", exp_E*5)
