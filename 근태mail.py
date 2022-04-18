'''
근태 변경 메일 자동으로 보내는 코드
gmail로 로그인해서 보내는 방법으로 22년 5월 31일부터 google 로그인을 계정, 비밀번호만으로 할 수 없게 되어 이후에는 불가능하다.
References : https://red-mail.readthedocs.io/en/latest/
'''

from redmail import gmail
import pandas as pd
from datetime import datetime

user = '홍길동'            # 보내는 사람
team = '사업1팀'           #팀
director = '길동'         #담당자

month = datetime.today().month
day = datetime.today().day
time_list = ['1. 08:30', '2. 09:00', '3. 09:30']
time_select = int(input(f'{time_list}\n출근할 시간의 번호를 입력하세요 : '))
time_list = ['08:30', '09:00', '09:30']

df = pd.DataFrame({
    '이름': [user],
    '적용일': [f'2022.0{month}.{day}'],
    '출근시간': [time_list[time_select - 1]]
},
    index=['']
)

gmail.username = 'abcd@gmail.co.kr'          #gmail계정
gmail.password = 'password'                  #비밀번호

gmail.send(
    subject=f'{month}월 {day}일자 근태 변경 관련 메일입니다.',
    sender='abcd@gmail.io',                  #발신메일주소
    receivers=['asdf@gmail.io'],           #송신메일주소
    html='''
        <p>안녕하세요 {{director}}님, {{team}}팀 {{user}}입니다.<br><br>

        {{month}}월 {{day}}일자 근태에 변경이 생겨 메일 보내드립니다.<br><br>

        </p>  {{mytable}}<br>
        <p>감사합니다.<br>
        {{user}} 올림
        </p>
        ''',

    body_tables={'mytable': df},
    body_params={
        'user' : user,
        'team' : team,
        'director' : director,
        'month': month,
        'day': day
    }
)
