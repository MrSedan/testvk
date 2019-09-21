import vk_api
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotEventType, VkBotLongPoll
from inf import tok, botid
vk_session = vk_api.VkApi(token=tok)
vk = vk_session.get_api()
longpoll = VkBotLongPoll(vk_session, botid)
def send(text,attach=0):
    vk.messages.send(
        peer_id=event.obj.peer_id,
        random_id=get_random_id(),
        message=text,
        attachment=attach
    )

for event in longpoll.listen()s:
    if event.type == VkBotEventType.MESSAGE_NEW:
        send("Test")