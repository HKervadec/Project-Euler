# teste la primarite du nombre passe en parametre
def prime(n):
    if n == 2:
        return True
        
    if n < 2 or not n % 2:
        return False
        
    lim = n ** 0.5
    i = 3
    while i <= lim:
        if not n % i:
            return False
            
        i += 2
        
    return True
    
    
# Supprime les doublons de la liste passee en parametre
def uniq(list):
    list.sort()
    
    size = len(list)
    i = 0
    while i < size - 1:
        if list[i] == list[i+1]:
            del list[i]
            size -= 1
            continue
            
        i += 1
        
    return list
    
    
# transforme un entier en liste contenant tout ses chiffres
def toList(n):
    # result = []
    
    # while n > 0:
        # result.append(n%10)
        # n //= 10
        
    # result.reverse()
    
    # return result
    result = []
    string = str(n)
    for c in string:
        result.append(int(c))
    
    return result