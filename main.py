from bs4 import BeautifulSoup

# 예제 HTML 코드
html_code = """
<iframe src="https://app.windly.cc/t/e/youtube.com/222691049.jpg" style="display:none;visibility:hidden"></iframe><div style="text-align:center"><video style="width: 90%;" muted controls src="https://cloud.video.taobao.com/play/u/1016719834/p/1/e/6/t/1/257391029003.mp4"></video></div><div style="text-align:center"><br/></div><div style="text-align:center"><br/></div><div style="text-align:center"><br/></div><div style="text-align:center"><br/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-3e54b7f1-d713-41ed-b663-e6a47ea0c9d9/content/"/></div><div style="text-align:center"><br/></div><div style="text-align:center"><br/></div><div style="text-align:center"><div style="text-align:center;height:1px;width:220px;min-height:1px;min-width:220px;max-height:1px;max-width:220px;margin-top:30px;margin-bottom:30px;margin-left:auto;margin-right:auto;background-color:#ddd;"></div></div><div style="text-align:center"><br/></div><div style="text-align:center"><br/></div><div style="text-align:center"><br/></div><div style="text-align:center"><br/></div><div style="text-align:center"><strong style="font-size: 2.5em">상세 페이지</strong></div><div style="text-align:center"><br/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-2187f81b-3008-4023-976d-2242bd54ed4d/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-f9a91bb7-e6bf-4d41-8555-84ec04aa3aad/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-4c71b18b-9fff-45b7-97a8-a72e3d1c9092/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-27de94c7-636a-4b8a-af29-4e066688cf90/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-f175d6eb-2ab0-41ca-b1d7-ec4130823400/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-9489ca03-314f-4617-bcd8-5bf401e37b54/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-0fc04df9-c693-4dc2-adf0-9a6c7b3e2b40/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-d793ae59-3539-4ae8-941f-f3dc4d0cf6c8/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-dcafbe00-0483-4f33-9e18-e5475418d507/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-4842f085-c9ae-4ce2-814b-521a9c4c8b96/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-5689d378-a723-4826-9812-36a0eb725b65/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-37a6ecbf-1115-495f-8b6f-5762d93337e8/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-b849dd94-b69d-4a24-864a-0a8a2d15d7d7/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-ef08c9d3-a031-45f0-b2a8-3c870cf9661b/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-073e01c7-7123-44d9-b596-bb0518cb238b/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-4d83bb43-df94-4d63-b7dd-c3032b4a3ce7/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-8bfec12d-a184-439c-ab1f-04b34f01c960/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-3dd4e731-c1a9-4dd6-be81-dd63539faa4b/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-edb772a8-7a6b-4344-bcf2-6f740b8f53c7/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-4afb2cc3-7dc6-4d6b-ba56-69a3d3ba138a/content/"/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-35008bb8-5536-473b-b921-d6d71fd6130c/content/"/></div><div style="text-align:center"><br/></div><div style="text-align:center"><br/></div><div style="text-align:center"><br/></div><div style="text-align:center"><br/></div><div style="text-align:center"><div style="text-align:center;height:1px;width:220px;min-height:1px;min-width:220px;max-height:1px;max-width:220px;margin-top:30px;margin-bottom:30px;margin-left:auto;margin-right:auto;background-color:#ddd;"></div></div><div style="text-align:center"><br/></div><div style="text-align:center"><br/></div><div style="text-align:center"><img src="https://app.windly.cc/media/d-e7bc275e-2a89-4966-9d3f-d66199919625/content/"/></div>
"""

# BeautifulSoup 객체 생성
soup = BeautifulSoup(html_code, 'lxml')

# `<html>` 태그 찾기
html_tag = soup.find('html')

# `lang="ko"` 속성 추가
html_tag.attrs['lang'] = 'ko'

for tag in soup.find_all(True):  # find_all(True)는 모든 태그를 가져옵니다.
    # 'class'와 'id' 속성 제거
    if "class" in tag.attrs:
        del tag['class']
    if "id" in tag.attrs:
        del tag['id']

    # 'style' 속성에 너비 설정 추가
    tag.attrs['style'] = 'text-align:center; width: 200px;'.strip()

# 수정된 HTML 출력
print(soup.prettify())