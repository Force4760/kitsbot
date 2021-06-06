#html list of kits
def subtt(lists):
    i = 0
    output = []
    for kit in lists:
        i += 1
        output.append(f"""
***{i} - {str(kit[0]).replace("*"," ")}***
- {kit[1][:-5]}
- By: **{str(kit[2]).replace("*"," ")}**
- Score: {kit[3]}
- Download: {kit[4]}
""")
    return output