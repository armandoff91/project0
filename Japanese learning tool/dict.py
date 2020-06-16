dict = {}
hira = dict

dict['a'] = 'あ'
dict['i'] = 'い'
dict['u'] = 'う'
dict['e'] = 'え'
dict['o'] = 'お'

dict['ka'] = 'か'
dict['ki'] = 'き'
dict['ku'] = 'く'
dict['ke'] = 'け'
dict['ko'] = 'こ'

dict['sa'] = 'さ'
dict['shi'] = 'し'
dict['su'] = 'す'
dict['se'] = 'せ'
dict['so'] = 'そ'

dict['ta'] = 'た'
dict['chi'] = 'ち'
dict['tsu'] = 'つ'
dict['te'] = 'て'
dict['to'] = 'と'

dict['na'] = 'な'
dict['ni'] = 'に'
dict['nu'] = 'ぬ'
dict['ne'] = 'ね'
dict['no'] = 'の'

dict['ha'] = 'は'
dict['hi'] = 'ひ'
dict['fu'] = 'ふ'
dict['he'] = 'へ'
dict['ho'] = 'ほ'

dict['ma'] = 'ま'
dict['mi'] = 'み'
dict['mu'] = 'む'
dict['me'] = 'め'
dict['mo'] = 'も'
# save it to text

def translate2(string, dict):
    length = len(string)
    index = 0
    output = ''
    while index < length:
        if string[index:index+1] in dict:
            output = output + dict[string[index:index+1]]
            index = index + 1
        elif string[index:index+2] in dict:
            output = output + dict[string[index:index+2]]
            index = index + 2
        elif string[index:index+3] in dict:
            output = output + dict[string[index:index+3]]
            index = index + 3
        else:
            output = output + string[index:index+1]
            index = index + 1
    return output
