import ollama

text = """
연남동에서 최근 용산으로 이전한 파스타바 입니다. 한동안 파스타바가 유행이었잖아요. 눈앞에서 생면 뽑아다가 삶아 슥슥 비벼주는게 보는재미 먹는재미 더해져 저도 몇군데 찾아다녔었죠. 사실 요즘은 대부분 예약제에 예약하기도 쉽지 않아서 더 자주 못가게 되는 경향이 있는데..이곳 비아톨레도 파스타바는 제가 방문해봤던 파스타바 중 가장 정통 이탈리안 스타일을 추구하는 업장이라 소개해드릴 수 있을것 같습니다.
코스로 예약을 했는데요, 웰컴 디쉬부터 네종류의 개성 넘치는 파스타, 직접 구워낸 빵과 디저트들까지 즐거운 시간을 가졌습니다. 음식 간이 전반적으로 좀 있는 편이라 싱겁게 드시는 분들께는 짜게, 보통인 분들껜 조금 짭짤하게 느껴지실 수도 있어요. 저는 짜게먹는 사람이라 그런지 딱 맞아서 좋았고요. 이날의 최고 메뉴는 굴 파스타였습니다ㅎㅎ
바 형태의 매장이다보니 조리과정을 구경하는 것도 재밌지만 쉐프님과 이런저런 얘기 나누는게 특히 좋았네요. 최근 집에서 파스타 만들면서 잘 안되는 부분들도 딱 해결해주시고..감사합니다.
참, 주류가 필수인 매장이라 이점은 참고하셔야 합니다. 와인 종류도 많은데 보틀 주문이 부담스러우신 분들은 글라스로 주문도 가능하니 예약 시 문의하시면 될것같아요.
덧붙여 이 동네는 처음 가봤는데 주택가 골목 사이사이에 세련된 카페와 식당들이 콕콕 숨어있네요. 일찍 도착해서 한바퀴 둘러봤는데 구경하는 재미가 있더라고요. 순식간에 또 힙한 동네가 되는게 아닐까? 아니면 이미 되었는데 나만 모르고있었던게 아닐까? 싶었습니다.
"""

response=ollama.chat(
    model="mistral",
    messages=[
        {
            "role":"user",
            "content":f"이 텍스트 50자 이내로 요약해줘: {text}"
        }
    ] 
)

print(response["message"]["content"])