#atm services

class Atm:
    total=10000
    mobile_no =1234567890
    account_no=12345678901

    def __init__(self,name):
        pass
    @classmethod
    def withdrawal(cls):
        print('Please enter your account \n 1.current \n 2. saving')
        m = input()
        amount = (input('enter the amount in multiple of 500:'))
        if amount[-3:] == '000' or amount[-3:] == '500' and int(amount) <= cls.total:
            balance = cls.total - int(amount)
            print('Please wait for the Cash....!')
            display = input('do you want to display your balance yes or No ? : ')
            if display == 'yes':
                print('your balance amount is :', balance)
                print('Thank you using SBI ATM service,Please Visit again')
            else:
                print('Thank you using SBI ATM service ,Please Visit again')
        elif amount[-3:] == '000' or amount[-3:] == '500' and int(amount) > cls.total:
            print('insufficient balance,please check your balance  ')
        else:
            print('Please enter the amount in multiple of 500,try again')
    @classmethod
    def balance_check(cls):
        print('Account Balanace ', cls.total)
        print('Thank you using SBI ATM service,Please Visit again')

    @classmethod
    def deposite(cls):
        mob_number = int(input('Enter your 10 digits mobile number : '))
        acc_no = int(input('enter your eleven digits acc nos :'))
        if mob_number == cls.mobile_no and cls.account_no == acc_no:
            deposit = int(input('enter the amount to be deposite:'))
            dep_balance = deposit + cls.total
            print('wait for the transaction to be complete...!')
            print('Your Transaction copleted successfully \n your account balance is ', dep_balance)

    def other_banking_service(self):
        print('we provide banking services soon ,thank you visit agian')


if __name__ == '__main__':
    print('Welcome to State Bank of india...!')
    s = int(input("please enter number between 1 to 25 : "))
    count=0
    x=1212
    if s <= 25:
        while(True):
            n = int(input("Please Enter Your PIN : "))
            count = count + 1
            if n == x:
                print('Welcome to State Bank of india')
                print('SBI SERVICES')
                print('-------------------------------------')
                print(
                    '1.Withdrawal \n 2.Balance Check \n 3.Net banking \n 4.Deposit \n 5.Other Banking related services')
                choice = int(input('Please enter your choice :'))
                if choice == 1:
                    print('Please enter your account \n 1.saving  2.Current')
                    m = input()
                    amount = (input('enter the amount in multiple of 500:'))
                    if amount[-3:] == '000' or amount[-3:] == '500' and int(amount) <= total:
                        balance = total - int(amount)
                        print('Please wait for the Cash....!')
                        time.sleep(3)
                        display = input('do you want to display your balance yes or No ? : ')
                        time.sleep(2)
                        if display == 'yes':
                            print('your balance amount is :', balance)
                            print('Thank you using SBI ATM service,Please Visit again')
                            break
                        else:
                            print('Thank you using SBI ATM service ,Please Visit again')
                            break
                    elif amount[-3:] == '000' or amount[-3:] == '500' and int(amount) > total:
                        print('insufficient balance,please check your balance  ')
                        break
                    else:
                        print('Please enter the amount in multiple of 500,try again')
                        break
                elif choice == 2:
                    print('Customer Name', name)
                    print('Account Balanace ', total)
                    print('Thank you using SBI ATM service,Please Visit again')
                    break
                elif choice == 3:
                    print('we provide net banking service soon')
                    break
                elif choice == 4:
                    mob_number = int(input('Enter your 10 digits mobile number : '))
                    time.sleep(2)
                    acc_no = int(input('enter your eleven digits acc nos :'))
                    time.sleep(2)
                    if mob_number == mobile_no and account_no == acc_no:
                        deposit = int(input('enter the amount to be deposite:'))
                        dep_balance = deposit + total
                        print('wait for the transaction to be complete...!')
                        time.sleep(5)
                        print('Your Transaction copleted successfully \n your account balance is ', dep_balance)
                        break
                elif choice == 5:
                    print('we provide all services soon Thank you ,visit again')
                    break
            elif n != x and count < 10:
                print("your entered Wrong pin ,please try again")
                attempt = attempt - 1
                print("you have ", attempt, " attempt remaining")
            elif n != x and count == 10:
                print('Your limit over,please try again after some times')
                break

    else:
        print('You entered wrong number')
