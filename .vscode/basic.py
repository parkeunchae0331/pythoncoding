# Boolean, Numbers, String, Bytes, Lists, Tuples, Sets, Dictionaries ...
a="string"
b=True
c=10
d= 10.1
dic= {
    "name":"kim",
    "age":10
}
llist=[3,4,5]
ttuple=4,5,6
sset={4,5,6}
print(type(sset))

# +,-,*,/,//,%,**.....
# > >= < <= == != +=.....

# 형변환 int,float,complex,str.....
print(int(d))

# math 함수
import math
print(math.ceil(5.1))
print(math.floor(3.456))

#문자열
str1="hello"
str2="python"
str3=\
"""ha
ha
ha"""

print(len(str1))
print(str1+"\t"+str2)
print(str3)

print('h' in str1)
print('h' not in str1)

# 문자열함수...

str10="nice"
print(str10.islower())
print(str10.lower())
print(str10.isupper())

print(str10[0:2])
print(str10[1:3])

# Boolean, Numbers, String, Bytes, Lists, Tuples, Sets, Dictionaries ...
a="string"
b=True
c=10
d= 10.1
dic= {
    "name":"kim",
    "age":10
}
llist=[3,4,5]
ttuple=4,5,6
sset={4,5,6}
print(type(sset))

# +,-,*,/,//,%,**.....
# > >= < <= == != +=.....

# 형변환 int,float,complex,str.....
print(int(d))

# math 함수
import math
print(math.ceil(5.1))
print(math.floor(3.456))

#문자열
str1="hello"
str2="python"
str3=\
"""ha
ha
ha"""

print(len(str1))
print(str1+"\t"+str2)
print(str3)

print('h' in str1)
print('h' not in str1)

# 문자열함수...

str10="nice"
print(str10.islower())
print(str10.lower())
print(str10.isupper())
print(str10[0:2])
print(str10[1:3])

# 리스트(순서가 있고 중복허용 수정가능 삭제가능)
#   + 하면 리스트가 합쳐지고, * 하면 그 수만큼 리스트의 안에 값개수가 늘어남
# 수정은 그냥 값 넣어주면되고, 삭제는 del a[?] 하면 ?인덱스값의 정보가 사라짐.
# append() 끝부분삽입
# sort() 정렬
# reverse() 반대로정렬
# insert(2,6) 2 번인덱스에 6넣겠다.
# remove(4) 4라는숫자를찾아서지운다.
# pop() 끝에있는걸 팝  LIFO
# ?.extend(??) ?리스트에 ??리스트를 확장 합쳐짐
q=[]
w=list()
e=[1,2,3,4]
r=[10,200,'pen','banana',[2,3]]
print(r[4][1])

#튜플 (순서가있고 중복허용 수정과삭제는 안됨)
#?.index(3) 3이란정보가있는 인덱스값을 반환
#?.count(3) 3이란정보가 몇개가있는지를 반환
qt=()
wt=(1,)
et=(1,2,3,4)
rt=(10,(20,30,40))
print(rt[1][2])

#딕셔너리 순서가없고 중복이안되며 수정과삭제는 가능함
# key,value 로 나뉨 json과비슷함->//몽고디비
# 키는 중복이안되는데 밸류는 중복이 되도됌.
# ?.get(키) 해서 키를 찾는게좋음(없어도 오류가 뜨지않는다)
# ?['address']='seoul' 하면 a의 딕셔너리 값이 추가가된다.
# key는키 ,values는벨류,   items 두개다
ad={'name':'park',
'phone':'010-6289-0144'}
#다 넣을수있음 근데 반환시키려면 나중에 print(list(sd.keys()) 형변환해서 바구니에 넣고 그 바구니를 슬라이싱해서 프린트해주면됨.
sd={'list':[1,2,3,4,5]}



#집합 순서없고중복도안됨 print 해도 공통요소는 하나만나옴. 추가제거 가능.
# 튜플로 변환하거나 리스트로 변환해서 프린트시킴.
#  qs.intersection(ws) 교집합 &
# qs.union(ws) 합집합 |
# qs.difference(ws) 빼라 -
# ?.add(지울값)   
# ?.remove(지울값)
qs=set()
ws=set([2,3,4,5,6])

