class Score:
    scores = []
    def __init__(self, name, kor, eng, math):
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math

    def getName(self):
        return self.name

    def getKor(self):
        return self.kor

    def getEng(self):
        return self.eng

    def getMath(self):
        return self.math

    @staticmethod
    def inputData():
        while True:
            print('\n\n1. 입력')
            name = input('이름 :')
            kor = input('국어 :')
            eng = input('영어 :')
            mat = input('수학 :')
            Score.scores.append(Score(name, kor, eng, mat))

            flag = input('계속 입력하시겠습니까(y/n)?')
            if flag == 'n':
                break

    @staticmethod
    def printData():
        print('\n\n-------------------------------------')
        print('이름', '국어', '영어', '수학', sep='\t\t')
        print('-' * 30)

        for score in Score.scores:
            print(f'{score.getName():8}{score.getKor():8}{score.getEng():8}{score.getMath():8}')

        print('-' * 30)



while True:
    print('\n\n메인 메뉴')
    print('\t1. 입력')
    print('\t2. 출력')
    print('\t3. 종료')

    n = int(input("번호를 입력하세요:"))

    if n == 1:
        Score.inputData()
    elif n == 2:
        Score.printData()
    elif n == 3:
        break
