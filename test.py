names = ['Cls','Back','','Close',
            '7','8','9','/',
            '4','5','6','*'
            '1','2','3','-',
            '0','.','=','+']

# 创建网格中位置的列表
positions = [(i,j) for i in range(5) for j in range(4)]

# 创建表格布局
grid = QGridLayout()
self.setLayout(grid)

# 创建按钮并添加到grid中
for name,position in names,positions:
    pass