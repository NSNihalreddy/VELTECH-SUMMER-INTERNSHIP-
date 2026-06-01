birthyear=int(input("enter birth year:"))
if birthyear>2026:
    print("invalid year")
else:
    age=2026-birthyear
    print(f'present age {age}')
    print(f'age in 10 years: {age+10}')

