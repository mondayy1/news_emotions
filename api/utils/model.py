import openai
from api.utils.secrets import api_key

client = openai.OpenAI(
    # This is the default and can be omitted
    api_key=api_key
)

def get_posnegs_gpt(titles):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": (
                    "너는 뉴스 제목을 분석하는 보조자야. 사용자가 요청한 뉴스의 제목들을 분석해 감정(긍정적/부정적)을 도출해."
                    "결과는 반드시 **줄을 띄워서** 제공해야 하며, 절대 다른 문장을 추가하지 마."
                )
            },
            {
                "role": "user", 
                "content": (
                    f"이 뉴스 제목들을 보고 긍정적/부정적인 뉴스 제목 각각 5개, 총 10개를 선정하고, 결과는 줄을 띄워서 작성해."
                    f"'{titles}'"
                )
            }
        ]
    )

    gpt_answer = chat_completion.choices[0].message.content
    text = gpt_answer.split('\n')
    positives = [item[3:] for item in text[1:6]]
    negatives = [item[3:] for item in text[8:13]]

    return positives, negatives

def get_summary_gpt(titles):
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", 
                "content": (
                    "너는 뉴스 분석을 도와주는 보조자야. 사용자가 요청한 뉴스의 제목들을 분석해 한줄평을 작성해줘."
                    "절대 한 문장을 넘어가선 안돼."
                )
            },
            {
                "role": "user", 
                "content": (
                    f"이 뉴스 제목들을 보고 너의 의결을 작성해줘."
                    f"'{titles}'"
                )
            }
        ]
    )

    gpt_answer = chat_completion.choices[0].message.content

    return gpt_answer