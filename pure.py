
###################################################################
#      Greatest Common Divisor                                    #
###################################################################

def gcd(ainput,binput):
    a = min([ainput,binput])
    b = max([ainput,binput])
    rem = a % b
    while rem > 0:
        a = b
        b = rem
        rem = a % b
    return b

###################################################################
#      Euclidean Algorithm                                        #
###################################################################

def euclid_algorithm(ainput,binput):

    count = 0
    a = max([ainput,binput])
    b = min([ainput,binput])
    rem = a % b
    mult = [a//b]
    forward = [str(a) + ' = ' + str(mult[count]) + '*' 
             + str(b) + ' + ' + str(rem)]

# Working algorithm forwards

    while rem > 0:
        a = b
        b = rem
        count = count + 1
        rem = a % b
        mult.append(a//b)
        forward.append(str(a) + ' = ' + str(mult[count]) + '*'
                     + str(b) + ' + ' + str(rem))

# Working the algorithm backwards

    l1 = -mult[count - 1]
    l2 = 1
    if count > 1:
        l3 = -mult[count - 2]
        l4 = 1
        for i in range(count-3,-1,-1):
            l1_new = l1*l3 + l2
            l2_new = l1*l4
            l1 = l1_new
            l2 = l2_new
            l3 = -mult[i]
            l4 = 1

        l1_new = l1*l3 + l2
        l2_new = l1*l4
        l1 = l1_new
        l2 = l2_new

# preparing output

    gcd = b
    min_mult = l1
    max_mult = l2
    backward = str(min_mult) + '*' + str(min([ainput,binput])) + ' + ' + \
               str(max_mult) + '*' + str(max([ainput,binput])) 
    
    output = {'gcd': gcd, 'min_mult': min_mult, 'max_mult': max_mult, 'forward': forward, 'backward': backward}    
    
    return output

###################################################################
#      Prime Factorisation                                        #
###################################################################

def prime_fact(minput):
    read = True 
    m = minput
    prime_file = open("primes/primes_1mill.txt",'r')
    prime_file = list(map(int,prime_file.readline().split()))
    primes = []
    powers = []
    nxt = 0
    while m != 1:
        if read:
            pc = int(prime_file[nxt])
            nxt+=1
            count = 0
        rem = m % pc
        if rem == 0:
            read = False
            count = count + 1
            m = m/pc
        else:
            read = True
            if count > 0:
                primes.append(pc)
                powers.append(count)
    if count > 0:
        primes.append(pc)
        powers.append(count)
    return [primes, powers]

###################################################################
#      phi function                                               #
###################################################################

def phi(minput):
    [primes,powers] = primeFact(minput)
    phi = 1
    for i in range(0,len(primes)):
        phi = phi*(primes[i] - 1)*primes[i]**(powers[i] - 1)
    return phi

###################################################################
#      set cross product                                          #
###################################################################

def set_cross_prod(sets):
    num_sets = len(sets)
    num_elements = 1

    for st in sets:
        num_elements *= len(st)

    elements = []
    for i in range(0,num_elements):
        divisor = num_elements
        element = []
        index = i
        for j in range(0,num_sets-1):
            divisor = divisor/len(sets[j])
            lindex = int(index//divisor)              
            index = int(index%divisor)              
            element.append(sets[j][lindex])
        j = j + 1
        element.append(sets[j][index])
        elements.append(element)

    return elements


                    
