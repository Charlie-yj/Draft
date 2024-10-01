def read(text)
    ridename, restrictions = text.split(":") 
# 'ridename'과 'cmmin, cmmax에 설정할 키 제한'을 각각 리스트로 만들어주는 과정. ','에 의해':'을 기점으로 '이름'을 ridename에, '키 제한'을 restrictions에 리스트의 형태로 지정해 준다.
# ridename = ['와일드 윙'] restrictions = ['110cm 이상']
# ridename = ['톰 오브 호러'], restrictions = ['-']
# ridename = ['플라잉 체어'], restrictions = ['140cm ~ 195cm']

    ridename = ridename.strip()
    restrictions = restrictions.strip()

    cmmin = cmmax = None
# 여기서 cmmin, cmmax에 초기값 설정 해줘야하는 이유: 예시 중 상한값 또는 하한값이 있다면 그 경우에 맞게 표시되도록 설정해주면 되지만, 상한값 또는 하한값이 없는 경우 자동으로 None으로 표시되어야하기 때문.


    if "~" in restrictions:
        parts = restrictions.split("~") # parts = ['140cm ', ' 195cm']
        cmmin = int(parts[0].strip().replace("cm", ""))
        cmmax = int(part[1].strip().replace("cm", ""))

    elif "이상" in restrictions:
        cmmin = int(restrictions.split("cm")[0].strip())
# restrictions.split("cm"): ['110', 'cm 이상']
# 왜 resctircions[0].replace("cm 이상", "")가 안되는가?: 현재 리스트 restrictions = [110cm 이상]의 [0]은 1이기 때문(하나 하나가 다 개별적인 문자열로 있는 상태; 공백도 포함하여).
    elif "이하" in restrictions:
        cmmax = int(restrictions.split("cm")[0].strip())

    elif "이상" in restrictions and "이하" in restrictions:
        pass
# 문제에 이런 예시가 없으므로 구현하지 않음

    return ridename, cmmin, cmmax


if __name__ == "__main__":
    ridename, cmmin, cmmax = read(input())
# ridename, cmmin, cmmax를 read함수에서 반환된 값에 각각 지정
    print("이름:", ridename)
    print("하한:", cmmin)
    print("상한:", cmmax)