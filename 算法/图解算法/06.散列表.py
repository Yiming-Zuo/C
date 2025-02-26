# 1
# 散列表、哈希表、字典、映射、关联函数：
# 使用散列函数来确定散列表中元素(key)的存储位置(索引)
# 散列函数:将不同的输入(key)均匀地映射到散列表中的不同的索引
# 散列表:
# 数组:存储value，key通过散列函数来确定key在数组中的索引
# 链表:如果两个key被映射到了数组中的同一个位置(冲突)，就在这个位置存储一个链表

# 散列表 O(1) key --散列函数--> 索引 --散列表(数组+链表)--> value
# 数组 
# O(n) key --简单查找--> value
# O(logn) key --二分查找--> value


# 2
# 防止重复
voted = {}
def check_voter(name):
	if voted.get(name) == True:
		print("爬！")
		return
	voted[name] = True
	print("投票成功！")

check_voter("tom")
check_voter("tom")


# 3
# 缓存原理：将缓存的数据存储在散列表中，当用户请求时服务器不用处理生成，而是直接发送缓存中的数据
# 缓存页面：将URL映射到页面数据

# web服务区缓存数据，以免服务器重复处理生成页面
cache = {}
def get_page(url):
	if cache.get(url):
		return cache[url]  # 如果缓存中有请求的数据，直接返回
	data = get_data_from_server(url)  # 服务器处理请求，生成数据
	cache[url] = data  # 缓存记录此次请求的数据
	return data
	
# 4 散列表与数组、链表的对比
#                 查找   插入  删除
# 散列表(平均情况)  O(1)  O(1)  O(1)
# 散列表(最糟情况)  O(n)  O(n)  O(n)
# 数组            O(1)  O(n)  O(n)
# 链表            O(n)  O(1)  O(1)  


# 5
# 冲突:散列函数给两个key分配的位置相同-->在此位置存储一个链表
# 避免冲突
# 1.低填装因子=元素数/位置数:度量散列表中有多少位置是空的
#   填装因子>0.7 --> 调整散列表的长度(添加位置)
#   1.1 创建新数组，长度加一倍
#   1.2 使用散列函数将所有元素插入到新散列表中
# 2.好散列函数:均匀的映射，让数组中的值均匀分布
# 例:将每个字符映射到一个素数:a=2,b=3,c=5...，对于字符串，将每个字符对应的素数相加除以散列表长度，取余。