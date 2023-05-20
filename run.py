import time
print("Mengecek Library : ")
time.sleep(5)
import subprocess
lib1 = "Colorama"
lib2 = "pyfiglet"
lib3 = "Phonenumbers"
try:
    subprocess.check_call(["pip", "install", lib1])
    from colorama import Fore, Back, Style
    print(f"{Fore.BLUE}~ {Fore.RED}{lib1}{Fore.GREEN} Installed {Fore.RESET}")
    time.sleep(3)
except subprocess.CalledProcessError :
    print(f"{lib1} No Installed");
try:
    subprocess.check_call(["pip", "install", lib2])
    from colorama import Fore, Back, Style
    print(f"{Fore.BLUE}~ {Fore.RED}{lib2}{Fore.GREEN} Installed {Fore.RESET}")
    from pyfiglet import Figlet
    time.sleep(3)
except subprocess.CalledProcessError :
    print(f"{lib2} No Installed");
try:
    subprocess.check_call(["pip", "install", lib3])
    from colorama import Fore, Back, Style
    print(f"{Fore.BLUE}~ {Fore.RED}{lib3}{Fore.GREEN} Installed {Fore.RESET}")
    import phonenumbers
    from phonenumbers import geocoder, carrier
    time.sleep(3)
except subprocess.CalledProcessError :
    print(f"{lib3} No Installed");
custom_fig = Figlet(font='slant')
text = custom_fig.renderText('NumFo')
print(f"{Fore.BLUE}{text}{Fore.RESET}")
print(f"{Fore.BLUE} Example : +62812312323")
def get_country_from_phone_number(phone_number):
    try :
        parsed_number = phonenumbers.parse(phone_number, None)
        country = geocoder.description_for_number(parsed_number, "en")
        return country
    except phonenumbers.phonenumberutil.NumberParseException :
        return "invalid phone numbers"

def get_city_from_phone_number(phone_number):
    try :
        parsed_number = phonenumbers.parse(phone_number, None)
        country_code = phonenumbers.region_code_for_number(parsed_number)
        city = geocoder.description_for_number(parsed_number, "en")
        return city
    except phonenumbers.phonenumberutil.NumberParseException :
        return "Invalid Phone Numbers"
def get_operator_from_phone_number(phone_number):
    parsed_number = phonenumbers.parse(phone_number, None)
    if phonenumbers.is_valid_number(parsed_number):
        operator = carrier.name_for_number(parsed_number, "en")
        return operator
    else:
        return "Invalid Phone Numbers"
num = input(f"{Fore.RED}Input Phone Number : {Fore.GREEN}")
print(f"{Fore.RESET}")
country = get_country_from_phone_number(num)
city = get_city_from_phone_number(num)
operator = get_operator_from_phone_number(num)
if city == country :
    city = "-";
else :
    city = get_city_from_phone_number(num)
print(f"{Fore.BLUE}Country {Fore.RESET}: {Fore.GREEN}{country}")
print(f"{Fore.BLUE}City {Fore.RESET}: {Fore.GREEN}{city}")
print(f"{Fore.BLUE}Operator {Fore.RESET}: {Fore.GREEN}{operator}")
