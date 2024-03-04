for i in range(3, 11):

    with open("template.py") as f:


        d = f.read()


    d = d.replace("day2", f"day{i}")

    with open(f"day{i}.py", "w") as f:

        f.write(d)


    with open(f"day{i}.txt", "w") as f:

        pass