#if문
if True:
    print("hello")

elif False:
    print("no")

else:
    print("nonono")



#반복문 for
v1=1
while v1<11:
    print(v1)
    v1+=1
#v2 는자동으로 0부터시작
for v2 in range(10):
    print(v2)

for v3 in range(4,7):
    print(v3)

#순서가있는(문자열,리스트,튜플,집합,사전)자료형 반복가능
#iterable리턴함수:range,reversed,enumerate,filter,map,zip

names=['one','two','three']
for vvv in names:
    print(vvv)

my_info={
    'name':'eunchae',
    'phone':'010-6289-0144'
}
#기본값은 키
for a in my_info:
    print(a)
#키
for key in my_info.values():
    print(key)
#벨류
for key in my_info.keys():
    print(key)
#아이템
for k,v in my_info.items():
    print(k,v)
    break
else: 
    print("브레이크문을 만나지못한 포문은 이 구문이 실행된다. 즉 모든반복문이 다 정상적으로 수행된경우 엘스가 실행된다.")


# 컨티뉴를 만나면 밑에애를 무시하고 다음  v 로 넘어가게된다.
lt=["1",2,3,4.5,True]
for v in lt:
    if type(v) is float:
        continue
    print("타입:",type(v))


#함수정의
#def 함수명(parameter)

def hello(world):
    print("hello",world)

hello("inbok")

#리턴
def hello_return(world):
    val="hello"+str(world)
    return val

hr=hello_return("gg")
print(hr)

#다중리턴
def return_mul(world):
    y1=world*100
    y2=world*200
    y3=world*300
    return y1,y2,y3

b1,b2,b3=return_mul(10)
print(b1,b2,b3)

def return_mul(world):
    y1=world*100
    y2=world*200
    y3=world*300
    return (y1,y2,y3) #어떤형태로든 리턴시킬수있음.


# *args(매개변수의갯수를 모를때(받는매개변수가없을때도있는겨), 
# 다양한거 받아서 함수의 흐름을 바꿀수있음.튜플로넘어옴.), *kwargs//
#  **별이 두개면 딕셔너리형태로 받겠다는뜻 *한개는튜플
def args_func(*args):
    print(args)

args_func('kim')

args_func('kim','park')

def kwargs_func(**kwargs):
    for k,v in kwargs.items():
        print(kwargs)

kwargs_func(name1='kim',name2="park")

#혼합
def example_mul(arg1,arg2,*args,**kwargs):
    print(arg1,arg2,args,kwargs)

example_mul(10,20)
example_mul(10,20,'park','kim',age1=25,age2=54)


#중첩함수(클로저) 메모리관리를 편하게 할수있음. 데코레이터../
def nested_func(num):
    def func_in(num):
        print(num)
    print("in func")
    func_in(num+10000)

nested_func(100)

#100이 첫번째함수로 넘어가서 들어가고, 두번째함수는 들어갔지만 아직 선언이 안되고 실행은안됐음. 
# 그래서 인 펑션먼저 출력하고 인자로 넘어간애가 2번째함수를 실행시켜서 10100이 실행이된다.


#원하는데이터타입를 적어둘수있음. 예외는 반환하진않지만, 가독성이 높아진다.
def return_mul(world:int)-> list:
    y1=world*100
    y2=world*200
    y3=world*300
    return [y1,y2,y3]


# 람다식 // 메모리절약 , 가독성 향상 , 코드간결 너무많이써면 가독성이 떨어지느 상황이 발생.
# 함수는 객체생성 -> 리소스(메모리)할당
# 람다는 즉시실행 (heap초기화) -> 메모리초기화

#일반적함수 -> 변수할당



lam_mul=lambda x: x*10 

print(lam_mul(20))


def final (x,y,func):
    print(x*y*func(10))

final(10,10,lam_mul)


#클래스 pass예약어해두면 에러가안뜬다.
#속성/메소드 둘로 이루어짐.
class Hi:
    pass

class UserInfo:
    #클래스를 초기화를 해줘야함.
    def __init__(self,name):
        self.name=name
    def user_info(self):
        print("Name:",self.name)

