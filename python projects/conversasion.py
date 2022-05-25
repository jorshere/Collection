def statement(phase):
    interrogates=("how","when","where","why","what")
    if phase.startswith(interrogates):
        return f"{phase.capitalize()}? "
    else:
        return f"{phase.capitalize()}. "
final=[]
while True:
    stats = input("say somthing: ")
    if stats == "\end":
        break
    else:
        final.append(statement(stats))
print("".join(final))
