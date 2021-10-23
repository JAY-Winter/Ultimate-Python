<h1> PROBLEM & SOLVE </h1>

1. 문제 정렬이 string 이어서 "10", "1", "2", "3," ..., "9" 식으로 정렬
-> natsort.natsorted() 를 이용해서 해결
-> natsort Library

2. insertPageBrake 후 새로 생긴 페이지에 insertInlineImage 가 들어가야 하는데 기존 index 다음 위치로 삽입
-> endOfSegmentLocation 을 지우고
-> insertPageBrake - location : index_location 으로 수정해서 해결