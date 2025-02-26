# 贪婪算法：每步都选择局部最优解，最终得到全局最优解

# NP完全问题：没有快速算法，使用近似算法快速找到近似解
# 旅行商问题和集合覆盖问题：需要计算所有的解，并从中选出最小/最短的那个
# 1.元素少时算法运行速度很多，越多越慢
# 2.涉及或者可以转换为所有组合、序列、集合的问题通常是NP完全问题
# 3.不能将问题分解成小问题，需要考虑所有可能的情况

# 精确算法:O(2^n)
# 贪婪算法:O(n^2)

states_needed = {"mt", "wa", "or", "id", "nv", "ut", "ca", "az"}
stations = {"kone" : {"id", "nv", "ut"}, 
	"ktwo" : {"wa", "id", "mt"}, 
	"kthree" : {"or", "nv", "ca"}, 
	"kfour" : {"nv", "ut"}, 
	"kfive" : {"ca", "az"}}
final_stations = set()

while states_needed:
	best_station = None
	states_covered = set()
	for key, value in stations.items():
		covered = value & states_needed
		if len(covered) > len(states_covered):
			best_station = key
			states_covered = covered
	states_needed -= states_covered
	final_stations.add(best_station)
	
print(final_stations)