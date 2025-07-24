from betterterminal import ProgressBar
import time

bar = ProgressBar(total=100, prefix='Progresso', suffix='Concluído', length=40)

for i in range(101):
    bar.update(i)
    time.sleep(0.02)
