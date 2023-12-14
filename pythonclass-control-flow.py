is_divisible_num = 2001
if (is_divisible_num % 4)==0:
    if(is_divisible_num % 100)==0:
        if(is_divisible_num% 400)==0:
            print("leap year")
        else:
           print("not leap")
    else:
       print("leap")
else:
   print("not leap")