#2개해줘야함.(클래스+함수1개)

#인스턴스생성
user1=UserInfo("kim")
#인스턴스사용
user1.user_info()

#주소값?클래스마다 뽑아내도 주소값이 다 독립적이다.(다르다고)
print(id(user1))
print(user1.__dict__)


#클래스와 인스턴스랑 차이가 있다. 클래스는 몸 인스턴스화는 옷을 장착!
#네임스페이스 : 객체를 인스턴스화할때 저장된 공간
#클래스변수 : 직접사용가능, 객체보다먼저생성
#인스턴스변수 : 객체마다별도로존재, 인스턴스 생성후사용

#self 이해
class SelfTest:
    h=1
    #얘는 함수로 호출해야함.
    def function1():
        print("1")
      
    #얜인스턴스화해서 써야함 무조건 셀프들어감.
    def function2(self):
        print("2")
    
haha=SelfTest()
#함수로
SelfTest.function1()
#인스턴스로
haha.function2()



#상속
#슈퍼클래스(부모), 서브클래스(자식) -> 모든속성/메소드 사용가능

class Car:
    """Parent Class"""
    def __init__(self,tp,color):
        self.type=tp
        self.color=color
    
    def show(self):
        return 'car class "show method"'

class BmwCar(Car):
    """Sub Class"""
    def __init__(self,car_name,tp,color):
        super().__init__(tp,color)
        self.car_name=car_name

    def show_model(self)->None:
        return "you car name: %s" %self.car_name 

class BenzCar(Car):
    """Sub Class"""
    def __init__(self,car_name,tp,color):
        super().__init__(tp,color)
        self.car_name=car_name

    def show_model(self)->None:
        return "you car name: %s" %self.car_name 

    # 부모와같은이름의함수 오버라이딩가능
    def show(self):
        #근데 부모애있는 글을같이 쓰고싶으면써주면됨
        print(super().show())

        return 'car class " method"'

#사용방법
model1=BmwCar('520d','sedan','red')

print(model1.color) #super
print(model1.car_name) #sub
print(model1.show()) #super
print(model1.show_model()) #sub
print(model1.__dict__)

#overriding  부모상속받은애를 함수를변경가능. 덮어씌움
model2=BenzCar("220d","sedan","red")
print(model2.show())

#상속정보 //뭘상속받았는지알수있다.
#다중상속도 가능. ()오브젝트안에 부모클래스를 넣어주면된다.
print(BmwCar.mro())

#모듈? - 폴더 안 파일하나하나(식기)
#패키지? - 파일하나하나를 뭉쳐논것 구조적으로관리하는것.폴더 (부엌)
#모듈 불러오기? 
# (클래스사용)from 패키지이름.패키지안에파일이름 import 파일안의클래스이름 //그럼 그 클래스안의 함수 쓸수있음.
# (함수사용)from 패키지이름.패키지안의파일이름 import 사용할함수이름//하면 함수사용가능.
# 근데 파일안의모듈이름이 너무 길면 as a 해서 짧게 쓸수있음.
#상대경로 .. -> 부모디렉토리로 .->현재디렉토리


#파일 읽기,쓰기
#읽기모드 : r, 쓰기모드(기존파일삭제):w ,추가모드(파일생성 또는 추가):a

#파일읽기
# f=open('./폴더/파일이름.txt','r')
# content=f.read()
# print(content)
# f.close()

#같지만 더 편한 파일읽기
# with open('./폴더/파일이름.txt','r') as f:
#     c=f.read()
#     print(c)

#한번읽어오면 커서가 밑으로 내려가므로, 불렀던내용을 다시 불러올순없다.

#한문장씩 읽어오기
# with open('./폴더/파일이름.txt','r') as f:
#     line=f.readline()
#     while line:
#          print(line,end='gg')
#          line=f.readline()


#응용 5 3 5 1 3  6자리고, 소수3째자리까지 나와라.
# score=[]
# with open(~~~) as f:
#     for line in f:
#         score.append(int(line))
#     print(score)
# print("평균은 {6:3}".format(sum(score)/len(score)))

#파일로 쓰기?
#with open(~~~,'w') as f:
#   f.write("~~~")


#예외처리하기
