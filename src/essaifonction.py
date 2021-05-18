



def verificationcode(a, essai):
    
    solution = a.copy()
    response = []

    if solution == essai:
        response = 4*["black"]

    else: 
        for i in range(4):
            if solution[i] == essai[i]:
                response.append("black")
                solution[i] = "0"
                essai[i] = "rien"



        for i in range(4):
            for n in range(4):
                 if essai[i] == solution[n]:
                    response.append("white")
                    solution[n] = "0"
                    essai[i] = "rien"
                    
    
    return response


code = ["green", "yellow", "red", "blue"]

print(code)

e = ["green", "red", "blue", "blue"]

print(e)

a = verificationcode(code, e)

print(code)
