from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

client = OpenAI(api_key=openai_api_key)

assistant = client.beta.assistants.create(
  name="Seoul Photo Guide",
  instructions="""\
    You are a guide recommending photography themes for people who want to take pictures and explore in Seoul.\
    Considering the user's input, suggest appropriate photography keywords and explain the reason.\
    The photography keywords should be separated from the other content with '@', and provided in a structured list format.\
    The recommended keywords must be included in the following list:\
    ['거리&골목길', '건축물', '공원', '궁궐', '광화문&종로', '다리', '산', '서촌&북촌', '식물', '역사 문화 공간', '자연산책로', '캠퍼스', '야경&전망', '테마파크', '한강']\
    """,
  model="gpt-4o",
)

example_conversations = [
    {
    'input':'난 역사적인 장소와 고대 건축물을 촬영하는 것을 좋아해',
    'output':'역사적인 장소와 고대 건축물을 촬영하는 것을 좋아하신다면, 서울에는 많은 매력적인 장소들이 있습니다. 한국의 풍부한 역사와 문화를 반영하는 웅장한 궁궐과 역사적 공간을 탐험해 보세요.@["궁궐", "역사 문화 공간"]'
    },
    {
    'input':'도시 풍경을 촬영하고 싶은데 서울의 매력을 느낄 수 있게 전통적인 건축물이 어우러진 곳이면 좋겠어',
    'output':'도시 풍경을 촬영하는 것을 좋아하신다면, 광화문과 종로 지역을 추천드립니다. 이곳은 서울의 현대적인 모습과 전통적인 건축물이 어우러져 다양한 사진을 찍기 좋은 곳입니다.@["광화문&종로", "건축물"]'
    },
    {
    'input':'자연과 식물 사진을 찍고싶은데 좋은 장소 있을까?',
    'output':'자연과 식물을 촬영하고 싶으시다면, 서울의 여러 공원을 추천드립니다. 특히 다양한 식물을 감상할 수 있는 공원에서 멋진 사진을 찍을 수 있을 것입니다@["공원", "식물"]'
    },
    {
    'input':'골목길과 작은 거리를 탐험하며 사진을 찍는 것을 좋아해. 서울에 그런 곳이 있을까?',
    'output':'골목길과 작은 거리를 탐험하며 사진을 찍는 것을 좋아하신다면, 서촌과 북촌 지역을 추천드립니다. 이곳은 전통 한옥과 현대 건축물이 어우러져 독특한 분위기를 자아냅니다.@["서촌&북촌","거리&골목길"]'
    },
    {
    'input':'한강에서 사진을 찍고 싶은데, 어떤걸 찍는 게 좋을까?',
    'output':'한강에서 사진을 찍고 싶으시다면, 한강변의 다채로운 풍경을 주제로 삼아보세요. 일몰이나 야경을 배경으로 한강의 아름다움을 담아보세요.@["한강","야경&전망"]'
    },
    {
    'input':'서울의 예쁘고 멋진 다리를 찍고싶어',
    'output':'서울에는 아름다운 다리들이 많이 있습니다. 여러 다리들은 각기 다른 매력을 가지고 있어, 멋진 사진을 찍기 좋은 장소입니다.@["다리"]'
    },
    {
    'input':'높은 곳에서 풍경 사진을 찍고 싶어',
    'output':'높은 곳에서 풍경 사진을 찍고 싶으시다면, 서울에는 멋진 전망을 감상할 수 있는 장소들이 많이 있습니다. 특히 서울의 아름다운 전경을 한눈에 담을 수 있는 곳에서 멋진 사진을 찍어보세요.@["산","야경&전망"]'
    },
    {
    'input':'사람들이 북적이는 곳에 가고 싶어',
    'output':'캠퍼스와 테마파크는 사람들이 북적이는 곳을 원하는 당신에게 훌륭한 선택입니다. 캠퍼스는 다양한 행사와 활동으로 항상 활기차며, 테마파크는 놀이기구와 공연으로 많은 사람들이 모여 북적이는 장소입니다.@["캠퍼스","테마파크"]'
    },
]

def get_example_conversations():
    return example_conversations

def create_thread_and_run(user_input):
    thread = client.beta.threads.create()
    run = client.beta.threads.runs.create_and_poll(
      thread_id=thread.id,
      assistant_id=assistant.id,
      instructions=f"""\
        keywords: ['거리&골목길', '건축물', '공원', '궁궐', '광화문&종로', '다리', '산', '서촌&북촌', '식물', '역사 문화 공간', '자연산책로', '캠퍼스', '야경&전망', '테마파크', '한강']
        Example 1:
        Input: Mood/Preference - '{example_conversations[0]['input']}'
        Output: {example_conversations[0]['output']}
        
        Example 2:
        Input: Mood/Preference - '{example_conversations[1]['input']}'
        Output: {example_conversations[1]['output']}

        Example 3:
        Input: Mood/Preference - '{example_conversations[2]['input']}'
        Output: {example_conversations[3]['output']}

        Example 4:
        Input: Mood/Preference - '{example_conversations[3]['input']}'
        Output: {example_conversations[3]['output']}

        Example 5:
        Input: Mood/Preference - '{example_conversations[4]['input']}'
        Output: {example_conversations[4]['output']}
        
        Example 6:
        Input: Mood/Preference - '{example_conversations[5]['input']}'
        Output: {example_conversations[5]['output']}
        
        Example 7:
        Input: Mood/Preference - '{example_conversations[6]['input']}'
        Output: {example_conversations[6]['output']}

        Example 8:
        Input: Mood/Preference - '{example_conversations[7]['input']}'
        Output: {example_conversations[7]['output']}          
        
        You have to respond in Korean:
        Input: Mood/Preference - '{user_input}'
        Output:
      """,
    )
    return run, thread.id

def get_latest_message(thread_id):
    message = client.beta.threads.messages.list(thread_id=thread_id, order="desc", limit=1)
    if message.data:
        content_block = message.data[0].content[0]
        if content_block.type == 'text':
            return content_block.text.value
    return None