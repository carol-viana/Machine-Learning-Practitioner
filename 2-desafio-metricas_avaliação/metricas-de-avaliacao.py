#matriz de confusão arbitrária
VP = 50
VN = 40
FP = 10
FN = 5

def sensibilidade(VP, FN):
    return VP / (VP + FN) if (VP + FN) != 0 else 0

def especificidade(VN, FP,):
    return VN / (VN + FP) if (VN + FP) != 0 else 0

def acuracia(VP, VN, FP, FN):
    return (VP + VN) / (VP + VN + FP + FN)

def precisao(VP, FP):    
    return VP / (VP + FP) if (VP + FP) != 0 else 0

def fscore(VP, FP, FN):
    sensi = sensibilidade(VP, FN)
    preci = precisao(VP, FP)    
    return (2 * preci * sensi) / (preci + sensi) if (preci + sensi) != 0 else 0



print(f"Sensibilidade: {sensibilidade(VP, FN)}")
print(f"Especificidade: {especificidade(VN, FP,)}")
print(f"Acurácia: {acuracia(VP, VN, FP, FN)}")
print(f"Precisão: {precisao(VP, FP)}")
print(f"F-score: {fscore(VP, FP, FN)}")
    
