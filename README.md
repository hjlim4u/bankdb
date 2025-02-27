# bankdb

DB를 설계하는데 있어 필요한 몇가지 과정을 거처 은행의 계좌 입출금과 본인인증을 구현한 간단한 프로그램을 구현해보았다.

DBMS를 구현하기 위해서는 대략 4가지의 과정을 거쳐 설계의 과정을 거친다.
첫번째로 DB를 활용하여 해결하고자 하는 문제의 요구사항을 분석하는 단계, 해당 프로젝트에서는 은행의 계좌입출금, 본인인증 등 본격적인 업무를 수행하기 위해 데이터베이스가 만족해야할 최소 요건을 정하는 단계이다. 해당 단계에서는 보통 데이터베이스가 다루어야할 데이터를 정의하고 해당 데이터가 일관성있게 저장되기 위한 조건들을 명시한다.

두번째는 요구사항을 바탕으로 entity relationship model을 설계하는 단계이다. entity relationship 모델은 여러 성질(attribute)를 가진 객체에 해당하는 entity와 그 객체가 가지고 있는 성질(Attribute)간의 관계를 시각적으로 표현하는 단계이다. 

세번째 단계에서는 er model을 기반으로 relational model을 작성하는 단계이다. relational model은 각 테이블과 그 테이블의 schema를 정의하고 테이블간의 의존 및 참조 관계를 시각적으로 표현한 모델이다. 

네번째 단계는 이 relational 모델을 바탕으로 SQL문을 통해 실제 DB를 생성하고 쿼리를 수행하는 프로그램을 작성하는 단계이다.

이 네 단계 순차적으로 진행해야만 하는 것이 아니라 수정사항이 발생할 때마다 이전단계로 돌아가서 수정을 하는 방식으로 데이터베이스 설계를 수행한다.
해당 프로젝트와 관련하여 이 네가지 단계에 대한 세부적인 사항들은 wiki에 업로드 해두었다.
