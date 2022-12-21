
def readfile(file_bok):
    with open(file_bok, "r", encoding="utf_8") as s:
        return list(map(lambda x: x.replace('\n', ''), s.readlines()))


def addcontactstr(file_bok, contact):
    with open(file_bok, "a", encoding="utf_8") as faleap:
        faleap.write(", ".join(contact)+"\n")


def addcontactlist(file_bok, contact):
    with open(file_bok, "a", encoding="utf_8") as faleap:
        faleap.write(str("\n".join(contact)+'\n\n'))
