#!/usr/bin/env python3
  
import argparse

num2digit = ['ศูนย์', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
amntdigit = ['', 'สิบ', 'ร้อย', 'พัน', 'หมื่น', 'แสน', 'ล้าน']

def spell_digit(digit, royal_society=False, is_million=False):
  result = []
  for i, num in enumerate(digit):
    result.append(num2digit[int(num)])
    result.append(amntdigit[len(digit)-i-1])
   
  if(len(digit) >= 2 ):
    if(int(digit[-1]) == 0):
      result[-2] = ''
    elif(int(digit[-1]) == 1):
      if(royal_society or int(digit[-2]) != 0):
        result[-2] = 'เอ็ด'
    
    if(int(digit[-2]) == 1):
      result[-4] = ''
    elif(int(digit[-2]) == 2):
      result[-4] = 'ยี่'

  for i in range(len(digit)):
    if(int(digit[i])== 0):
      result[i*2] = result[i*2+1] = ''

  if(is_million):
    result[-1] = 'ล้าน'

  return result


def spell_decimal(decimal):
  num2digit = ['ศูนย์', 'หนึ่ง', 'สอง', 'สาม', 'สี่', 'ห้า', 'หก', 'เจ็ด', 'แปด', 'เก้า']
  result = [num2digit[int(num)] for num in decimal]
  return result


# input: digit string, can contains , and .
# e.g. spelling_number("1000")
# e.g. spelling_number("1,234")
# e.g. spelling_number("๒,๐๐๑")
def spelling_number(string, spl_token='|', royal_society=False):

  string = string.replace(',', '')
  dot_amount = len(string.split('.'))

  digit = ""
  decimal = ""

  if(dot_amount == 2):
    digit, decimal = string.split('.')
  elif(dot_amount == 1):
    digit = string
  else:
    print("numbers should not contains more than one dot")
    return 
  
  if(not digit.isdigit() or (decimal != "" and not decimal.isdigit())):
    print('input is not numbers')
    return string
  
  result = []

  # spell digit
  start_index = max(len(digit)-6, 0)
  end_index = min(start_index+6, len(digit))
  is_million = False
  
  while(start_index >= 0):
    result = spell_digit(digit[start_index:end_index], is_million=is_million) + result
    end_index = start_index
    start_index -= 6
    is_million = True

  if(start_index > -6):
    result = spell_digit(digit[0:end_index], is_million=is_million) + result

  # spell decimal
  if(decimal != ""):
    result = result + ['จุด'] + spell_decimal(decimal)

  return spl_token.join([x for x in result if x != ''])

# input string as sentence , spl_token="" if no split
# e.g. ฉัน มี เรือ 23 ลำ.
def numbers2grapheme(string, spl_token="|"):
  if(spl_token != ""):
    result = ""
    for word in string.split(spl_token):
      if(word.replace(',', '').replace('.', '').isdigit()):
        result += spelling_number(word, spl_token=spl_token) + spl_token
      else:
        result += word + spl_token
    if(len(result) > 0 and result[-1] == spl_token):
      result = result[:-1]

  else:
    result = ""
    start_ind = -1
    end_ind = 0
    for i in range(len(string)):
      if(string[i].isdigit()):
        if(start_ind == -1):
          start_ind = i
      elif(start_ind != -1):
        if((i+1 < len(string)) and (string[i] in ['.', ',']) and (string[i+1].isdigit())):
          continue
        result = result + string[end_ind:start_ind] + spelling_number(string[start_ind:i], spl_token=spl_token)
        end_ind = i
        start_ind = -1

    if(start_ind != -1):
      result = result + string[end_ind:start_ind] + spelling_number(string[start_ind:], spl_token=spl_token)
    else:
      result += string[end_ind:]

  return result


if __name__ == '__main__':
  
  parser = argparse.ArgumentParser(description="""Convert numbers into Thai grapheme.
  Example:
    ./spelling_number.py ฉัน มี เรือ 23 ลำ.
    ./spelling_number.py มีดินสอเป็น10แท่ง
    ./spelling_number.py "10|100|1000" -s "|"
    ./spelling_number.py "555" "มีดินสอเป็น10แท่ง -s "" """, formatter_class=argparse.RawTextHelpFormatter)
  parser.add_argument('numbers', metavar='numbers', type=str, nargs='+',
                      help='sentences or words to spell')
  parser.add_argument('-s', "--spl_token", type=str, default=" ",
                      help="""split token, put blank if input has no tokenization
  e.g. -s "" , default is space""")

  args = parser.parse_args()

  for number in args.numbers:
    print(numbers2grapheme(number, spl_token=args.spl_token))