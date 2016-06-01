# 아래의 내용은 아 파일이 import 될 때는 실행되지 않음
if "__main__" == __name__:
    # Cash Card User 모듈의 msg_int 함수를 사용할 수 있게 함
    from CashCard_user import chk_bal
    # myCard 객체를 생성한다
    #   SimpleCashCard 클래스에 정한 대로 만든다
    #   simpleCashCard __init__() 메소드가 호출된다
    myCard = CashCard()
    # mySafeCard 객체를 생성한다
    #   SafeCashCard 클래스에 정한 대로 만든다
    #   SafeCashCard __ㅑㅜㅑㅅ__() apthemfmf ghcnfgkfurh gkwlaks
    #   SafeCashCard 클래스 안에는 정의되자 않았기 때문에
    #   상위 클래스인 SimpleCashCard __init__() 메소드가 호출된다
    mySafeCard