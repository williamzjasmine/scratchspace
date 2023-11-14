# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19
# letters used in total.
# If all the numbers from 1 to 1,000 (one thousand) inclusive were written out in words, how many letters would be used?
# NOTE: Do not count spaces or hyphens. For example, (three hundred and forty-two) contains 23 letters.


ones_str = ['', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
teens_str = ['ten', 'eleven', 'twelve', 'thirteen', 'fourteen',
             'fifteen', 'sixteen', 'seventeen' , 'eighteen', 'nineteen']
tens_str = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

# will print all numbers 1-1000
total = 0
for hund in ones_str:
    for ten in tens_str:
        if ten == 'ten':
            for teen in teens_str:
                if hund == '':
                    print(teen)
                    total += len(teen.replace(' ', ''))
                else:
                    num_str = hund + ' hundred and ' + teen
                    print(num_str)
                    total += len(num_str.replace(' ', ''))
            continue
        for one in ones_str:
            if hund == '':
                num_str = ten + " " + one
                print(num_str)
                total += len(num_str.replace(' ', ''))
            else:
                if one == '' and ten == '':
                    num_str = hund + ' hundred'
                    print(num_str)
                    total += len(num_str.replace(' ', ''))
                else:
                    num_str = hund + ' hundred and ' + ten + "" + one
                    print(num_str)
                    total += len(num_str.replace(' ', ''))

# have to add 11 for the final "one thousand"
print(f'Number of letters in all numbers 1-1000: {total+ 11}')
