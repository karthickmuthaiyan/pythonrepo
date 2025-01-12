def f_alpha_case_counter(v_sentence):
    v_upper=0
    v_lower=0
    for i in v_sentence:
        if i.isupper():
            v_upper+=1
        elif i.islower():
            v_lower+=1
    return v_upper, v_lower

if __name__ == '__main__':
    v_sentence=input('Enter a sentence: ')
    print(v_sentence)
    uppr,lwr=f_alpha_case_counter(v_sentence)
    print("UPPERCASE :",uppr,"\nLOWERCASE :", lwr)
    