zoo=('python','elephant','penguin')
print('Number of animals in the zoo is ',len(zoo))

new_zoo=('monkey','camel',zoo)
print('Number of cages in the new zoo is ',len(new_zoo))
print('All anamals in new zoo are ',new_zoo)
#new_zoo[2] 来指定 new_zoo 中的第三个项目
print('Animals brought from old zoo are ',new_zoo[2])
#定 new_zoo[2][2] 来指定new_zoo 元组中的第三个项目中的第三个项目
print('Last animal brought from old zoo is ',new_zoo[2][2])
print('Number of animals in the new zoo is',len(new_zoo)-1+len(new_zoo[2]))
