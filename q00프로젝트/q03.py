time=3725
hours=time//3600
minutes=(time%3600)//60
seconds=time%60
print(f"{hours}시간 {minutes}분{seconds}초")