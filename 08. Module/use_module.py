import my_module

selected = my_module.random_rsp()

print('가위인가요?', my_module.SCISSOR == selected)
print('바위인가요?', my_module.ROCK == selected)
print('보인가요?', my_module.PAPER == selected)
